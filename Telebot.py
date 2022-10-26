
import telebot


token = 'ваш токен' 

#создаем бота
bot = telebot.TeleBot(token)

#любое текстовое сообщение функции echo будет обрабатываться
@bot.message_handler(content_types=['text']) 

#функция бота
def echo(message):
	myName = 'Dima'
	if myName in message.text == 'Dima':
		bot.send_message(message.chat.id, 'Ба! Знакомые все лица!')
	else:
		bot.send_message(message.chat.id, message.text)


bot.polling(none_stop = True) 
