# Generated annotation browsing view. The authored CSV is never modified.
param([string]$Python = 'python')
$ErrorActionPreference = 'Stop'
Import-Module ImportExcel -MinimumVersion 7.8.10 -ErrorAction Stop
$repo = (Resolve-Path (Join-Path $PSScriptRoot '../..')).Path
$index = Join-Path $repo 'reference/indexes/animehistory'
$sourcePath = Join-Path $index 'category-index.csv'
$sourceHash = (Get-FileHash -LiteralPath $sourcePath).Hash
$stage = Join-Path $repo ('.tmp/category-workbook/' + [guid]::NewGuid().ToString('N'))
New-Item -ItemType Directory -Path $stage -Force | Out-Null
$dataPath = Join-Path $stage 'joined.json'
& $Python (Join-Path $PSScriptRoot 'category_index.py') view-data --output $dataPath
if ($LASTEXITCODE -ne 0) { throw 'Category validation/join failed' }
$data = @(Get-Content -LiteralPath $dataPath -Raw -Encoding UTF8 | ConvertFrom-Json)
$output = Join-Path $stage 'category-review.xlsx'
$columns = @('Open image','web_timestamp','image_id','screening_status','categories','subjects',
 'subject_details','visual_summary','presentation','scene_group_id','scene_summary','research_priority',
 'revisit_reason','uncertainties','identification_confidence','detail_status','reported_context',
 'screened_by','screened_utc','detail_reviewed_by','detail_reviewed_utc','detail_references',
 'image_key','episode_id','episode_number','locator_ordinal','episode_title','web_seconds',
 'image_url','source_page_url','alignment_status')
$widths = @(14,19,15,23,34,32,36,80,17,20,65,22,70,80,29,22,75,20,31,24,31,60,24,17,20,20,40,20,65,65,23)
$expected = @{}
$summaries = @()
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
   if ($rows[$i].screening_status -ne 'UNREVIEWED') { $sheet.Row($i+6).Height = 60 }
  }
  $summaries += [pscustomobject][ordered]@{Episode=$id;Records=$rows.Count;
   Screened=@($rows | Where-Object screening_status -eq 'SCREENED').Count;
   Recheck=@($rows | Where-Object screening_status -eq 'NEEDS_RECHECK').Count;
   Unavailable=@($rows | Where-Object screening_status -eq 'UNAVAILABLE').Count;
   Unreviewed=@($rows | Where-Object screening_status -eq 'UNREVIEWED').Count;
   'Detail partial'=@($rows | Where-Object detail_status -eq 'PARTIAL').Count;
   'Detail reviewed'=@($rows | Where-Object detail_status -eq 'REVIEWED').Count}
 }
 $null = $summaries | Export-Excel -ExcelPackage $package -WorksheetName Overview -StartRow 6 -TableName CategoryCoverage -TableStyle Medium2 -PassThru
 $overview.Cells[2,1].Value = 'Episode reference coverage'
 $overview.Cells[2,1].Style.Font.Size = 14
 $overview.Cells[4,1].Value = 'Counts describe sampled gallery images. Recheck and unavailable remain unresolved.'
 $overview.Cells[35,1].Value = 'Edit the authored CSV; refresh replaces this workbook. No detailed review implied by screening.'
 $overview.View.ShowGridLines = $false
 $overview.Cells[1,1,35,8].Style.Font.Name = 'Arial'
 $overview.Cells[1,1,35,8].Style.Font.Size = 10
 $overview.Column(1).Width = 16
 for ($c=2;$c -le 8;$c++) { $overview.Column($c).Width = 20 }
 for ($i=0;$i -lt 26;$i++) {
  $overview.Cells[($i+7),1].Hyperlink = [OfficeOpenXml.ExcelHyperLink]::new("'$($summaries[$i].Episode)'!A1",$summaries[$i].Episode)
 }
 $package.Save()
} finally { $package.Dispose() }

$check = Open-ExcelPackage -Path $output
try {
 if ($check.Workbook.Worksheets.Count -ne 27) { throw 'Worksheet count mismatch' }
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
  foreach ($c in 1..8) {
   $field = @($summaries[$i].PSObject.Properties.Name)[$c-1]
   if ([string]$check.Workbook.Worksheets['Overview'].Cells[($i+7),$c].Value -cne [string]$summaries[$i].$field) { throw 'Coverage summary mismatch' }
  }
 }
} finally { $check.Dispose() }
if ((Get-FileHash -LiteralPath $sourcePath).Hash -ne $sourceHash) { throw 'Authored CSV changed during build; refusing stale view' }
Move-Item -LiteralPath $output -Destination (Join-Path $index 'category-review.xlsx') -Force
Remove-Item -LiteralPath $dataPath
Remove-Item -LiteralPath $stage
[pscustomobject]@{Output=(Join-Path $index 'category-review.xlsx');Records=$data.Count;Sheets=27;VerifiedCells=$verified;VerifiedImageLinks=$links;AuthoredCsvUnchanged=$true} | ConvertTo-Json
