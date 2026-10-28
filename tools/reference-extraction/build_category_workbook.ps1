# Generated annotation browsing view. The authored CSV is never modified.
param([string]$Python = 'python', [switch]$VerifyAlignmentMedia, [string]$FFprobe = 'ffprobe')
$ErrorActionPreference = 'Stop'
Import-Module ImportExcel -MinimumVersion 7.8.10 -ErrorAction Stop
$repo = (Resolve-Path (Join-Path $PSScriptRoot '../..')).Path
$index = Join-Path $repo 'reference/indexes/animehistory'
$sourcePath = Join-Path $index 'category-index.csv'
$sourceHash = (Get-FileHash -LiteralPath $sourcePath).Hash
$supplementPath = Join-Path $index 'supplemental-index.csv'
$supplementHash = if (Test-Path -LiteralPath $supplementPath) { (Get-FileHash -LiteralPath $supplementPath).Hash } else { '' }
$inputHashes = @{}
$inputPaths = @((Get-ChildItem -LiteralPath $index -Filter '*.csv').FullName)
$inputPaths += @((Get-ChildItem -LiteralPath (Join-Path $index 'CSVs') -Filter 'episode-*.csv').FullName)
$inputPaths += (Join-Path $repo 'reference/indexes/performance-subtitle-coverage.json')
foreach ($path in $inputPaths) { $inputHashes[$path] = (Get-FileHash -LiteralPath $path).Hash }
$stage = Join-Path $repo ('.tmp/category-workbook/' + [guid]::NewGuid().ToString('N'))
New-Item -ItemType Directory -Path $stage -Force | Out-Null
$dataPath = Join-Path $stage 'joined.json'
& $Python (Join-Path $PSScriptRoot 'category_index.py') view-data --output $dataPath
if ($LASTEXITCODE -ne 0) { throw 'Category validation/join failed' }
$jsonOptions = @{}
if ((Get-Command ConvertFrom-Json).Parameters.ContainsKey('DateKind')) { $jsonOptions.DateKind = 'String' }
$data = @(Get-Content -LiteralPath $dataPath -Raw -Encoding UTF8 | ConvertFrom-Json @jsonOptions)
$manualPath = Join-Path $stage 'manual.json'
& $Python (Join-Path $PSScriptRoot 'category_index.py') supplement-data --output $manualPath
if ($LASTEXITCODE -ne 0) { throw 'Manual reference validation/join failed' }
$manual = @(Get-Content -LiteralPath $manualPath -Raw -Encoding UTF8 | ConvertFrom-Json @jsonOptions)
$alignmentPath = Join-Path $stage 'alignment.json'
$projectionArgs = @((Join-Path $repo 'tools/reference-alignment/projection.py'),'--output',$alignmentPath)
if ($VerifyAlignmentMedia) { $projectionArgs += @('--verify-current','--ffprobe',$FFprobe) }
& $Python @projectionArgs
if ($LASTEXITCODE -ne 0) { throw 'Alignment projection failed; existing workbook preserved' }
$alignment = Get-Content -LiteralPath $alignmentPath -Raw -Encoding UTF8 | ConvertFrom-Json @jsonOptions
$timingFields = @('matched_local_start','matched_local_end','estimated_local_time','timing_basis','mapping_id',
 'alignment_availability','suggested_search_half_window_seconds','anchor_id','anchor_status','alignment_input_id',
 'alignment_method','alignment_reason','alignment_checked_utc','matched_local_start_seconds',
 'matched_local_end_seconds','estimated_local_seconds')
