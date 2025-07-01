import os
import telebot

BOT_TOKEN = os.getenv("TELEGRAM_TOKEN", "ΒΑΛΕ_ΕΔΩ_ΤΟ_TOKEN")

bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start', 'hello'])
def send_welcome(message):
    bot.reply_to(message, "Γεια σου! Είμαι ο Lucien Proxy 🤖")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, f"Έλαβα: {message.text}")

if __name__ == "__main__":
    print("Lucien Polling Bot ξεκίνησε...")
    bot.polling(none_stop=True)
