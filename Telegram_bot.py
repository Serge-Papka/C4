import telebot
import json

TOKEN = "6255604196:AAGpD6yipCTS3jGEPgs-fIi_RdAyLE20kjA"

bot = telebot.TeleBot(TOKEN)


# @bot.message_handler(content_types=['text'])
# def function_name(message):
#     str_ = bot.reply_to(message, "This is a message handler2")
#     print(str_)
#     print (type(str_))


# @bot.message_handler(content_types=['voice', ])
# def function_name(message):
#     bot.reply_to(message, "This is a voice")
#     a=bot.reply_to(message, "This is a voice222")
#     print (a)

# # Обрабатываются все сообщения, содержащие команды '/start' or '/help'.
# @bot.message_handler(commands=['start', 'help'])
# def handle_start_help(message):
#     pass


# # Обрабатывается все документы и аудиозаписи
# @bot.message_handler(content_types=['document', 'audio'])
# def handle_docs_audio(message):
#     pass

# """Допишите обработчик так, чтобы он из сообщения брал username и выдавал приветственное сообщение с привязкой к пользователю."""
# @bot.message_handler(commands=['start', 'help' , '123'])
# def send_welcome(message:telebot.types.Message):
#     bot.reply_to(message, f"Welcome2, {message.chat.username}")
#     bot.send_message(message.chat.id, f"Welcome, {message.chat.username}")
#     # print(message.chat.username)

# Напишите обработчик, который на сообщения с фотографией будет отвечать сообщением «Nice meme XDD». Бот должен отвечать
# не отдельным сообщением, а с привязкой к картинке.

@bot.message_handler(content_types=['photo', ])
def say_lmao(message: telebot.types.Message):
    bot.reply_to(message, 'Nice meme XDD')


bot.polling(none_stop=True)




