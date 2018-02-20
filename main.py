import config
import telebot

bot = telebot.TeleBot(config.token)
token = '533314669:AAF_L5ViVpyyEsdy0DKK1SshUwHUQ3bQPi8'

@bot.message_handler(content_types=["text"])
def repeat_all_messages(message):
    bot.send_message(message.chat.id, message.text)

if __name__ == '__main__':
     bot.polling(none_stop=True)
