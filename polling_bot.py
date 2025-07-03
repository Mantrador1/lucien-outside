import os
import telebot

BOT_TOKEN = os.getenv("TELEGRAM_TOKEN", "????_??O_??_TOKEN")

bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start', 'hello'])
def send_welcome(message):
    bot.reply_to(message, "Ge?a s??! ??µa? ? Lucien Proxy ??")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, f"??aßa: {message.text}")

if __name__ == "__main__":
    print("Lucien Polling Bot ?e????se...")
    bot.polling(none_stop=True)