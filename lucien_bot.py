import telebot
import subprocess

# Token
TOKEN = '7573715897:AAGgNmOxIOrRywzihuF4jFYkBTU9ymvwgn0'
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "ðŸ”“ Lucien Core online. Send /run <command> or /code <python>")

@bot.message_handler(func=lambda message: True)
def handle_all(message):
    user_input = message.text.strip()

    if user_input.startswith("/run "):
        command = user_input[5:]
        try:
            result = subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT, text=True, timeout=10)
        except subprocess.CalledProcessError as e:
            result = f"[âŒ Error]\n{e.output}"
        except Exception as e:
            result = f"[âš ï¸ Exception] {e}"
        bot.reply_to(message, f"[ðŸ–¥ Output]\n{result}")

    elif user_input.startswith("/code "):
        code = user_input[6:]
        try:
            exec_locals = {}
            exec(code, {}, exec_locals)
            result = exec_locals.get("result", "[âœ… Executed]")
        except Exception as e:
            result = f"[âš ï¸ Exception] {e}"
        bot.reply_to(message, str(result))

    else:
        bot.reply_to(message, f"ðŸŸ¢ Lucien ÎµÎ´ÏŽ. Î£Ï„ÎµÎ¯Î»Îµ `/run` Î³Î¹Î± command Î® `/code` Î³Î¹Î± Python.")

print("âœ… Lucien Bot with Executor running...")
bot.polling()
