import os
import subprocess
import time

# === SETTINGS ===
FLY_TOKEN = "fo1_0b2cmKKV7ddaE-nfOUJud9iQqTi6OaJtSGcxva1p0uk"
APP_NAME = "lucien-outside"
REGION = "ams"  # Amsterdam
REPO_URL = "https://github.com/Mantrador1/lucien-proxy.git"
OPENROUTER_KEY = "ΒΑΛΕ_ΕΔΩ_ΤΟ_API_KEY_ΣΟΥ"

# === STEP 1: Configure environment ===
os.environ["FLY_API_TOKEN"] = FLY_TOKEN

# === STEP 2: Clone repository ===
if not os.path.exists(APP_NAME):
    subprocess.run(["git", "clone", REPO_URL, APP_NAME], check=True)
os.chdir(APP_NAME)

# === STEP 3: Create fly.toml if not exists ===
if not os.path.exists("fly.toml"):
    subprocess.run(["flyctl", "launch", "--name", APP_NAME, "--region", REGION, "--no-deploy"], check=True)

# === STEP 4: Set secrets ===
subprocess.run(["flyctl", "secrets", "set", f"OPENROUTER_API_KEY={OPENROUTER_KEY}"], check=True)

# === STEP 5: Deploy ===
subprocess.run(["flyctl", "deploy", "--force"], check=True)

# === STEP 6: Confirm ===
print(f"\n🚀 Deployment complete! Access Lucien at:\n➡️ https://{APP_NAME}.fly.dev/ask")
