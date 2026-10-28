param(
    [int]$Port = 8765,
    [string]$Python = (Join-Path $env:USERPROFILE "anaconda3\envs\context_fabric\python.exe")
)

$ErrorActionPreference = "Stop"
$ContextDir = Split-Path -Parent $MyInvocation.MyCommand.Path
$Corpus = Join-Path $ContextDir "data\bhsa\tf\2021"

if (-not (Test-Path -LiteralPath $Python)) {
    throw "Context Fabric Python environment is missing at $Python. Supply -Python with the environment's python.exe path."
}

$PythonCheck = & $Python -c "import sys; sys.exit(0 if sys.version_info >= (3, 13) else 1)" 2>&1
if ($LASTEXITCODE -ne 0) {
    throw "Context Fabric requires a working Python 3.13+ environment. Supply -Python with a suitable environment's python.exe path. Python reported: $PythonCheck"
}

if (-not (Test-Path -LiteralPath (Join-Path $Corpus "otype.tf"))) {
    throw "BHSA 2021 is not present at $Corpus. Follow README.md first."
}

$Features = @(
    "book", "chapter", "verse",
    "lex", "lex_utf8", "g_lex_utf8", "g_word_utf8", "g_cons_utf8",
    "voc_lex_utf8", "gloss",
    "sp", "pdp", "gn", "nu", "ps", "st", "vt", "vs", "ls",
    "language", "function", "typ", "domain", "kind", "rela",
    "mother", "mother_object_type", "label", "trailer_utf8", "freq_lex"
) -join " "

Write-Host "Starting local Context Fabric MCP server"
Write-Host "Corpus: $Corpus"
Write-Host "SSE endpoint: http://127.0.0.1:$Port/sse"
Write-Host "The first launch compiles a sizeable .cfm cache and can take several minutes."

# Invoke the installed entry point through this environment's Python. Windows
# console-script executables embed an absolute Python path and break after moves.
& $Python -c "from cfabric_mcp import main; main()" `
    --corpus "bhsa=$Corpus" `
    --features $Features `
    --sse $Port `
    --host 127.0.0.1 `
    --verbose

if ($LASTEXITCODE -ne 0) {
    throw "Context Fabric MCP exited with code $LASTEXITCODE."
}

