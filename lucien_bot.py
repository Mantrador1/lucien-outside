import telebot
import subprocess

# Token
TOKEN = os.environ.get("BOT_TOKEN")
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Ã°Å¸â€â€œ Lucien Core online. Send /run <command> or /code <python>")

@bot.message_handler(func=lambda message: True)
def handle_all(message):
    user_input = message.text.strip()

    if user_input.startswith("/run "):
        command = user_input[5:]
        try:
            result = subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT, text=True, timeout=10)
        except subprocess.CalledProcessError as e:
            result = f"[Ã¢ÂÅ’ Error]\n{e.output}"
        except Exception as e:
            result = f"[Ã¢Å¡Â Ã¯Â¸Â Exception] {e}"
        bot.reply_to(message, f"[Ã°Å¸â€“Â¥ Output]\n{result}")

    elif user_input.startswith("/code "):
        code = user_input[6:]
        try:
            exec_locals = {}
            exec(code, {}, exec_locals)
            result = exec_locals.get("result", "[Ã¢Å“â€¦ Executed]")
        except Exception as e:
            result = f"[Ã¢Å¡Â Ã¯Â¸Â Exception] {e}"
        bot.reply_to(message, str(result))

    else:
        bot.reply_to(message, f"Ã°Å¸Å¸Â¢ Lucien ÃŽÂµÃŽÂ´ÃÅ½. ÃŽÂ£Ãâ€žÃŽÂµÃŽÂ¯ÃŽÂ»ÃŽÂµ `/run` ÃŽÂ³ÃŽÂ¹ÃŽÂ± command ÃŽÂ® `/code` ÃŽÂ³ÃŽÂ¹ÃŽÂ± Python.")

print("Ã¢Å“â€¦ Lucien Bot with Executor running...")
bot.polling()