$numericTiming = @('suggested_search_half_window_seconds','matched_local_start_seconds','matched_local_end_seconds','estimated_local_seconds')
foreach ($pair in @(@{Rows=$data;Timing=@($alignment.gallery_timing)},@{Rows=$manual;Timing=@($alignment.manual_timing)})) {
 $byKey = @{}
 foreach ($row in $pair.Timing) {
  if ($byKey.ContainsKey($row.image_key)) { throw 'Duplicate timing projection key' }
  $byKey[$row.image_key] = $row
 }
 if ($byKey.Count -ne $pair.Rows.Count) { throw 'Timing projection row count mismatch' }
 foreach ($row in $pair.Rows) {
  if (-not $byKey.ContainsKey($row.image_key)) { throw 'Missing timing projection key' }
  foreach ($field in $timingFields) { $row | Add-Member -NotePropertyName $field -NotePropertyValue $byKey[$row.image_key].$field }
 }
}
$output = Join-Path $stage 'category-review.xlsx'
foreach ($record in @($data) + @($manual)) {
 foreach ($field in @('screened_utc','detail_reviewed_utc')) {
  if ($record.$field -is [datetime]) { throw 'JSON review timestamps must remain strings; run with PowerShell 7.5 or newer.' }
 }
}
$columns = @('Open image','web_timestamp','image_id','screening_status','categories','subjects',
 'subject_details','visual_summary','presentation','scene_group_id','scene_summary','research_priority',
 'revisit_reason','uncertainties','identification_confidence','detail_status','reported_context',
 'screened_by','screened_utc','detail_reviewed_by','detail_reviewed_utc','detail_references',
 'image_key','episode_id','episode_number','locator_ordinal','episode_title','web_seconds',
 'image_url','source_page_url','alignment_status')
$widths = @(14,19,15,23,34,32,36,80,17,20,65,22,70,80,29,32,75,20,31,24,31,60,24,17,20,20,40,20,65,65,23)
$primaryTiming = @('estimated_local_time','matched_local_start','matched_local_end','timing_basis',
 'alignment_availability','mapping_id','suggested_search_half_window_seconds')
