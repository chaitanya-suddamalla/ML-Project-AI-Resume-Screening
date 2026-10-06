import os
import sys
import subprocess
import urllib.request
import json

REPO_NAME = "ML-Project-AI-Resume-Screening"
GITHUB_USER = "geethikameda7125"

def push(token=None):
    if not token and len(sys.argv) > 1:
        token = sys.argv[1]
        
    if not token:
        token = input("Enter your GitHub Personal Access Token (PAT): ").strip()
        
    if not token:
        print("Error: A GitHub Personal Access Token is required to authenticate with GitHub.")
        print("Create a token in 30 seconds at: https://github.com/settings/tokens/new?scopes=repo&description=ML-Project-Push")
        return

    print(f"\n1. Authenticating with GitHub API for user '{GITHUB_USER}'...")
    req_data = json.dumps({
        "name": REPO_NAME,
        "description": "AI-Based Resume Screening and Job Matching System - B.Tech CSE Project (FastAPI, React.js, Scikit-Learn, SQLite)",
        "private": False
    }).encode("utf-8")

    req = urllib.request.Request(
        "https://api.github.com/user/repos",
        data=req_data,
        headers={
            "Content-Type": "application/json",
            "User-Agent": "Antigravity-AI-Assistant",
            "Authorization": f"token {token}"
        }
    )

    try:
        resp = urllib.request.urlopen(req)
        print(f"✅ Successfully created repository '{REPO_NAME}' on GitHub!")
    except urllib.error.HTTPError as e:
        if e.code == 422:
            print(f"ℹ️ Repository '{REPO_NAME}' already exists on your GitHub account. Proceeding with push...")
        else:
            print(f"❌ GitHub API Error ({e.code}): {e.reason}")
            try:
                err_detail = json.loads(e.read().decode('utf-8'))
                print("Detail:", err_detail.get('message', ''))
            except Exception:
                pass
            return

    remote_url = f"https://{token}@github.com/{GITHUB_USER}/{REPO_NAME}.git"
    print("\n2. Setting git remote origin...")
    subprocess.run(["git", "remote", "remove", "origin"], capture_output=True)
    subprocess.run(["git", "remote", "add", "origin", remote_url])

    print("\n3. Pushing main branch to GitHub...")
    res = subprocess.run(["git", "push", "-u", "origin", "main"], capture_output=True, text=True)
    
    if res.returncode == 0:
        print(f"\n🎉 SUCCESS! Your complete project has been pushed to GitHub:")
        print(f"👉 https://github.com/{GITHUB_USER}/{REPO_NAME}")
    else:
        print("❌ Git Push Error:")
        print(res.stderr)

if __name__ == "__main__":
    push()
