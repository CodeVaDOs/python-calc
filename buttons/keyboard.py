from telebot import types

main_menu = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True, row_width=2)
button1 = types.KeyboardButton(text='Random image')
main_menu.add(button1)
