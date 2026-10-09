# =============================================================================
# BLOOMBERG_MAIL — PREPARAÇÃO DO AMBIENTE LOCAL
# Projeto: BLOOMBERG_MAIL
# Repositório: carlos-andrade/BLOOMBERG_MAIL
# Fase: FASE-01 — Preparação local
# Versão: 1.0
# Data: 2026-10-09
# =============================================================================
# Cria a estrutura local e clona o repositório público, sem apagar ou
# sobrescrever ficheiros existentes. Não inicia captura RTD nem faz push.
# Executar em PowerShell com a conta Windows que utilizará o Excel/Profit.
# =============================================================================

[CmdletBinding()]
param(
    [string]$Root = 'D:\BLOOMBERG_MAIL',
    [string]$RepositoryUrl = 'https://github.com/carlos-andrade/BLOOMBERG_MAIL.git'
)

Set-StrictMode -Version Latest
$ErrorActionPreference = 'Stop'

$RepoPath = Join-Path $Root 'repo\BLOOMBERG_MAIL'
$ExpectedRemote = $RepositoryUrl.TrimEnd('/')
$GitCommand = Get-Command git -ErrorAction SilentlyContinue

if (-not $GitCommand) {
    throw 'Git não foi encontrado no PATH. Instale o Git for Windows e volte a executar este script.'
}

# Falhar de forma segura se o destino existir e não for um clone Git.
if (Test-Path -LiteralPath $RepoPath) {
    $GitMetadata = Join-Path $RepoPath '.git'
    if (-not (Test-Path -LiteralPath $GitMetadata)) {
        throw "O destino já existe mas não parece ser um clone Git: $RepoPath. Nada foi apagado. Renomeie/inspecione a pasta manualmente."
    }

    $CurrentRemote = (& git -C $RepoPath remote get-url origin 2>$null)
    if ($LASTEXITCODE -ne 0 -or -not $CurrentRemote) {
        throw "Não foi possível confirmar o remoto origin em $RepoPath. Nenhuma alteração foi feita ao repositório."
    }
    $CurrentRemote = $CurrentRemote.TrimEnd('/')
    if ($CurrentRemote -ne $ExpectedRemote -and $CurrentRemote -ne 'git@github.com:carlos-andrade/BLOOMBERG_MAIL.git') {
        throw "O remoto origin existente não corresponde ao repositório esperado: $CurrentRemote. Nada foi sobrescrito."
    }
}

# Criar apenas diretórios em falta. New-Item -Force não elimina conteúdos existentes.
$Directories = @(
    $Root,
    (Join-Path $Root 'repo'),
    (Join-Path $Root 'dados_locais\RAW'),
    (Join-Path $Root 'dados_locais\HISTORICO'),
    (Join-Path $Root 'dados_locais\NORMALIZADOS'),
    (Join-Path $Root 'dados_locais\QUARENTENA'),
    (Join-Path $Root 'dados_locais\MANIFESTOS'),
    (Join-Path $Root 'logs\CAPTURA'),
    (Join-Path $Root 'logs\VALIDACAO'),
    (Join-Path $Root 'logs\GIT'),
    (Join-Path $Root 'backups'),
    (Join-Path $Root 'configuracao_local')
)

foreach ($Directory in $Directories) {
    if (-not (Test-Path -LiteralPath $Directory)) {
        New-Item -ItemType Directory -Path $Directory | Out-Null
    }
}

# Clonar apenas se ainda não existir um clone válido.
if (-not (Test-Path -LiteralPath $RepoPath)) {
    & git clone $RepositoryUrl $RepoPath
    if ($LASTEXITCODE -ne 0) {
        throw 'git clone falhou. As pastas locais foram preservadas; corrija a ligação e volte a executar.'
    }
    Write-Host "Clone criado: $RepoPath" -ForegroundColor Green
}
else {
    Write-Host "Clone existente validado; não foi atualizado nem alterado: $RepoPath" -ForegroundColor Yellow
}

Write-Host ''
Write-Host 'Estrutura local preparada.' -ForegroundColor Green
Write-Host 'Nenhum ficheiro RTD foi aberto ou modificado.'
Write-Host 'Nenhum commit ou push foi executado.'
Write-Host 'A captura por alteração ainda NÃO está ativa.'
Write-Host ''
Write-Host 'Verificação manual do clone:'
Write-Host ('  git -C "' + $RepoPath + '" status --short --branch')
Write-Host ('  git -C "' + $RepoPath + '" remote -v')
