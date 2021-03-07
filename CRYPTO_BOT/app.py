import telebot
from config import keys, TOKEN
from extensions import APIException, CryptoConverter

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def send_welcome(message: telebot.types.Message):
    if message.chat.username:
        bot.send_message(message.chat.id,
                         f'Приветствую, {message.chat.username}, наберите "/help" для получения справки')
    else:
        bot.send_message(message.chat.id,
                         f'Приветствую, {message.chat.first_name}, наберите "/help" для получения справки')


@bot.message_handler(commands=['help'])
def help_(message: telebot.types.Message):
    text = 'Для начала работы введите команду боту в следующем формате:\n<валюта из которой конвертируем> \
<валюта в которую конвертируем> <количество>"\
\nили "/values" для получения списка доступных валют'
    bot.reply_to(message, text)


@bot.message_handler(commands=['values'])
def values_(message: telebot.types.Message):
    text = 'Доступные валюты:\n'
    text += '\n'.join(keys.keys())
    bot.reply_to(message, text)


@bot.message_handler(content_types=['text'])
def convert(message: telebot.types.Message):
    values = list(map(str.upper, message.text.split(' ')))
    try:
        total = CryptoConverter.get_price(values)
    except APIException as e:
        bot.reply_to(message, f'Ошибка пользователя\n{e}')
    except Exception as e:
        bot.reply_to(message, f'Не удалось обработать команду\n{e}')
    else:
        text = f'Цена {values[2]} {values[0]} в {values[1]} = {total}{keys[values[1]]}'
        bot.send_message(message.chat.id, text)


bot.polling(none_stop=True)
