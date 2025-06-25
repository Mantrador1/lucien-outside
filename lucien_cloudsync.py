import os
import time
import hashlib
from webdav3.client import Client

# WebDAV Config
options = {
    'webdav_hostname': "https://webdav.pcloud.com",
    'webdav_login':    "fotoniomail@gmail.com",
    'webdav_password': "LucienBot2025"
}

client = Client(options)
target_folder = "/Lucien_Uploads"
local_folder = "C:/lucien_proxy/uploads"

# Δημιουργεί φάκελο στο cloud αν δεν υπάρχει
if not client.check(target_folder):
    client.mkdir(target_folder)

def file_checksum(path):
    with open(path, 'rb') as f:
        return hashlib.md5(f.read()).hexdigest()

uploaded = {}

while True:
    try:
        for filename in os.listdir(local_folder):
            full_path = os.path.join(local_folder, filename)
            if not os.path.isfile(full_path):
                continue

            checksum = file_checksum(full_path)
            if uploaded.get(filename) == checksum:
                continue  # skip if same

            remote_path = f"{target_folder}/{filename}"
            client.upload_sync(remote_path=remote_path, local_path=full_path)
            uploaded[filename] = checksum
            print(f"✅ Synced: {filename}")

    except Exception as e:
        print(f"⚠️ Error: {str(e)}")

    time.sleep(900)  # κάθε 15 λεπτά
