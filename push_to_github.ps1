# Automated GitHub Repository Creator & Pusher using GitHub CLI
Write-Host "===================================================" -ForegroundColor Cyan
Write-Host "  AUTOMATED GITHUB REPOSITORY CREATOR AND PUSHER" -ForegroundColor Cyan
Write-Host "===================================================" -ForegroundColor Cyan

Write-Host "`nStep 1: Opening GitHub browser login..." -ForegroundColor Yellow
& "C:\Program Files\GitHub CLI\gh.exe" auth login --web --git-protocol https --hostname github.com

Write-Host "`nStep 2: Creating GitHub Repository 'ML-Project-AI-Resume-Screening' and Pushing Code..." -ForegroundColor Yellow
& "C:\Program Files\GitHub CLI\gh.exe" repo create ML-Project-AI-Resume-Screening --public --source=. --remote=origin --push

Write-Host "`n===================================================" -ForegroundColor Green
Write-Host "SUCCESS! Your project is pushed to GitHub!" -ForegroundColor Green
Write-Host "Repository: https://github.com/geethikameda7125/ML-Project-AI-Resume-Screening" -ForegroundColor Green
Write-Host "===================================================" -ForegroundColor Green
