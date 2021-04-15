from main import bot
import commands.randomImg

bot.add_message_handler({commands.randomImg})

bot.polling()
