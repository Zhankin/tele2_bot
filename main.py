import config
import telebot

bot = telebot.TeleBot(config.token)
token = '533314669:AAF_L5ViVpyyEsdy0DKK1SshUwHUQ3bQPi8'

def start(bot, update):
    update.message.reply_text(
        "Hello!"
        "Please select menu:",
        reply_markup=markup)

    return CHOOSING

def main_menu(message):
  markup = types.ReplyKeyboardMarkup(True, False)
  button1 = types.KeyBoardButton('Info')
  button2 = types.KeyBoardButton('Forecast')
  markup.add(button1, button2)

if __name__ == '__main__':
     bot.polling(none_stop=True)