$metadataTiming = @($timingFields | Where-Object { $_ -notin $primaryTiming })
$columns = @($columns[0..1]) + $primaryTiming + @($columns[2..($columns.Count-1)]) + $metadataTiming
$widths = @($widths[0..1]) + @(24,24,24,24,29,23,37) + @($widths[2..($widths.Count-1)]) + @(23,26,68,34,75,32,32,32,32)
$expected = @{}
$summaries = @()
$manualTable = @()
$manualColumns = @()
$alignmentTables = @{}
$alignmentColumns = @{}
$galleryTargets = @{}
$package = Open-ExcelPackage -Path $output -Create
try {
 $overview = $package.Workbook.Worksheets.Add('Overview')
 foreach ($n in 1..26) {
  $id = 'EP-{0:D2}' -f $n
  $rows = @($data | Where-Object episode_id -eq $id)
  $table = @($rows | ForEach-Object {
   $item = [ordered]@{'Open image'='View image'}
   foreach ($column in $columns | Select-Object -Skip 1) { $item[$column] = $_.$column }
   [pscustomobject]$item
  })
  $expected[$id] = $table
  $null = $table | Export-Excel -ExcelPackage $package -WorksheetName $id -StartRow 5 -TableName ('Category{0:D2}' -f $n) -TableStyle Medium2 -NoNumberConversion '*' -NoHyperLinkConversion '*' -PassThru
  $sheet = $package.Workbook.Worksheets[$id]
  $sheet.Cells[2,1].Value = "$id category screening"
  $sheet.Cells[2,1].Style.Font.Size = 14
  $sheet.Cells[3,1].Value = 'Generated view. Times: direct intervals / bounded model estimates / unmapped. Check availability; edit CSVs, not this workbook.'
  $sheet.View.ShowGridLines = $false
  $sheet.View.FreezePanes(6,4)
  $sheet.Cells[5,1,($rows.Count+5),$columns.Count].Style.Font.Name = 'Arial'
  $sheet.Cells[5,1,($rows.Count+5),$columns.Count].Style.Font.Size = 10
  $sheet.Cells[5,1,($rows.Count+5),$columns.Count].Style.VerticalAlignment = 'Center'
  $sheet.Cells[5,1,5,$columns.Count].Style.WrapText = $true
  $sheet.Row(5).Height = 42
  for ($c=1;$c -le $columns.Count;$c++) { $sheet.Column($c).Width = $widths[$c-1] }
  for ($i=0;$i -lt $rows.Count;$i++) {
   $r = $i+6
   for ($c=1;$c -lt $columns.Count;$c++) {
    if ([string]$table[$i].($columns[$c]) -eq '') { $sheet.Cells[$r,($c+1)].Value = $null }
   }
   $sheet.Cells[$r,1].Hyperlink = [uri]$rows[$i].image_url
   $sheet.Cells[$r,1].Style.Font.Color.SetColor([System.Drawing.Color]::FromArgb(29,78,216))
   foreach ($column in @('episode_number','locator_ordinal','web_seconds') + $numericTiming) {
    $c = [array]::IndexOf($columns,$column)+1
    if ($null -ne $rows[$i].$column -and [string]$rows[$i].$column -ne '') {
     $sheet.Cells[$r,$c].Value = [double]$rows[$i].$column
     $sheet.Cells[$r,$c].Style.Numberformat.Format = if ($column -in $numericTiming) { '0.000' } else { '0' }
    }
   }
   $galleryTargets[$rows[$i].image_key] = "'$id'!A$r"
   $sheet.Row($r).Height = 22
  }
  foreach ($column in @('categories','subjects','subject_details','visual_summary','uncertainties','revisit_reason','reported_context','scene_summary')) {
   $c = [array]::IndexOf($columns,$column)+1
   $sheet.Cells[6,$c,($rows.Count+5),$c].Style.WrapText = $true
  }
  # Give authored text enough height without expanding untouched rows.
  for ($i=0;$i -lt $rows.Count;$i++) {
   if ($rows[$i].screening_status -ne 'UNREVIEWED') {
    $lineEstimate = 1
    foreach ($column in @('categories','subjects','subject_details','visual_summary','uncertainties','revisit_reason','reported_context','scene_summary')) {
     $c = [array]::IndexOf($columns,$column)+1
     $usableWidth = [Math]::Max(1,$sheet.Column($c).Width * 0.85)
     $lines = 0
     foreach ($part in ([string]$rows[$i].$column -split '\r?\n')) { $lines += [Math]::Max(1,[Math]::Ceiling($part.Length / $usableWidth)) }
     $lineEstimate = [Math]::Max($lineEstimate,$lines)
    }
    $sheet.Row($i+6).Height = [Math]::Min(300,[Math]::Max(60,$lineEstimate * 13 + 12))
   }
  }
  $summaries += [pscustomobject][ordered]@{Episode=$id;Records=$rows.Count;
   Screened=@($rows | Where-Object screening_status -eq 'SCREENED').Count;
   Recheck=@($rows | Where-Object screening_status -eq 'NEEDS_RECHECK').Count;
   Unavailable=@($rows | Where-Object screening_status -eq 'UNAVAILABLE').Count;
   Unreviewed=@($rows | Where-Object screening_status -eq 'UNREVIEWED').Count;
   'Initial review complete'=@($rows | Where-Object detail_status -eq 'INITIAL_REVIEW_COMPLETE').Count;
   'Deep dive partial'=@($rows | Where-Object detail_status -eq 'PARTIAL').Count;
   'Deep dive reviewed'=@($rows | Where-Object detail_status -eq 'REVIEWED').Count}
 }
 $null = $summaries | Export-Excel -ExcelPackage $package -WorksheetName Overview -StartRow 6 -TableName CategoryCoverage -TableStyle Medium2 -PassThru
 $overview.Cells[2,1].Value = 'Episode reference coverage'
 $overview.Cells[2,1].Style.Font.Size = 14
 $overview.Cells[4,1].Value = 'Counts describe sampled gallery images. Recheck and unavailable remain unresolved.'
 $overview.Cells[35,1].Value = 'Initial review complete = annotated survey. Deep dive counts cover scoped questions; see the index README.'
 $overview.Cells[42,1].Value = 'Alignment evidence and navigation (separate from review progress)'
 $overview.Cells[43,1].Value = 'Alignment anchors'
 $overview.Cells[43,2].Value = @($alignment.anchors).Count
 $overview.Cells[43,1].Hyperlink = [OfficeOpenXml.ExcelHyperLink]::new("'Alignment anchors'!A1",'Alignment anchors')
 $overview.Cells[44,1].Value = 'Alignment mappings'
 $overview.Cells[44,2].Value = @($alignment.mappings).Count
 $overview.Cells[44,1].Hyperlink = [OfficeOpenXml.ExcelHyperLink]::new("'Alignment mappings'!A1",'Alignment mappings')
 $overview.Cells[46,1].Value = 'Direct matches'
 $overview.Cells[46,2].Value = $alignment.report.timing_basis.DIRECT_MATCH
 $overview.Cells[47,1].Value = 'Model estimates'
 $overview.Cells[47,2].Value = $alignment.report.timing_basis.MAPPING_ESTIMATE
 $overview.Cells[48,1].Value = 'Unmapped'
 $overview.Cells[48,2].Value = $alignment.report.timing_basis.UNMAPPED
 $overview.Cells[50,1].Value = 'Timing is release- and segment-specific. See Alignment mappings for episodes, ranges and coefficients; never reuse another episode offset.'
 $overview.Cells[51,1].Value = 'Direct timestamps describe reviewed intervals; model timestamps are navigation estimates. Blank is not zero.'
 $overview.Cells[52,1].Value = if ($VerifyAlignmentMedia) { 'Explicit current-input verification requested; each row records its result and check time.' } else { 'Routine build: video digests not recomputed. Recorded alignment is labeled RECORDED_UNCHECKED.' }
 $overview.Cells[1,1,52,9].Style.Font.Name = 'Arial'
 $overview.Cells[1,1,52,9].Style.Font.Size = 10
 $overview.Cells[42,1].Style.Font.Bold = $true
 $overview.Column(1).Width = 25
 $overview.View.ShowGridLines = $false
 $overview.Cells[1,1,35,9].Style.Font.Name = 'Arial'
 $overview.Cells[1,1,35,9].Style.Font.Size = 10
 $overview.Column(1).Width = 16
 for ($c=2;$c -le 9;$c++) { $overview.Column($c).Width = 20 }
 $overview.Column(7).Width = 27
 for ($i=0;$i -lt 26;$i++) {
  $overview.Cells[($i+7),1].Hyperlink = [OfficeOpenXml.ExcelHyperLink]::new("'$($summaries[$i].Episode)'!A1",$summaries[$i].Episode)
 }
 if ($manual.Count -gt 0) {
  $manualColumns = @('Open image','local_timestamp','image_id','episode_id','alignment_status','media_availability',
   'categories','subjects','subject_details','visual_summary','related_gallery_ids')
  $manualColumns += @($manual[0].PSObject.Properties.Name | Where-Object { $_ -notin $manualColumns })
  $manualTable = @($manual | ForEach-Object {
   $item = [ordered]@{'Open image'='View screenshot'}
   foreach ($column in $manualColumns | Select-Object -Skip 1) { $item[$column] = $_.$column }
   [pscustomobject]$item
  })
  $null = $manualTable | Export-Excel -ExcelPackage $package -WorksheetName 'Manual references' -StartRow 5 -TableName ManualReferences -TableStyle Medium2 -NoNumberConversion '*' -NoHyperLinkConversion '*' -PassThru
  $sheet = $package.Workbook.Worksheets['Manual references']
  $sheet.Cells[2,1].Value = 'Manual episode references'
  $sheet.Cells[2,1].Style.Font.Size = 14
  $sheet.Cells[3,1].Value = 'NOT_LOCAL images require archive restore before opening. Player times are unreconciled; gallery counts remain separate.'
  $sheet.View.ShowGridLines = $false
  $sheet.View.FreezePanes(6,5)
  $sheet.Cells[5,1,($manual.Count+5),$manualColumns.Count].Style.Font.Name = 'Arial'
  $sheet.Cells[5,1,($manual.Count+5),$manualColumns.Count].Style.Font.Size = 10
  $sheet.Cells[5,1,($manual.Count+5),$manualColumns.Count].Style.VerticalAlignment = 'Center'
  $sheet.Cells[5,1,5,$manualColumns.Count].Style.WrapText = $true
  $sheet.Row(5).Height = 42
  for ($c=0;$c -lt $manualColumns.Count;$c++) {
   $field = $manualColumns[$c]
   $sheet.Column($c+1).Width = 25
   if ($field -eq 'detail_status') { $sheet.Column($c+1).Width = 32 }
   if ($field -in @('visual_summary','reported_context','uncertainties','revisit_reason','source_description','media_path')) { $sheet.Column($c+1).Width = 85 }
   if ($field -in @('categories','subjects','subject_details','media_sha256','image_key','timestamp_basis')) { $sheet.Column($c+1).Width = 40 }
   $sheet.Cells[6,($c+1),($manual.Count+5),($c+1)].Style.WrapText = $true
   for ($i=0;$i -lt $manual.Count;$i++) {
    if ([string]$manualTable[$i].$field -eq '') { $sheet.Cells[($i+6),($c+1)].Value = $null }
    if ($field -in (@('local_seconds','episode_number','media_bytes') + $numericTiming) -and $null -ne $manualTable[$i].$field -and [string]$manualTable[$i].$field -ne '') {
     $sheet.Cells[($i+6),($c+1)].Value = [double]$manualTable[$i].$field
     $sheet.Cells[($i+6),($c+1)].Style.Numberformat.Format = if ($field -in $numericTiming) { '0.000' } else { '0' }
    }
   }
  }
  for ($i=0;$i -lt $manual.Count;$i++) {
   $sheet.Cells[($i+6),1].Hyperlink = [uri]$manual[$i].media_uri
   $sheet.Cells[($i+6),1].Style.Font.Color.SetColor([System.Drawing.Color]::FromArgb(29,78,216))
   $sheet.Row($i+6).Height = 95
  }
  $overview.Cells[38,1].Value = 'Manual references (separate from gallery counts)'
  $overview.Cells[39,1].Value = 'Total'
  $overview.Cells[39,2].Value = $manual.Count
  $overview.Cells[39,1].Hyperlink = [OfficeOpenXml.ExcelHyperLink]::new("'Manual references'!A1",'Total')
 }
 foreach ($spec in @(
  @{Name='Alignment anchors';Rows=@($alignment.anchors);First=@('anchor_id','episode_id','image_id','web_timestamp','role','status','match_kind','matched_local_start','matched_local_end','alignment_availability','notes','reviewer','reviewed_utc','method');Table='AlignmentAnchors'},
  @{Name='Alignment mappings';Rows=@($alignment.mappings);First=@('mapping_id','episode_id','status','segment_label','web_range','model','scale','offset_seconds','fit_count','holdout_count','alignment_availability','limitations');Table='AlignmentMappings'})) {
  if ($spec.Rows.Count -eq 0) { throw 'Alignment register is empty; no recorded evidence to project' }
  $fields = @($spec.First) + @($spec.Rows[0].PSObject.Properties.Name | Where-Object { $_ -notin $spec.First })
  $table = @($spec.Rows | ForEach-Object {
   $item = [ordered]@{}
   foreach ($field in $fields) { $item[$field] = $_.$field }
   [pscustomobject]$item
  })
  $alignmentTables[$spec.Name] = $table; $alignmentColumns[$spec.Name] = $fields
  $null = $table | Export-Excel -ExcelPackage $package -WorksheetName $spec.Name -StartRow 5 -TableName $spec.Table -TableStyle Medium2 -NoNumberConversion '*' -NoHyperLinkConversion '*' -PassThru
  $sheet = $package.Workbook.Worksheets[$spec.Name]
  $sheet.Cells[2,1].Value = $spec.Name
  $sheet.Cells[2,1].Style.Font.Size = 14
  $sheet.Cells[3,1].Value = 'Generated evidence/history view. Only active MATCHED anchors / VALIDATED bounded mappings can supply derived times. Edit the owning CSV.'
  $sheet.View.ShowGridLines = $false; $sheet.View.FreezePanes(6,4)
  $sheet.Cells[5,1,($table.Count+5),$fields.Count].Style.Font.Name = 'Arial'
  $sheet.Cells[5,1,($table.Count+5),$fields.Count].Style.Font.Size = 10
  $sheet.Cells[5,1,($table.Count+5),$fields.Count].Style.VerticalAlignment = 'Top'
  $sheet.Cells[5,1,5,$fields.Count].Style.WrapText = $true
  $sheet.Row(5).Height = 42
  for ($c=0;$c -lt $fields.Count;$c++) {
   $field=$fields[$c]; $sheet.Column($c+1).Width = 25
   if ($field -in @('notes','limitations','recipe_json')) { $sheet.Column($c+1).Width = 85 }
   if ($field -in @('input_id','video_sha256','subtitle_sha256','locator_sha256','image_sha256','alignment_input_id')) { $sheet.Column($c+1).Width = 68 }
   if ($field -in @('fit_anchor_ids','holdout_anchor_ids','video_source')) { $sheet.Column($c+1).Width = 65 }
   $sheet.Cells[6,($c+1),($table.Count+5),($c+1)].Style.WrapText = $true
   for ($i=0;$i -lt $table.Count;$i++) {
    $value=$table[$i].$field
    if ([string]$value -eq '') { $sheet.Cells[($i+6),($c+1)].Value=$null }
    if ($field -in @('fit_count','holdout_count') -and $null -ne $value) { $sheet.Cells[($i+6),($c+1)].Value=[int]$value }
    if (([string]$value).Length -gt 32767) { throw 'Alignment field exceeds Excel cell capacity' }
   }
  }
  for ($i=0;$i -lt $table.Count;$i++) {
   $sheet.Row($i+6).Height=100
   if ($spec.Name -eq 'Alignment anchors') {
    $target=$galleryTargets[$spec.Rows[$i].image_key]
    if (-not $target) { throw 'Anchor gallery link cannot resolve' }
    $sheet.Cells[($i+6),3].Hyperlink=[OfficeOpenXml.ExcelHyperLink]::new($target,$table[$i].image_id)
   }
  }
 }
 $package.Save()
} finally { $package.Dispose() }

