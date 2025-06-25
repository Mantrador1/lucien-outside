# memory.py

# Απλή μνήμη στη RAM (χάνονται τα δεδομένα με κάθε restart)
session_memory = {}

def store_message(chat_id, text):
    if chat_id not in session_memory:
        session_memory[chat_id] = []
    session_memory[chat_id].append(text)
    if len(session_memory[chat_id]) > 20:
        session_memory[chat_id] = session_memory[chat_id][-20:]

def get_last_messages(chat_id, limit=5):
    return session_memory.get(chat_id, [])[-limit:]
