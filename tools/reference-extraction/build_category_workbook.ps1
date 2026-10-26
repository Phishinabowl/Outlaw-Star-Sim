# Generated annotation browsing view. The authored CSV is never modified.
param([string]$Python = 'python')
$ErrorActionPreference = 'Stop'
Import-Module ImportExcel -MinimumVersion 7.8.10 -ErrorAction Stop
$repo = (Resolve-Path (Join-Path $PSScriptRoot '../..')).Path
$index = Join-Path $repo 'reference/indexes/animehistory'
$sourcePath = Join-Path $index 'category-index.csv'
$sourceHash = (Get-FileHash -LiteralPath $sourcePath).Hash
$supplementPath = Join-Path $index 'supplemental-index.csv'
$supplementHash = if (Test-Path -LiteralPath $supplementPath) { (Get-FileHash -LiteralPath $supplementPath).Hash } else { '' }
$stage = Join-Path $repo ('.tmp/category-workbook/' + [guid]::NewGuid().ToString('N'))
New-Item -ItemType Directory -Path $stage -Force | Out-Null
$dataPath = Join-Path $stage 'joined.json'
& $Python (Join-Path $PSScriptRoot 'category_index.py') view-data --output $dataPath
if ($LASTEXITCODE -ne 0) { throw 'Category validation/join failed' }
$data = @(Get-Content -LiteralPath $dataPath -Raw -Encoding UTF8 | ConvertFrom-Json)
$manualPath = Join-Path $stage 'manual.json'
& $Python (Join-Path $PSScriptRoot 'category_index.py') supplement-data --output $manualPath
if ($LASTEXITCODE -ne 0) { throw 'Manual reference validation/join failed' }
$manual = @(Get-Content -LiteralPath $manualPath -Raw -Encoding UTF8 | ConvertFrom-Json)
$output = Join-Path $stage 'category-review.xlsx'
$columns = @('Open image','web_timestamp','image_id','screening_status','categories','subjects',
 'subject_details','visual_summary','presentation','scene_group_id','scene_summary','research_priority',
 'revisit_reason','uncertainties','identification_confidence','detail_status','reported_context',
 'screened_by','screened_utc','detail_reviewed_by','detail_reviewed_utc','detail_references',
 'image_key','episode_id','episode_number','locator_ordinal','episode_title','web_seconds',
 'image_url','source_page_url','alignment_status')
$widths = @(14,19,15,23,34,32,36,80,17,20,65,22,70,80,29,32,75,20,31,24,31,60,24,17,20,20,40,20,65,65,23)
$expected = @{}
$summaries = @()
$manualTable = @()
$manualColumns = @()
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
  $sheet.Cells[3,1].Value = 'Generated view. Save annotations in category-index.csv. Web times are unaligned.'
  $sheet.View.ShowGridLines = $false
  $sheet.View.FreezePanes(6,4)
  $sheet.Cells[5,1,($rows.Count+5),$columns.Count].Style.Font.Name = 'Arial'
  $sheet.Cells[5,1,($rows.Count+5),$columns.Count].Style.Font.Size = 10
  $sheet.Cells[5,1,($rows.Count+5),$columns.Count].Style.VerticalAlignment = 'Center'
  for ($c=1;$c -le $columns.Count;$c++) { $sheet.Column($c).Width = $widths[$c-1] }
  for ($i=0;$i -lt $rows.Count;$i++) {
   $r = $i+6
   for ($c=1;$c -lt $columns.Count;$c++) {
    if ([string]$table[$i].($columns[$c]) -eq '') { $sheet.Cells[$r,($c+1)].Value = $null }
   }
   $sheet.Cells[$r,1].Hyperlink = [uri]$rows[$i].image_url
   $sheet.Cells[$r,1].Style.Font.Color.SetColor([System.Drawing.Color]::FromArgb(29,78,216))
   foreach ($column in @('episode_number','locator_ordinal','web_seconds')) {
    $c = [array]::IndexOf($columns,$column)+1
    $sheet.Cells[$r,$c].Value = [int]$rows[$i].$column
    $sheet.Cells[$r,$c].Style.Numberformat.Format = '0'
   }
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
  for ($c=0;$c -lt $manualColumns.Count;$c++) {
   $field = $manualColumns[$c]
   $sheet.Column($c+1).Width = 25
   if ($field -eq 'detail_status') { $sheet.Column($c+1).Width = 32 }
   if ($field -in @('visual_summary','reported_context','uncertainties','revisit_reason','source_description','media_path')) { $sheet.Column($c+1).Width = 85 }
   if ($field -in @('categories','subjects','subject_details','media_sha256','image_key','timestamp_basis')) { $sheet.Column($c+1).Width = 40 }
   $sheet.Cells[6,($c+1),($manual.Count+5),($c+1)].Style.WrapText = $true
   for ($i=0;$i -lt $manual.Count;$i++) {
    if ([string]$manualTable[$i].$field -eq '') { $sheet.Cells[($i+6),($c+1)].Value = $null }
    if ($field -in @('local_seconds','episode_number','media_bytes')) {
     $sheet.Cells[($i+6),($c+1)].Value = [int64]$manualTable[$i].$field
     $sheet.Cells[($i+6),($c+1)].Style.Numberformat.Format = '0'
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
 $package.Save()
} finally { $package.Dispose() }

$check = Open-ExcelPackage -Path $output
try {
 $sheetCount = 27 + [int]($manual.Count -gt 0)
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
} finally { $check.Dispose() }
if ((Get-FileHash -LiteralPath $sourcePath).Hash -ne $sourceHash) { throw 'Authored CSV changed during build; refusing stale view' }
if ($supplementHash -and (Get-FileHash -LiteralPath $supplementPath).Hash -ne $supplementHash) { throw 'Supplement CSV changed during build' }
Move-Item -LiteralPath $output -Destination (Join-Path $index 'category-review.xlsx') -Force
Remove-Item -LiteralPath $dataPath
Remove-Item -LiteralPath $manualPath
Remove-Item -LiteralPath $stage
[pscustomobject]@{Output=(Join-Path $index 'category-review.xlsx');Records=$data.Count;ManualReferences=$manual.Count;Sheets=$sheetCount;VerifiedCells=$verified;VerifiedImageLinks=$links;VerifiedManualCells=$manualVerified;AuthoredCsvUnchanged=$true} | ConvertTo-Json
