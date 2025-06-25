# memory.py

# Î‘Ï€Î»Î® Î¼Î½Î®Î¼Î· ÏƒÏ„Î· RAM (Ï‡Î¬Î½Î¿Î½Ï„Î±Î¹ Ï„Î± Î´ÎµÎ´Î¿Î¼Î­Î½Î± Î¼Îµ ÎºÎ¬Î¸Îµ restart)
session_memory = {}

def store_message(chat_id, text):
    if chat_id not in session_memory:
        session_memory[chat_id] = []
    session_memory[chat_id].append(text)
    if len(session_memory[chat_id]) > 20:
        session_memory[chat_id] = session_memory[chat_id][-20:]

def get_last_messages(chat_id, limit=5):
    return session_memory.get(chat_id, [])[-limit:]
