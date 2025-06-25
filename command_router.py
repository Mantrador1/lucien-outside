# command_router.py

def route_command(chat_id, command):
    if command.startswith("/start"):
        return "🚀 LucienX ενεργοποιήθηκε. Πες μου κάτι."
    
    if command.startswith("/help"):
        return "ℹ️ Διαθέσιμες εντολές: /start, /help, /whoami, /reset"
    
    if command.startswith("/whoami"):
        return f"Είσαι ο χρήστης με chat_id: {chat_id}"

    if command.startswith("/reset"):
        return "🔄 Η μνήμη μου θα καθαριστεί (όταν υλοποιηθεί)."

    return f"❓ Δεν καταλαβαίνω την εντολή: {command}"
