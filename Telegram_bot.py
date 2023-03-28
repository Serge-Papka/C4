import telebot

TOKEN = "6255604196:AAGpD6yipCTS3jGEPgs-fIi_RdAyLE20kjA"

bot = telebot.TeleBot(TOKEN)
@bot.message_handler(filters)
def function_name(message):
    bot.reply_to(message, "This is a message handler")
bot.polling(none_stop=True)
