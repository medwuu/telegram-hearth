# todo:
# сделать inline mode

import telebot
import time

# вставьте свой токен ниже
TOKEN = ""
bot = telebot.TeleBot(TOKEN)

hearth = "\
🤍️🤍️🤍️🤍️🤍️🤍️🤍️🤍️🤍️\n\
🤍️🤍️❤️❤️🤍️❤️❤️🤍️🤍️\n\
🤍️❤️❤️❤️❤️❤️❤️❤️🤍️\n\
🤍️❤️❤️❤️❤️❤️❤️❤️🤍️\n\
🤍️❤️❤️❤️❤️❤️❤️❤️🤍️\n\
🤍️🤍️❤️❤️❤️❤️❤️🤍️🤍️\n\
🤍️🤍️🤍️❤️❤️❤️🤍️🤍️🤍️\n\
🤍️🤍️🤍️🤍️❤️🤍️🤍️🤍️🤍️\n\
🤍️🤍️🤍️🤍️🤍️🤍️🤍️🤍️🤍️"

circle = "\
⚪⚪⚪⚪⚪⚪⚪⚪⚪\n\
⚪⚪⚪🔴🔴🔴⚪⚪⚪\n\
⚪⚪🔴🔴🔴🔴🔴⚪⚪\n\
⚪🔴🔴🔴🔴🔴🔴🔴⚪\n\
⚪🔴🔴🔴🔴🔴🔴🔴⚪\n\
⚪🔴🔴🔴🔴🔴🔴🔴⚪\n\
⚪⚪🔴🔴🔴🔴🔴⚪⚪\n\
⚪⚪⚪🔴🔴🔴⚪⚪⚪\n\
⚪⚪⚪⚪⚪⚪⚪⚪⚪"

square = "\
⬜⬜⬜⬜⬜⬜⬜⬜⬜\n\
⬜🟥🟥🟥🟥🟥🟥🟥⬜\n\
⬜🟥🟥🟥🟥🟥🟥🟥⬜\n\
⬜🟥🟥🟥🟥🟥🟥🟥⬜\n\
⬜🟥🟥🟥🟥🟥🟥🟥⬜\n\
⬜🟥🟥🟥🟥🟥🟥🟥⬜\n\
⬜🟥🟥🟥🟥🟥🟥🟥⬜\n\
⬜🟥🟥🟥🟥🟥🟥🟥⬜\n\
⬜⬜⬜⬜⬜⬜⬜⬜⬜"


@bot.message_handler(commands=['start', 'help'])
def start(message):
    bot.send_video(message.chat.id, open("media/presentation.mp4", "rb"), caption="Привет, я бот, который делает ✨магию✨. Просто отправь мне название фигуры (сердце, квадрат, или круг), а затем любой текст и увидишь магию!\nПример:\n<code>круг Привет, Мир!</code>\n<code>Сердце Люблю Вас!</code>", parse_mode='html')



@bot.message_handler(content_types=['text'])
def beautiful_hearth(message):
    # определение фигуры
    try:
        figure = {"сердце" : hearth, "круг" : circle, "квадрат" : square}[message.text.split(" ", 1)[0].lower()]
        print(message.text.lower().split(" ", 1))
    except KeyError:
        bot.send_message(message.chat.id, "Упс, что-то пошло не так. Проверьте формат сообщения!")
        return "Invalid Input"
    # установка подходящего фигуре эмодзи
    if figure == hearth:
        red, orange, yellow, blue, green, white = ["❤️", "🧡", "💛", "💙", "💚", "🤍"]
    elif figure == circle:
        red, orange, yellow, blue, green, white = ["🔴", "🟠", "🟡", "🔵", "🟢", "⚪"]
    elif figure == square:
        red, orange, yellow, blue, green, white = ["🟥", "🟧", "🟨", "🟦", "🟩", "⬜"]
    message_id = bot.send_message(message.chat.id, figure).message_id
    time.sleep(0.5)
    bot.edit_message_text(figure.replace(red, orange), message.chat.id, message_id)
    time.sleep(0.5)
    bot.edit_message_text(figure.replace(red, yellow), message.chat.id, message_id)
    time.sleep(0.5)
    bot.edit_message_text(figure.replace(red, blue), message.chat.id, message_id)
    time.sleep(0.5)
    final_figure = bot.edit_message_text(figure.replace(red, green), message.chat.id, message_id).text
    # замена надписи на фон
    counter = 1
    for is_green in final_figure:
        if is_green == green:
            bot.edit_message_text(final_figure.replace(is_green, white, counter), message.chat.id, message_id)
            counter += 1
            time.sleep(0.01)
    # постепенное исчезновение
    for cycle in range(8, 0, -1):
        string = ""
        for vert in range(cycle, 0, -1):
            for horiz in range(cycle, 0, -1):
                string += white
            string += "\n"
        bot.edit_message_text(string, message.chat.id, message_id)
        time.sleep(0.2)
    # вывод текста пользователя
    bot.edit_message_text(message.text.split(" ", 1)[1], message.chat.id, message_id)









bot.polling(non_stop=True)