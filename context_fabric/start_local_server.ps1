param(
    [int]$Port = 8765
)

$ErrorActionPreference = "Stop"
$ContextDir = Split-Path -Parent $MyInvocation.MyCommand.Path
$RepoRoot = Split-Path -Parent $ContextDir
$Server = Join-Path $RepoRoot ".context-fabric-venv\Scripts\cfabric-mcp.exe"
$Corpus = Join-Path $ContextDir "data\bhsa\tf\2021"

if (-not (Test-Path -LiteralPath $Server)) {
    throw "Context Fabric MCP is not installed at $Server. Follow README.md first."
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

& $Server `
    --corpus "bhsa=$Corpus" `
    --features $Features `
    --sse $Port `
    --host 127.0.0.1 `
    --verbose

