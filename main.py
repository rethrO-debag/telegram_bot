import telebot
import config
import logic
from telebot import types

#bot
bot = telebot.TeleBot(config.TOKEN)

@bot.message_handler(commands=['start'])
def get_start(message):
    sti = open('static/welcome.webp', 'rb')

    message = logic.auth_user(message.chat.id)
    
    bot.send_message(message.chat.id, f"Добро пожаловать, {message.from_user.first_name} {message.from_user.last_name}")
    bot.send_photo(message.chat.id, sti)

'''
@bot.message_handler(commands = ['info'])
def get_user_info(message):
    markup_inline = types.InlineKeyboardMarkup()
    item_yes = types.InlineKeyboardButton(text = 'Да', callback_data = 'yes')
    item_no = types.InlineKeyboardButton(text = 'Нет', callback_data = 'no')

    markup_inline.add(item_yes, item_no)
    bot.send_message(message.chat.id, 'Желаете узнать небольшую информацию о вас?',
        reply_markup = markup_inline
    )

@bot.callback_query_handler(func = lambda call: True)
def answer(call):
    if call.data == 'yes':
        markup_reply = types.ReplyKeyboardMarkup(resize_keyboard = True)
        item_id = types.KeyboardButton('Мой ID')
        item_username = types.KeyboardButton('Мой ник')

        markup_reply.add(item_id, item_username)
        bot.send_message(call.message.chat.id, 'Нажмите на одну из кнопок',
            reply_markup = markup_reply
        )
    elif call.data == 'no':
        pass

@bot.message_handler(content_types=['text'])
def get_text(message):
    if message.text == 'Мой ID':
        bot.send_message(message.chat.id, f'Your ID: {message.from_user.id}')
    elif message.text == 'Мой ник':
        bot.send_message(message.chat.id, f'Your ID: {message.from_user.first_name} {message.from_user.last_name}')
'''

bot.polling(none_stop=True)