$check = Open-ExcelPackage -Path $output
try {
 $sheetCount = 29 + [int]($manual.Count -gt 0)
 if ($check.Workbook.Worksheets.Count -ne $sheetCount) { throw 'Worksheet count mismatch' }
 $verified = 0; $links = 0
 foreach ($n in 1..26) {
  $id = 'EP-{0:D2}' -f $n
  $sheet = $check.Workbook.Worksheets[$id]; $rows = $expected[$id]
  if ($sheet.Tables.Count -ne 1 -or $sheet.Dimension.End.Row -ne $rows.Count+5) { throw "Table/row mismatch: $id" }
  if ($sheet.View.Panes.Count -eq 0) { throw "Missing frozen headers: $id" }
  for ($c=0;$c -lt $columns.Count;$c++) {
   if ($sheet.Cells[5,($c+1)].Value -cne $columns[$c]) { throw "Header mismatch: $id" }
   for ($i=0;$i -lt $rows.Count;$i++) {
    if ([string]$sheet.Cells[($i+6),($c+1)].Value -cne [string]$rows[$i].($columns[$c])) { throw "Value mismatch: $id / $i / $($columns[$c])" }
    if ($sheet.Cells[($i+6),($c+1)].Formula) { throw 'Unexpected formula in browsing data' }
    $verified++
   }
  }
  for ($i=0;$i -lt $rows.Count;$i++) {
   if ($sheet.Cells[($i+6),1].Hyperlink.AbsoluteUri -ne $rows[$i].image_url) { throw "Image link mismatch: $id / $i" }
   $links++
  }
 }
 foreach ($i in 0..25) {
  foreach ($c in 1..9) {
   $field = @($summaries[$i].PSObject.Properties.Name)[$c-1]
   if ([string]$check.Workbook.Worksheets['Overview'].Cells[($i+7),$c].Value -cne [string]$summaries[$i].$field) { throw 'Coverage summary mismatch' }
  }
 }
 $manualVerified = 0
 if ($manual.Count -gt 0) {
  $sheet = $check.Workbook.Worksheets['Manual references']
  if ($sheet.Tables.Count -ne 1 -or $sheet.Dimension.End.Row -ne $manual.Count+5) { throw 'Manual table/row mismatch' }
  for ($c=0;$c -lt $manualColumns.Count;$c++) {
   if ($sheet.Cells[5,($c+1)].Value -cne $manualColumns[$c]) { throw 'Manual header mismatch' }
   for ($i=0;$i -lt $manual.Count;$i++) {
    if ([string]$sheet.Cells[($i+6),($c+1)].Value -cne [string]$manualTable[$i].($manualColumns[$c])) { throw "Manual value mismatch: $i / $($manualColumns[$c])" }
    if ($sheet.Cells[($i+6),($c+1)].Formula) { throw 'Unexpected formula in manual data' }
    $manualVerified++
   }
  }
  for ($i=0;$i -lt $manual.Count;$i++) {
   if ($sheet.Cells[($i+6),1].Hyperlink.AbsoluteUri -cne $manual[$i].media_uri) { throw 'Manual media link mismatch' }
  }
  if ($check.Workbook.Worksheets['Overview'].Cells[39,2].Value -ne $manual.Count) { throw 'Manual overview count mismatch' }
 }
 $alignmentVerified=0
 foreach ($name in @('Alignment anchors','Alignment mappings')) {
  $sheet=$check.Workbook.Worksheets[$name]; $rows=$alignmentTables[$name]; $fields=$alignmentColumns[$name]
  if ($sheet.Tables.Count -ne 1 -or $sheet.Dimension.End.Row -ne $rows.Count+5) { throw "Alignment table/row mismatch: $name" }
  for ($c=0;$c -lt $fields.Count;$c++) {
   if ($sheet.Cells[5,($c+1)].Value -cne $fields[$c]) { throw 'Alignment header mismatch' }
   for ($i=0;$i -lt $rows.Count;$i++) {
    if ([string]$sheet.Cells[($i+6),($c+1)].Value -cne [string]$rows[$i].($fields[$c])) { throw "Alignment value mismatch: $name / $i / $($fields[$c])" }
    if ($sheet.Cells[($i+6),($c+1)].Formula) { throw 'Unexpected alignment formula' }
    $alignmentVerified++
   }
  }
 }
 for ($i=0;$i -lt @($alignment.anchors).Count;$i++) {
  $link=$check.Workbook.Worksheets['Alignment anchors'].Cells[($i+6),3].Hyperlink
  if ($link.ReferenceAddress -cne $galleryTargets[$alignment.anchors[$i].image_key]) { throw 'Anchor gallery link mismatch' }
 }
 if ($check.Workbook.Worksheets['Overview'].Cells[43,2].Value -ne @($alignment.anchors).Count -or $check.Workbook.Worksheets['Overview'].Cells[44,2].Value -ne @($alignment.mappings).Count) { throw 'Alignment overview count mismatch' }
} finally { $check.Dispose() }
if ((Get-FileHash -LiteralPath $sourcePath).Hash -ne $sourceHash) { throw 'Authored CSV changed during build; refusing stale view' }
if ($supplementHash -and (Get-FileHash -LiteralPath $supplementPath).Hash -ne $supplementHash) { throw 'Supplement CSV changed during build' }
foreach ($path in $inputHashes.Keys) { if ((Get-FileHash -LiteralPath $path).Hash -ne $inputHashes[$path]) { throw "Input changed during build; refusing stale view: $path" } }
Move-Item -LiteralPath $output -Destination (Join-Path $index 'category-review.xlsx') -Force
Remove-Item -LiteralPath $dataPath
Remove-Item -LiteralPath $manualPath
Remove-Item -LiteralPath $alignmentPath
Remove-Item -LiteralPath $stage
[pscustomobject]@{Output=(Join-Path $index 'category-review.xlsx');Records=$data.Count;ManualReferences=$manual.Count;Sheets=$sheetCount;VerifiedCells=$verified;VerifiedImageLinks=$links;VerifiedManualCells=$manualVerified;VerifiedAlignmentCells=$alignmentVerified;AlignmentReport=$alignment.report;AuthoredCsvUnchanged=$true} | ConvertTo-Json -Depth 5
