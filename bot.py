from main import bot
from handlers.randomImg import send_photo_command
from handlers.messageText import message_text

bot.add_message_handler(message_text)
bot.add_message_handler(send_photo_command)
bot.polling()
