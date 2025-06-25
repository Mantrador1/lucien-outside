import telebot
import sys, io, contextlib, os, time, traceback

TOKEN = '7573715897:AAGgNmOxIOrRywzihuF4jFYkBTU9ymvwgn0'
bot = telebot.TeleBot(TOKEN)

print("âœ… Lucien Executor v9 online and monitoring Telegram...")

def execute_python(code):
    buf = io.StringIO()
    try:
        with contextlib.redirect_stdout(buf), contextlib.redirect_stderr(buf):
            exec(code, {})
    except Exception as e:
        buf.write(f"âŒ Error: {e}")
    return buf.getvalue()

def execute_shell(cmd):
    try:
        out = os.popen(cmd).read()
        return out or "âœ… ÎŸÎ»Î¿ÎºÎ»Î·ÏÏŽÎ¸Î·ÎºÎµ Ï‡Ï‰ÏÎ¯Ï‚ output."
    except Exception as e:
        return f"âŒ Shell Error: {e}"

@bot.message_handler(commands=['start'])
def on_start(m):
    bot.reply_to(m, "Lucien Executor v9 ÎµÎ½ÎµÏÎ³ÏŒ. /code Î® /run Î® /apk")

@bot.message_handler(func=lambda m: m.text and m.text.startswith("/code "))
def on_code(m):
    res = execute_python(m.text[6:])
    bot.reply_to(m, f"ðŸ“¤ Python:
{res[:4000]}")

@bot.message_handler(func=lambda m: m.text and m.text.startswith("/run "))
def on_run(m):
    res = execute_shell(m.text[5:])
    bot.reply_to(m, f"ðŸ’» Shell:
{res[:4000]}")

@bot.message_handler(func=lambda m: m.text and m.text.startswith("/apk"))
def on_apk(m):
    bot.reply_to(m, "ðŸ“¦ APK module ÎµÎ½ÎµÏÎ³ÏŒ. Î£ÏÎ½Ï„Î¿Î¼Î± Kotlin & base64.")

@bot.message_handler(func=lambda m: True)
def on_fallback(m):
    bot.reply_to(m, "â“ Î§ÏÎ·ÏƒÎ¹Î¼Î¿Ï€Î¿Î¯Î·ÏƒÎµ /code, /run Î® /apk")

def run():
    while True:
        try:
            bot.polling(none_stop=True)
        except:
            traceback.print_exc()
            time.sleep(5)

if __name__ == "__main__":
    run()
