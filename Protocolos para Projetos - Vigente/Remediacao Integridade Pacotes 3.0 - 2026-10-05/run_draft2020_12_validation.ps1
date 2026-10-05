param(
    [string]$OpeningZip,
    [string]$ContinuityZip,
    [string]$OutputDirectory = $PSScriptRoot
)
$ErrorActionPreference='Stop'
Add-Type -AssemblyName System.IO.Compression.FileSystem
if(-not $OpeningZip){$OpeningZip=Join-Path $PSScriptRoot 'PROJECT_OPENING_3.0-REMEDIATED-MANIFEST-MATCHED.zip'}
if(-not $ContinuityZip){$ContinuityZip=Join-Path $PSScriptRoot 'CONTINUITY_3.0-REMEDIATED-MANIFEST-MATCHED.zip'}
$expectedOpening='737be69e02819eff07ce68de22d1872bc0d6489e47d6ffcab87b2662fe795914'
$expectedContinuity='430d3671826a7e1887a7282cf966869c9d74cc5f7382c5b9c6767eaf09fb8e2e'
if((Get-FileHash -LiteralPath $OpeningZip -Algorithm SHA256).Hash.ToLowerInvariant() -ne $expectedOpening){throw 'STOP: Opening ZIP SHA-256 mismatch.'}
if((Get-FileHash -LiteralPath $ContinuityZip -Algorithm SHA256).Hash.ToLowerInvariant() -ne $expectedContinuity){throw 'STOP: Continuity ZIP SHA-256 mismatch.'}
$pythonBase=(py -3.13 -c "import sys; print(sys.executable)").Trim()
$guid=[guid]::NewGuid().ToString('N')
$tempRoot=Join-Path $env:TEMP ('protocol-schema-validation-'+$guid)
$venv=Join-Path $tempRoot 'validator-venv'
New-Item -ItemType Directory -Path $tempRoot | Out-Null
try{
    $openingStage=Join-Path $tempRoot 'opening'
    $continuityStage=Join-Path $tempRoot 'continuity'
    New-Item -ItemType Directory -Path $openingStage,$continuityStage | Out-Null
    [System.IO.Compression.ZipFile]::ExtractToDirectory($OpeningZip,$openingStage)
    [System.IO.Compression.ZipFile]::ExtractToDirectory($ContinuityZip,$continuityStage)
    $openingRoot=Get-ChildItem -LiteralPath $openingStage -Directory | Select-Object -First 1 -ExpandProperty FullName
    $continuityRoot=Get-ChildItem -LiteralPath $continuityStage -Directory | Select-Object -First 1 -ExpandProperty FullName
    & $pythonBase -m venv --without-pip $venv
    if($LASTEXITCODE -ne 0){throw 'Python venv creation failed.'}
    $validatorPython=Join-Path $venv 'Scripts\python.exe'
    & $pythonBase -m pip --python $validatorPython --disable-pip-version-check --quiet install -r (Join-Path $PSScriptRoot 'requirements-validator.txt')
    if($LASTEXITCODE -ne 0){throw 'Isolated validator installation failed.'}
    & $validatorPython (Join-Path $PSScriptRoot 'validate_protocol_json_schemas.py') --opening-zip $OpeningZip --continuity-zip $ContinuityZip --opening-root $openingRoot --continuity-root $continuityRoot --output-json (Join-Path $OutputDirectory 'draft2020-12-validation-evidence.json') --output-report (Join-Path $OutputDirectory 'draft2020-12-validation-report.md')
    if($LASTEXITCODE -ne 0){throw 'Draft 2020-12 validation did not PASS.'}
}
finally{
    if(Test-Path -LiteralPath $tempRoot){
        $resolved=[System.IO.Path]::GetFullPath($tempRoot)
        $allowedCandidates=@($env:TEMP,(Join-Path $env:USERPROFILE 'AppData\Local\Temp'))
        $allowedMatch=$false
        foreach($candidateRoot in $allowedCandidates){$prefix=[System.IO.Path]::GetFullPath($candidateRoot).TrimEnd('\')+'\';if($resolved.StartsWith($prefix,[System.StringComparison]::OrdinalIgnoreCase)){$allowedMatch=$true}}
        $leaf=Split-Path -Leaf $resolved
        if(-not $allowedMatch -or $leaf -notmatch '^protocol-schema-validation-[a-f0-9]{32}$'){throw 'Refusing to remove temporary path outside the task-scoped TEMP directory.'}
        Remove-Item -LiteralPath $resolved -Recurse -Force
    }
}

