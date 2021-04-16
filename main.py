import telebot
from config import TOKEN
from func import json_parse

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(content_types=['document'])
def handle_docs_photo(message):
    try:
        chat_id = message.chat.id

        file_info = bot.get_file(message.document.file_id)
        downloaded_file = bot.download_file(file_info.file_path)
        src = 'D:\\Projekts\\!Python\\python-calc\\templete' + message.document.file_name
        with open(src, 'wb') as new_file:
            new_file.write(downloaded_file)

        bot.reply_to(message, json_parse(src))
    except Exception as e:
        bot.reply_to(message, e)