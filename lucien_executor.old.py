import telebot
import sys, io, contextlib, os, time, traceback

TOKEN = os.environ.get("BOT_TOKEN")
bot = telebot.TeleBot(TOKEN)

print("✅ Lucien Executor v9 online and monitoring Telegram...")

def execute_python(code):
    buf = io.StringIO()
    try:
        with contextlib.redirect_stdout(buf), contextlib.redirect_stderr(buf):
            exec(code, {})
    except Exception as e:
        buf.write(f"❌ Error: {e}")
    return buf.getvalue()

def execute_shell(cmd):
    try:
        out = os.popen(cmd).read()
        return out or "✅ Ολοκληρώθηκε χωρίς output."
    except Exception as e:
        return f"❌ Shell Error: {e}"

@bot.message_handler(commands=['start'])
def on_start(m):
    bot.reply_to(m, "Lucien Executor v9 ενεργό. /code ή /run ή /apk")

@bot.message_handler(func=lambda m: m.text and m.text.startswith("/code "))
def on_code(m):
    res = execute_python(m.text[6:])
    bot.reply_to(m, f"📤 Python:
{res[:4000]}")

@bot.message_handler(func=lambda m: m.text and m.text.startswith("/run "))
def on_run(m):
    res = execute_shell(m.text[5:])
    bot.reply_to(m, f"💻 Shell:
{res[:4000]}")

@bot.message_handler(func=lambda m: m.text and m.text.startswith("/apk"))
def on_apk(m):
    bot.reply_to(m, "📦 APK module ενεργό. Σύντομα Kotlin & base64.")

@bot.message_handler(func=lambda m: True)
def on_fallback(m):
    bot.reply_to(m, "❓ Χρησιμοποίησε /code, /run ή /apk")

def run():
    while True:
        try:
            bot.polling(none_stop=True)
        except:
            traceback.print_exc()
            time.sleep(5)

if __name__ == "__main__":
    run()
