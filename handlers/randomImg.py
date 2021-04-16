from main import bot
from buttons.keyboard import main_menu
import random


@bot.message_handler(commands=['photo'])
def send_photo_command(message):
    random_id = random.randint(1, 100000)
    random_img_url = 'https://source.unsplash.com/random/1280x720?sig=' + str(random_id)

    bot.send_photo(
        message.chat.id,
        random_img_url,
        reply_markup=main_menu
    )
