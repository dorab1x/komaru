import telebot

import time

# замените ВАШ ТОКЕН на токен вашего бота



#замените АЙДИ КАНАЛА на айди вашего канала

channel_id = '-1001947007978'

# замените komaru.gif на имя вашей гифки (komaru.gif служит примеру)

file_name = 'komaru.gif'

# отправляет гифки каждую секунду 

while True:

    try:

        with open(file_name, 'rb') as f:

            bot.send_animation(channel_id, f)

    except Exception as e:

        print(e)

    time.sleep(1)
