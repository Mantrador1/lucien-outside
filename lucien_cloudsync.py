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

# ÃŽâ€ÃŽÂ·ÃŽÂ¼ÃŽÂ¹ÃŽÂ¿Ãâ€¦ÃÂÃŽÂ³ÃŽÂµÃŽÂ¯ Ãâ€ ÃŽÂ¬ÃŽÂºÃŽÂµÃŽÂ»ÃŽÂ¿ ÃÆ’Ãâ€žÃŽÂ¿ cloud ÃŽÂ±ÃŽÂ½ ÃŽÂ´ÃŽÂµÃŽÂ½ Ãâ€¦Ãâ‚¬ÃŽÂ¬ÃÂÃâ€¡ÃŽÂµÃŽÂ¹
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
            print(f"Ã¢Å“â€¦ Synced: {filename}")

    except Exception as e:
        print(f"Ã¢Å¡Â Ã¯Â¸Â Error: {str(e)}")

    time.sleep(900)  # ÃŽÂºÃŽÂ¬ÃŽÂ¸ÃŽÂµ 15 ÃŽÂ»ÃŽÂµÃâ‚¬Ãâ€žÃŽÂ¬
