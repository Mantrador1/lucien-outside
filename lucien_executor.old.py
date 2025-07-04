import telebot
import sys, io, contextlib, os, time, traceback

TOKEN = os.environ.get("BOT_TOKEN")
bot = telebot.TeleBot(TOKEN)

print("Ã¢Å“â€¦ Lucien Executor v9 online and monitoring Telegram...")

def execute_python(code):
    buf = io.StringIO()
    try:
        with contextlib.redirect_stdout(buf), contextlib.redirect_stderr(buf):
            exec(code, {})
    except Exception as e:
        buf.write(f"Ã¢ÂÅ’ Error: {e}")
    return buf.getvalue()

def execute_shell(cmd):
    try:
        out = os.popen(cmd).read()
        return out or "Ã¢Å“â€¦ ÃŽÅ¸ÃŽÂ»ÃŽÂ¿ÃŽÂºÃŽÂ»ÃŽÂ·ÃÂÃÅ½ÃŽÂ¸ÃŽÂ·ÃŽÂºÃŽÂµ Ãâ€¡Ãâ€°ÃÂÃŽÂ¯Ãâ€š output."
    except Exception as e:
        return f"Ã¢ÂÅ’ Shell Error: {e}"

@bot.message_handler(commands=['start'])
def on_start(m):
    bot.reply_to(m, "Lucien Executor v9 ÃŽÂµÃŽÂ½ÃŽÂµÃÂÃŽÂ³ÃÅ’. /code ÃŽÂ® /run ÃŽÂ® /apk")

@bot.message_handler(func=lambda m: m.text and m.text.startswith("/code "))
def on_code(m):
    res = execute_python(m.text[6:])
    bot.reply_to(m, f"Ã°Å¸â€œÂ¤ Python:
{res[:4000]}")

@bot.message_handler(func=lambda m: m.text and m.text.startswith("/run "))
def on_run(m):
    res = execute_shell(m.text[5:])
    bot.reply_to(m, f"Ã°Å¸â€™Â» Shell:
{res[:4000]}")

@bot.message_handler(func=lambda m: m.text and m.text.startswith("/apk"))
def on_apk(m):
    bot.reply_to(m, "Ã°Å¸â€œÂ¦ APK module ÃŽÂµÃŽÂ½ÃŽÂµÃÂÃŽÂ³ÃÅ’. ÃŽÂ£ÃÂÃŽÂ½Ãâ€žÃŽÂ¿ÃŽÂ¼ÃŽÂ± Kotlin & base64.")

@bot.message_handler(func=lambda m: True)
def on_fallback(m):
    bot.reply_to(m, "Ã¢Ââ€œ ÃŽÂ§ÃÂÃŽÂ·ÃÆ’ÃŽÂ¹ÃŽÂ¼ÃŽÂ¿Ãâ‚¬ÃŽÂ¿ÃŽÂ¯ÃŽÂ·ÃÆ’ÃŽÂµ /code, /run ÃŽÂ® /apk")

def run():
    while True:
        try:
            bot.polling(none_stop=True)
        except:
            traceback.print_exc()
            time.sleep(5)

if __name__ == "__main__":
    run()
