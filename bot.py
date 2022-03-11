import telebot
a = telebot.TeleBot("5009305175:AAEGlNBcPFI4-XQ7SAndzfWaDC5XyrSLru4")
keyboard_test = telebot.types.ReplyKeyboardMarkup(True)
keyboard_test.row("Привет", "Пока", "Удалить клавиатуру")
@a.message_handler(commands=['start'])
def startWork(message):
 tid = message.chat.id
 a.send_message(tid, "start work!",reply_markup = keyboard_test)
@a.message_handler(content_types=['text'])
def sendYourMessage(message):
 mid = message.chat.id
 if message.text == "Привет":
   a.send_message(mid, "Привет")
 elif message.text == "Удалить клавиатуру":
   a.send_message(mid, "Клавиатура удалена", reply_markup=telebot.types.ReplyKeyboardRemove())
 elif message.text =="Пока":
   a.send_message(mid, "Пока")
 else:
   a.send_message(mid, "Не понимаю тебя")
a.polling()
