import telebot
import time
import PIL
import io


def chb(image):
    gray = image.convert("L")
    return gray




bot = telebot.TeleBot('1207739913:AAHCT3qW-uCTgZg6ouU_eYqwS_cIXhRdbb4')


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет, я являюсь дипломной работой молодого человека, стоящего перед вами. Давайте приступим к делу :)')
    time.sleep(0.5)
    bot.send_message(message.chat.id, 'Я создан для обработки фотографий. Загрузи в меня фотографию и получишь ее черно-белый вариант')



@bot.message_handler(commands=['help'])
def helping(message):
    bot.send_message(message.chat.id, '''1.Нажми на скрепочку
2.Выбери фотографию, которую нужно преобразить
3.Отправь ее боту
                     ''')


@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text.lower().strip() == "привет":
        if message.from_user.username is None:
            bot.reply_to(message, f"Привет, {message.from_user.first_name}! Пришли мне фотографию)")
        else:
            bot.reply_to(message, f"Привет, {message.from_user.username}! Пришли мне фотографию)" )
    elif message.text.lower().strip() == "import this":
        bot.reply_to(message, '''Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!''')
        
    else:
        bot.reply_to(message, "Ты можешь использовать команду /help для помощи")



@bot.message_handler(content_types=['photo'])   
def process_photo(message):
    bot.send_message(message.chat.id, "Ваше фото:")
    file_info = bot.get_file(message.photo[-1].file_id)
    downloaded_file = bot.download_file(file_info.file_path)
    image = PIL.Image.open(io.BytesIO(downloaded_file))
    grey = chb(image)
    grey.save('1.png')
    fphoto = open('1.png', 'rb')
    bot.send_photo(message.chat.id, fphoto)

bot.polling()
