# Generate the local AnimeHistory browsing workbook with ImportExcel; no network/media access.
$ErrorActionPreference = 'Stop'
Import-Module ImportExcel -MinimumVersion 7.8.10 -ErrorAction Stop
$repoRoot = (Resolve-Path (Join-Path $PSScriptRoot '../..')).Path
$root = Join-Path $repoRoot 'reference/indexes/animehistory'
$destination = Join-Path $root 'animehistory-review.xlsx'
$workDir = Join-Path $repoRoot '.tmp/animehistory-workbook'
New-Item -ItemType Directory -Path $workDir -Force | Out-Null
$output = Join-Path $workDir ('build-' + [guid]::NewGuid().ToString('N') + '.xlsx')
$fields = @('web_timestamp','image_id','caption','alignment_status','image_url','episode_id','episode_title','web_seconds','gallery_url','source_page_url','source_page','retrieved_utc','html_sha256','local_timestamp')
$widths = @(15,20,16,64,24,55,15,40,20,55,55,20,28,70,24)
$expected = @{}
$summaries = @()
$combined = @(Import-Csv -LiteralPath (Join-Path $root 'all-episodes.csv'))
$sourceIndex = 0
$package = Open-ExcelPackage -Path $output -Create
try {
 $overview = $package.Workbook.Worksheets.Add('Overview')
 foreach ($n in 1..26) {
  $id = 'EP-{0:D2}' -f $n
  $name = 'episode-{0:D2}.csv' -f $n
  $rows = @(Import-Csv -LiteralPath (Join-Path $root "CSVs/$name"))
  if ($rows.Count -ne 354) { throw "Unexpected record count: $id" }
  if (@($rows.image_id | Sort-Object -Unique).Count -ne $rows.Count) { throw "Duplicate image IDs: $id" }
  foreach ($row in $rows) {
   foreach ($field in $fields) {
    if ($sourceIndex -ge $combined.Count -or $row.$field -cne $combined[$sourceIndex].$field) { throw "Combined CSV mismatch: $id / $sourceIndex / $field" }
   }
   $sourceIndex++
  }
  $expected[$id] = $rows
  $data = @($rows | ForEach-Object {
   $item = [ordered]@{'Open image'='View image'}
   foreach ($field in $fields) { $item[$field] = $_.$field }
   [pscustomobject]$item
  })
  $null = $data | Export-Excel -ExcelPackage $package -WorksheetName $id -StartRow 5 -TableName ('Locators{0:D2}' -f $n) -TableStyle Medium2 -NoNumberConversion '*' -NoHyperLinkConversion '*' -PassThru
  $sheet = $package.Workbook.Worksheets[$id]
  $sheet.Cells[2,1].Value = "$id | $($rows[0].episode_title)"
  $sheet.Cells[2,1].Style.Font.Size = 14
  $sheet.Cells[3,1].Value = 'CSV sources remain authoritative; web times are unaligned.'
  $sheet.View.ShowGridLines = $false
  $sheet.View.FreezePanes(6,4)
  $sheet.Cells[5,1,359,15].Style.Font.Name = 'Arial'
  $sheet.Cells[5,1,359,15].Style.Font.Size = 10
  for ($c=1;$c -le 15;$c++) { $sheet.Column($c).Width = $widths[$c-1] }
  for ($i=0;$i -lt $rows.Count;$i++) {
   $r = $i+6
   $sheet.Cells[$r,1].Hyperlink = [uri]$rows[$i].image_url
   $sheet.Cells[$r,1].Style.Font.Color.SetColor([System.Drawing.Color]::FromArgb(29,78,216))
   $sheet.Cells[$r,9].Value = [int]$rows[$i].web_seconds
   $sheet.Cells[$r,12].Value = [int]$rows[$i].source_page
   $sheet.Row($r).Height = 22
  }
  $summaries += [pscustomobject][ordered]@{Episode=$id;Title=$rows[0].episode_title;Records=$rows.Count;'First web time'=$rows[0].web_timestamp;'Last web time'=$rows[-1].web_timestamp;'Local alignment'='UNVERIFIED';'Source CSV'="CSVs/$name"}
 }
 if ($sourceIndex -ne $combined.Count) { throw 'Combined CSV record count mismatch' }
 $null = $summaries | Export-Excel -ExcelPackage $package -WorksheetName Overview -StartRow 7 -TableName EpisodeOverview -TableStyle Medium2 -NoNumberConversion '*' -NoHyperLinkConversion '*' -PassThru
 $overview.Cells[2,1].Value = 'AnimeHistory episode locators'
 $overview.Cells[2,1].Style.Font.Size = 15
 $overview.Cells[4,1].Value = 'Generated browsing copy. Edit CSV sources; rebuilding replaces this workbook.'
 $overview.Cells[5,1].Value = 'Web times are unaligned locators; no images or visual annotations embedded.'
 $overview.View.ShowGridLines = $false
 $overview.Cells[1,1,35,7].Style.Font.Name = 'Arial'
 foreach ($i in 0..25) {
  $overview.Cells[(8+$i),1].Hyperlink = [OfficeOpenXml.ExcelHyperLink]::new("'$($summaries[$i].Episode)'!A1",$summaries[$i].Episode)
  $overview.Cells[(8+$i),3].Value = 354
 }
 $overview.Cells[35,2].Value = 'Total records'
 $overview.Cells[35,3].Formula = 'SUM(C8:C33)'
 $ow = @(14,46,12,22,22,23,36)
 for ($c=1;$c -le 7;$c++) { $overview.Column($c).Width = $ow[$c-1] }
 [OfficeOpenXml.CalculationExtension]::Calculate($package.Workbook)
 $package.Save()
} finally { $package.Dispose() }
$check = Open-ExcelPackage -Path $output
try {
 if ($check.Workbook.Worksheets.Count -ne 27) { throw 'Sheet count mismatch' }
 $verified = 0; $links = 0
 foreach ($n in 1..26) {
  $id = 'EP-{0:D2}' -f $n; $sheet = $check.Workbook.Worksheets[$id]; $rows = $expected[$id]
  for ($i=0;$i -lt $rows.Count;$i++) {
   for ($c=0;$c -lt $fields.Count;$c++) {
    $actual = [string]$sheet.Cells[($i+6),($c+2)].Value
    if ($actual -cne [string]$rows[$i].($fields[$c])) { throw "Data mismatch: $id / $i / $($fields[$c])" }
    $verified++
   }
   if ($sheet.Cells[($i+6),1].Hyperlink.AbsoluteUri -ne $rows[$i].image_url) { throw "Link mismatch: $id / $i" }
   $links++
  }
 }
 if ($check.Workbook.Worksheets['Overview'].Cells[35,3].Value -ne 9204) { throw 'Overview total mismatch' }

} finally { $check.Dispose() }

# Replace the generated view only after saved-file validation succeeds.
Move-Item -LiteralPath $output -Destination $destination -Force -ErrorAction Stop
[pscustomobject]@{Output=$destination;ImportExcelVersion=(Get-Module ImportExcel).Version.ToString();Sheets=27;Records=9204;VerifiedSourceFields=$verified;VerifiedImageLinks=$links} | ConvertTo-Json
