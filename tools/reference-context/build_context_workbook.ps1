# Generated ImportExcel browsing view. Maintained research and image indexes are read-only.
param([string]$Python = 'python')
$ErrorActionPreference = 'Stop'
Import-Module ImportExcel -MinimumVersion 7.8.10 -ErrorAction Stop
$repo = (Resolve-Path (Join-Path $PSScriptRoot '../..')).Path
$index = Join-Path $repo 'reference/indexes/context'
$temporaryBase = [IO.Path]::GetFullPath((Join-Path $repo '.tmp/context-workbook'))
$stage = Join-Path $temporaryBase ([guid]::NewGuid().ToString('N'))
$destination = Join-Path $index 'context-review.xlsx'

function Assert-OwnedStage {
 $resolved = [IO.Path]::GetFullPath($stage)
 if (-not $resolved.StartsWith($temporaryBase + [IO.Path]::DirectorySeparatorChar,[StringComparison]::OrdinalIgnoreCase)) {
  throw 'Temporary directory escaped the intended workspace'
 }
 $cursor = $resolved
 while ($cursor -and $cursor.Length -ge $repo.Length) {
  if (Test-Path -LiteralPath $cursor) {
   if ((Get-Item -LiteralPath $cursor -Force).Attributes -band [IO.FileAttributes]::ReparsePoint) { throw 'Temporary path contains a reparse point' }
  }
  $cursor = [IO.Path]::GetDirectoryName($cursor)
 }
}

