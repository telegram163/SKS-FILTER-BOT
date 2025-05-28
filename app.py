import telebot

bot = telebot.TeleBot("8175759277:AAGbytswH75oua-JdMkbVLkW2paLDEU2dMY")  # Replace with your token

@bot.message_handler(func=lambda _: True)
def reply(message):
    bot.reply_to(message, "I'm alive 24/7! 🚀")

bot.polling(none_stop=True)  # Keeps the bot running
