from telebot import TeleBot
from config import TOKEN
from helper import firstMSG, db_conn


print('Пошла жара!!!')
#bot
bot = TeleBot(TOKEN)
print('Бот готов к работе')

print('Подключение к бд. Запуск')
db_conn()
print('Подключение к бд. Запуск прошёл успешно')


@bot.message_handler(commands=['start'])
def get_start(message):
    sti = open('static/welcome.webp', 'rb')

    msg = firstMSG(message.chat.id)
    
    bot.send_message(message.chat.id, (msg + message.from_user.first_name + message.from_user.last_name))
    bot.send_photo(message.chat.id, sti)


@bot.message_handler(commands=['add_result'])
def add_result(message):
    msgText =  'Ну давай запишем \n\nСколько раз сделал?'
    msg = bot.send_message(message.chat.id, msgText)    
    bot.register_next_step_handler(msg, set_num_approaches)


def set_num_approaches(message):
    if int(message.text) > 20:
        msgText = 'Ништяк!!! '
    else:
        msgText = 'Окей '
    
    msgText += 'А теперь количество подходов'


    msg = bot.send_message(message.chat.id, 'Я записал твои результаты на текущую дату, до следующего раза, Мужчина!')  

print('Бот запущен')

bot.polling(none_stop=True)