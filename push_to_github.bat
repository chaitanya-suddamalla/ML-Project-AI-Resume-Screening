@echo off
echo ===================================================
echo   AUTOMATED GITHUB REPOSITORY CREATOR AND PUSHER
echo ===================================================
echo.
echo Step 1: Opening GitHub browser login...
"C:\Program Files\GitHub CLI\gh.exe" auth login --web --git-protocol https --hostname github.com
echo.
echo Step 2: Creating GitHub Repository 'ML-Project-AI-Resume-Screening' and Pushing Code...
"C:\Program Files\GitHub CLI\gh.exe" repo create ML-Project-AI-Resume-Screening --public --source=. --remote=origin --push
echo.
echo ===================================================
echo SUCCESS! Your project is pushed to GitHub!
echo Repository: https://github.com/geethikameda7125/ML-Project-AI-Resume-Screening
echo ===================================================
pause