Assert-OwnedStage
New-Item -ItemType Directory -Path $stage -Force | Out-Null
$package = $null
$check = $null
try {
 $dataPath = Join-Path $stage 'view.json'
 & $Python (Join-Path $PSScriptRoot 'context_tool.py') view-data --output $dataPath
 if ($LASTEXITCODE -ne 0) { throw 'Context validation/view generation failed' }
 $jsonOptions = @{}
 if ((Get-Command ConvertFrom-Json).Parameters.ContainsKey('DateKind')) { $jsonOptions.DateKind = 'String' }
 $data = Get-Content -LiteralPath $dataPath -Raw -Encoding UTF8 | ConvertFrom-Json @jsonOptions
 $output = Join-Path $stage 'context-review.xlsx'
 $package = Open-ExcelPackage -Path $output -Create
 $expected = @{}
 $hyperlinks = [Collections.Generic.List[object]]::new()
 $maps = @{}
 $tabNames = @('Subjects','Sources','Context','Links')
 $overview = $package.Workbook.Worksheets.Add('Overview')
 $overview.View.ShowGridLines = $false
 $overview.Cells[2,1].Value = 'Reference context review'
 $overview.Cells[2,1].Style.Font.Size = 14
 $overview.Cells[3,1].Value = 'Generated view. Maintain research in the CSVs; refresh replaces workbook edits.'
 $overview.Column(1).Width = 36; $overview.Column(2).Width = 18
 $overview.Column(3).Width = 3; $overview.Column(4).Width = 105
 $overview.Cells[5,1].Value = 'Measure'; $overview.Cells[5,2].Value = 'Count'
 $overviewRows = @()
 $metricRow = 6
 foreach ($metric in $data.metrics.PSObject.Properties) {
  $overview.Cells[$metricRow,1].Value = $metric.Name
  $overview.Cells[$metricRow,2].Value = [int]$metric.Value
  $overviewRows += ,@($metric.Name,[int]$metric.Value)
  $overview.Row($metricRow).Height = 24
  $metricRow++
 }
 $null = $overview.Tables.Add($overview.Cells[5,1,($metricRow-1),2],'ContextOverview')
 $overview.Tables[0].TableStyle = [OfficeOpenXml.Table.TableStyles]::Medium2
 $overview.Cells[5,4].Value = 'Reading the pilot'
 $overview.Cells[6,4].Value = 'Source checked means compared with a saved website capture. Primary corroboration is a separate, scoped evidence assessment.'
 $overview.Cells[8,4].Value = 'Missile naming remains a recheck. The two-jump Horus statement is a draft. Website agreement does not establish independent evidence.'
 $overview.Cells[10,4].Value = 'Five linked manual images are NOT_LOCAL after verified Episode 4 RAR cleanup. Restore originals only when inspection is needed.'
 $overview.Cells[12,4].Value = 'Image links provide context, not verified web/local timing. The pilot does not change the accepted ship layout or expand the slice.'
 foreach ($r in @(6,8,10,12)) { $overview.Cells[$r,4].Style.WrapText = $true; $overview.Row($r).Height = 42 }
 $overview.Cells[($metricRow+2),1].Value = 'Open context records'
 $overview.Cells[($metricRow+2),1].Hyperlink = [OfficeOpenXml.ExcelHyperLink]::new("'Context'!A5",'Open context records')

 foreach ($tab in $tabNames) {
  $rows = @($data.sheets.$tab)
  if ($rows.Count -eq 0) { throw "No data for expected pilot tab $tab" }
  $columns = @($rows[0].PSObject.Properties.Name)
  $leading = switch ($tab) {
   'Subjects' {@('subject_id','display_name','subject_type','identity_status','aliases','identification_cues','notes')}
   'Sources' {@('source_id','title','site','parse_status','canonical_url','version_url','notes')}
   'Context' {@('context_id','summary','about_subjects','review_status','evidence_status','continuity','source_title','source_url')}
   'Links' {@('link_id','context_id','relation','target_type','target_id','target_label','notes','target_url','media_availability')}
  }
  $columns = @($leading) + @($columns | Where-Object {$_ -notin $leading})
  $expected[$tab] = @{Rows=$rows;Columns=$columns}
  $maps[$tab] = @{}
  $sheet = $package.Workbook.Worksheets.Add($tab)
  $sheet.View.ShowGridLines = $false
  $sheet.View.FreezePanes(6,3)
  $sheet.Cells[2,1].Value = $tab
  $sheet.Cells[2,1].Style.Font.Size = 14
  $sheet.Cells[3,1].Value = if ($tab -eq 'Context') {'Filter review and evidence states separately. Source links refer to the captured article/version.'} else {'Generated projection of maintained CSV records and validated relationships.'}
  for ($c=0;$c -lt $columns.Count;$c++) {
   $field = $columns[$c]
   $sheet.Cells[5,($c+1)].Value = $field
   $width = switch -Regex ($field) {
    '^summary$' {76;break}
    '^uncertainties$|^notes$|^parse_warnings$|^revisit_reason$' {68;break}
    '^title$|^source_title$|^section_heading$|^target_label$|^display_name$|^about_subjects$' {44;break}
    '_url$|^canonical_url$|^version_url$|^attribution_url$' {55;break}
    'sha256$' {68;break}
    '_utc$' {34;break}
    '^aliases$|^identification_cues$|^document_key$|^version_key$' {48;break}
    default {25}
   }
   $sheet.Column($c+1).Width = $width
   for ($i=0;$i -lt $rows.Count;$i++) {
    $value = $rows[$i].$field
    if ($value -is [datetime]) { throw 'JSON timestamps must remain strings; run with PowerShell 7.5 or newer.' }
    $cell = $sheet.Cells[($i+6),($c+1)]
    if ($value -is [int] -or $value -is [long] -or $value -is [double]) {
     $cell.Value = $value; $cell.Style.Numberformat.Format = '0'
    } elseif ([string]$value -ne '') {
     $cell.Value = [string]$value; $cell.Style.Numberformat.Format = '@'
    }
    $cell.Style.WrapText = $true
   }
  }
  $null = $sheet.Tables.Add($sheet.Cells[5,1,($rows.Count+5),$columns.Count],('Context'+$tab))
  $sheet.Tables[0].TableStyle = [OfficeOpenXml.Table.TableStyles]::Medium2
  $sheet.Row(5).Height = 30
  $sheet.Cells[5,1,5,$columns.Count].Style.WrapText = $true
  for ($i=0;$i -lt $rows.Count;$i++) {
   $rowNumber = $i+6
   $maps[$tab][[string]$rows[$i].($columns[0])] = $rowNumber
   $lineCount = 1
   for ($c=0;$c -lt $columns.Count;$c++) {
    $value = [string]$rows[$i].($columns[$c])
    $lineCount = [Math]::Max($lineCount,[Math]::Ceiling($value.Length/($sheet.Column($c+1).Width*0.82)))
   }
   $sheet.Row($rowNumber).Height = [Math]::Max(36,$lineCount*14+10)
  }
  foreach ($field in @('review_status','continuity','parse_status','media_availability')) {
   $c = [array]::IndexOf($columns,$field)+1
   if ($c -gt 0) {
    foreach ($warning in @('NEEDS_RECHECK','DRAFT','UNKNOWN','PARTIAL','NOT_LOCAL')) {
     $rule = $sheet.ConditionalFormatting.AddEqual($sheet.Cells[6,$c,($rows.Count+5),$c])
     $rule.Formula = '"'+$warning+'"'
     $rule.Style.Fill.BackgroundColor.Color = [Drawing.Color]::FromArgb(255,242,204)
     $rule.Style.Font.Color.Color = [Drawing.Color]::FromArgb(128,76,0)
    }
   }
  }
 }

 foreach ($tab in $tabNames) {
  $sheet=$package.Workbook.Worksheets[$tab]; $columns=$expected[$tab].Columns; $rows=$expected[$tab].Rows
  for ($i=0;$i -lt $rows.Count;$i++) {
   for ($c=0;$c -lt $columns.Count;$c++) {
    $field=$columns[$c]; $value=[string]$rows[$i].$field
    $target = $null; $reference = $null
    if ($value -and $field -match '_url$') { $target=$value }
    elseif ($value -and $field -eq 'source_id' -and $tab -eq 'Context') { $reference="'Sources'!A$($maps['Sources'][$value])" }
    elseif ($value -and $field -eq 'context_id' -and $tab -eq 'Links') { $reference="'Context'!A$($maps['Context'][$value])" }
    elseif ($value -and $field -eq 'target_id' -and $tab -eq 'Links') {
     if ($rows[$i].target_type -eq 'SUBJECT') { $reference="'Subjects'!A$($maps['Subjects'][$value])" }
     elseif ($rows[$i].target_type -eq 'CONTEXT') { $reference="'Context'!A$($maps['Context'][$value])" }
    }
    if ($target -or $reference) {
     if ($reference -and $reference -notmatch "!A[0-9]+$") { throw "Unresolved internal link: $tab / $value" }
     $cell=$sheet.Cells[($i+6),($c+1)]
     if ($target) { $cell.Hyperlink=[uri]$target } else { $cell.Hyperlink=[OfficeOpenXml.ExcelHyperLink]::new($reference,$value) }
     $cell.Style.Font.Color.SetColor([Drawing.Color]::FromArgb(29,78,216))
     $hyperlinks.Add(@{Tab=$tab;Row=$i+6;Column=$c+1;Target=$target;Reference=$reference})
    }
   }
  }
 }
 foreach ($sheet in $package.Workbook.Worksheets) {
  $sheet.Cells[$sheet.Dimension.Address].Style.Font.Name = 'Arial'
  $sheet.Cells[$sheet.Dimension.Address].Style.Font.Size = 10
  $sheet.Cells[$sheet.Dimension.Address].Style.VerticalAlignment = [OfficeOpenXml.Style.ExcelVerticalAlignment]::Top
  $sheet.Cells[2,1].Style.Font.Size=14
 }
 $package.Workbook.Worksheets.MoveToStart('Overview')
 $package.Save(); $package.Dispose(); $package=$null

 $check = Open-ExcelPackage -Path $output
 if ($check.Workbook.Worksheets.Count -ne 5) {throw 'Expected five sheets'}
 $verified=0
 foreach ($tab in $tabNames) {
  $sheet=$check.Workbook.Worksheets[$tab]; $rows=$expected[$tab].Rows; $columns=$expected[$tab].Columns
  if ($sheet.Dimension.End.Row -ne $rows.Count+5 -or $sheet.Tables.Count -ne 1 -or $sheet.View.Panes.Count -eq 0) {throw "Missing table/rows/panes: $tab"}
  for ($c=0;$c -lt $columns.Count;$c++) {
   if ([string]$sheet.Cells[5,($c+1)].Value -cne $columns[$c]) {throw "Header mismatch: $tab"}
   for ($i=0;$i -lt $rows.Count;$i++) {
    $cell=$sheet.Cells[($i+6),($c+1)]
    if ([string]$cell.Value -cne [string]$rows[$i].($columns[$c]) -or $cell.Formula) {throw "Value/formula mismatch: $tab / $i / $($columns[$c])"}
    $verified++
   }
  }
 }
 foreach ($link in $hyperlinks) {
  $cell=$check.Workbook.Worksheets[$link.Tab].Cells[$link.Row,$link.Column]
  if ($link.Target -and $cell.Hyperlink.AbsoluteUri -cne ([uri]$link.Target).AbsoluteUri) {throw 'External link mismatch'}
  if ($link.Reference -and $cell.Hyperlink.ReferenceAddress -cne $link.Reference) {throw 'Internal link mismatch'}
 }
 for ($i=0;$i -lt $overviewRows.Count;$i++) {
  if ([string]$check.Workbook.Worksheets['Overview'].Cells[($i+6),1].Value -cne $overviewRows[$i][0] -or
      [int]$check.Workbook.Worksheets['Overview'].Cells[($i+6),2].Value -ne $overviewRows[$i][1]) {throw 'Overview metric mismatch'}
 }
 $check.Dispose(); $check=$null
 foreach ($item in $data.input_hashes.PSObject.Properties) {
  if ((Get-FileHash -LiteralPath (Join-Path $index ($item.Name+'.csv'))).Hash.ToLowerInvariant() -cne $item.Value) {throw 'Research CSV changed during generation'}
 }
 foreach ($item in $data.image_index_hashes.PSObject.Properties) {
  if ((Get-FileHash -LiteralPath (Join-Path $repo ('reference/indexes/animehistory/'+$item.Name))).Hash.ToLowerInvariant() -cne $item.Value) {throw 'Image index changed during generation'}
 }
 Move-Item -LiteralPath $output -Destination $destination -Force
 [pscustomobject]@{Output=$destination;Sheets=5;VerifiedCells=$verified;VerifiedLinks=$hyperlinks.Count;Metrics=$data.metrics;AuthoredDataUnchanged=$true} | ConvertTo-Json -Depth 4
} finally {
 if ($package) {$package.Dispose()}
 if ($check) {$check.Dispose()}
 Assert-OwnedStage
 if (Test-Path -LiteralPath $stage) {Remove-Item -LiteralPath $stage -Recurse -Force}
}
