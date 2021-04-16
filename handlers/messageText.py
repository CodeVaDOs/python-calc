from handlers.randomImg import *


@bot.message_handler(content_types=['text'])
def message_text(message):
    text = message.text.lower()

    if message.text == 'Random image':
        send_photo_command(message)
    else:
        bot.send_message(
            chat_id=message.chat.id,
            text='Error',
            reply_markup=main_menu
        )
