# ArcReel 로컬 실행 스크립트
# 시작:  powershell -ExecutionPolicy Bypass -File start-dev.ps1
# 종료:  powershell -ExecutionPolicy Bypass -File start-dev.ps1 -Stop

param([switch]$Stop)

$root = Split-Path -Parent $MyInvocation.MyCommand.Path

if ($Stop) {
    foreach ($port in 1241, 5173) {
        Get-NetTCPConnection -LocalPort $port -State Listen -ErrorAction SilentlyContinue |
            ForEach-Object { Stop-Process -Id $_.OwningProcess -Force -ErrorAction SilentlyContinue }
    }
    Write-Host "ArcReel 서버를 종료했습니다."
    exit
}

# ArcReel 보안 정책상 provider API 키(GEMINI_API_KEY 등)가 환경변수에 있으면
# 서버가 시작을 거부함. Windows 시스템 설정은 건드리지 않고 이 프로세스에서만 제거.
Remove-Item Env:GEMINI_API_KEY -ErrorAction SilentlyContinue

# 백엔드 (FastAPI, http://localhost:1241)
Start-Process powershell -ArgumentList @(
    "-NoExit", "-Command",
    "Set-Location '$root'; Remove-Item Env:GEMINI_API_KEY -ErrorAction SilentlyContinue; uv run uvicorn server.app:app --reload --reload-dir server --reload-dir lib --port 1241"
) | Out-Null

# 프론트엔드 (Vite, http://localhost:5173)
Start-Process powershell -ArgumentList @(
    "-NoExit", "-Command",
    "Set-Location '$root\frontend'; pnpm dev"
) | Out-Null

Write-Host ""
Write-Host "ArcReel 서버를 시작했습니다. 창이 두 개 뜰 거야."
Write-Host "  접속 주소 : http://localhost:5173"
Write-Host "  아이디    : admin  (비밀번호는 ArcReel\.env 의 AUTH_PASSWORD 참고)"
Write-Host "종료할 때는  powershell -ExecutionPolicy Bypass -File start-dev.ps1 -Stop"
