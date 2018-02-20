import config
import telebot

bot = telebot.TeleBot(config.token)
token = '110831855:AAE_GbIeVAUwk11O12vq4UeMnl20iADUtM'

@bot.message_handler(content_types=["text"])
def repeat_all_messages(message): # Название функции не играет никакой роли, в принципе
    bot.send_message(message.chat.id, message.text)

if __name__ == '__main__':
     bot.polling(none_stop=True)
