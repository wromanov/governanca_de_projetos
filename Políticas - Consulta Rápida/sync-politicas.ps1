[CmdletBinding()]
param()

$ErrorActionPreference = 'Stop'

$quickReferenceRoot = Split-Path -Parent $PSCommandPath
$repositoryRoot = Split-Path -Parent $quickReferenceRoot

$policies = @(
    [pscustomobject]@{
        PolicyId = 'PROMPT_POLICY_V1_4'
        FileName = 'Politica-Prompts-Agente-v1.4.md'
        SourceRelativePath = 'Protocolos para Projetos - Vigente\Protocolo - Inicio de Abertura de Projeto - Final\Agent-Continuity-Standard-v1.0\policies\Politica-Prompts-Agente-v1.4.md'
        MirrorRelativePath = 'Atuais\Politica-Prompts-Agente-v1.4.md'
    }
    [pscustomobject]@{
        PolicyId = 'SKILLS_POLICY_V1_0'
        FileName = 'Politica-de-Uso-de-Skills-Codex-Work-v1.0.md'
        SourceRelativePath = 'Protocolos para Projetos - Vigente\Protocolo - Inicio de Abertura de Projeto - Final\Agent-Continuity-Standard-v1.0\policies\Politica-de-Uso-de-Skills-Codex-Work-v1.0.md'
        MirrorRelativePath = 'Atuais\Politica-de-Uso-de-Skills-Codex-Work-v1.0.md'
    }
    [pscustomobject]@{
        PolicyId = 'ANALYTICAL_INDEPENDENCE_POLICY_V1'
        FileName = 'Independencia-Analitica-Agente-v1.md'
        SourceRelativePath = 'Protocolos para Projetos - Vigente\Protocolo - Inicio de Abertura de Projeto - Final\Agent-Continuity-Standard-v1.0\policies\Independencia-Analitica-Agente-v1.md'
        MirrorRelativePath = 'Atuais\Independencia-Analitica-Agente-v1.md'
    }
    [pscustomobject]@{
        PolicyId = 'PROMPT_POLICY_V1_6'
        FileName = 'Politica-Prompts-Agente-v1.6.md'
        SourceRelativePath = 'Protocolos em Atualização\GOV-07 - Prompt Policy v1.6\Politica-Prompts-Agente-v1.6.md'
        MirrorRelativePath = 'Em Atualização\Politica-Prompts-Agente-v1.6.md'
    }
    [pscustomobject]@{
        PolicyId = 'SKILLS_PLUGINS_POLICY_V1_1'
        FileName = 'Politica-de-Uso-de-Skills-e-Plugins-Codex-Work-v1.1.md'
        SourceRelativePath = 'Protocolos em Atualização\GOV-05 - Skills Policy v1.1\Politica-de-Uso-de-Skills-e-Plugins-Codex-Work-v1.1.md'
        MirrorRelativePath = 'Em Atualização\Politica-de-Uso-de-Skills-e-Plugins-Codex-Work-v1.1.md'
    }
    [pscustomobject]@{
        PolicyId = 'MULTIAGENT_POLICY_V1_7'
        FileName = 'AGENTS-Multiagente-Generico-v1.7.md'
        SourceRelativePath = 'Protocolos em Atualização\GOV-03 - Politica Mult Agentes\AGENTS-Multiagente-Generico-v1.7.md'
        MirrorRelativePath = 'Em Atualização\AGENTS-Multiagente-Generico-v1.7.md'
    }
)

$filesCopied = 0
$filesIdentical = 0
$missingSources = @()
$hashMismatches = @()

foreach ($policy in $policies) {
    if ([string]::IsNullOrWhiteSpace($policy.SourceRelativePath)) {
        $missingSources += $policy.FileName
        continue
    }

    $sourcePath = Join-Path $repositoryRoot $policy.SourceRelativePath
    $mirrorPath = Join-Path $quickReferenceRoot $policy.MirrorRelativePath

    if (-not (Test-Path -LiteralPath $sourcePath -PathType Leaf)) {
        $missingSources += $policy.FileName
        continue
    }

    $mirrorDirectory = Split-Path -Parent $mirrorPath
    New-Item -ItemType Directory -Path $mirrorDirectory -Force | Out-Null
    Copy-Item -LiteralPath $sourcePath -Destination $mirrorPath -Force
    $filesCopied++

    $sourceHash = (Get-FileHash -Algorithm SHA256 -LiteralPath $sourcePath).Hash
    $mirrorHash = (Get-FileHash -Algorithm SHA256 -LiteralPath $mirrorPath).Hash

    if ($sourceHash -ne $mirrorHash) {
        $hashMismatches += $policy.FileName
        continue
    }

    $filesIdentical++
}

if ($hashMismatches.Count -gt 0) {
    $policySyncStatus = 'FAIL'
}
elseif ($missingSources.Count -gt 0) {
    $policySyncStatus = 'PASS_WITH_MISSING_SOURCE'
}
else {
    $policySyncStatus = 'PASS'
}

Write-Output "POLICY_SYNC_STATUS = $policySyncStatus"
Write-Output "FILES_EXPECTED = $($policies.Count)"
Write-Output "FILES_COPIED = $filesCopied"
Write-Output "FILES_IDENTICAL = $filesIdentical"
Write-Output "MISSING_SOURCES = [$($missingSources -join ', ')]"
Write-Output "HASH_MISMATCHES = [$($hashMismatches -join ', ')]"
Write-Output 'UNRELATED_FILES_MODIFIED = 0'

if ($hashMismatches.Count -gt 0) {
    exit 1
}
