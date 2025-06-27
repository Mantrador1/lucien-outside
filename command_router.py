# command_router.py

from memory import get_last_messages

def route_command(chat_id, command):
    if command.startswith("/start"):
        return "🚀 LucienX ενεργοποιήθηκε. Πες μου κάτι."

    if command.startswith("/help"):
        return "ℹ️ Διαθέσιμες εντολές: /start, /help, /whoami, /recall, /reset"

    if command.startswith("/whoami"):
        return f"Είσαι ο χρήστης με chat_id: {chat_id}"

    if command.startswith("/recall"):
        messages = get_last_messages(chat_id)
        if not messages:
            return "❗ Δεν θυμάμαι τίποτα ακόμα από εσένα."
        return "🧠 Τα τελευταία σου μηνύματα:\n" + "\n".join(f"• {msg}" for msg in messages)

    if command.startswith("/reset"):
        return "🔄 Η μνήμη μου θα καθαριστεί (όταν υλοποιηθεί)."

    return f"❓ Δεν καταλαβαίνω την εντολή: {command}"
