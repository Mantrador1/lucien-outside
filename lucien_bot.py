import telebot
import subprocess

# Token
TOKEN = os.environ.get("BOT_TOKEN")
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "🔓 Lucien Core online. Send /run <command> or /code <python>")

@bot.message_handler(func=lambda message: True)
def handle_all(message):
    user_input = message.text.strip()

    if user_input.startswith("/run "):
        command = user_input[5:]
        try:
            result = subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT, text=True, timeout=10)
        except subprocess.CalledProcessError as e:
            result = f"[❌ Error]\n{e.output}"
        except Exception as e:
            result = f"[⚠️ Exception] {e}"
        bot.reply_to(message, f"[🖥 Output]\n{result}")

    elif user_input.startswith("/code "):
        code = user_input[6:]
        try:
            exec_locals = {}
            exec(code, {}, exec_locals)
            result = exec_locals.get("result", "[✅ Executed]")
        except Exception as e:
            result = f"[⚠️ Exception] {e}"
        bot.reply_to(message, str(result))

    else:
        bot.reply_to(message, f"🟢 Lucien εδώ. Στείλε `/run` για command ή `/code` για Python.")

print("✅ Lucien Bot with Executor running...")
bot.polling()
