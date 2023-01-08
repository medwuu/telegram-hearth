import telebot
import config
import time
# from datetime import datetime

bot = telebot.TeleBot(config.TOKEN)

basic_hearth = "\
⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️\n\
⬜️⬜️🟥🟥⬜️🟥🟥⬜️⬜️\n\
⬜️🟥🟥🟥🟥🟥🟥🟥⬜️\n\
⬜️🟥🟥🟥🟥🟥🟥🟥⬜️\n\
⬜️🟥🟥🟥🟥🟥🟥🟥⬜️\n\
⬜️⬜️🟥🟥🟥🟥🟥⬜️⬜️\n\
⬜️⬜️⬜️🟥🟥🟥⬜️⬜️⬜️\n\
⬜️⬜️⬜️⬜️🟥⬜️⬜️⬜️⬜️\n\
⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️"


@bot.message_handler(content_types=['text'])
def hearth(message):
    message_id = bot.send_message(message.chat.id, basic_hearth)
    time.sleep(0.5)
    bot.edit_message_text(basic_hearth.replace("🟥", "🟧"), message.chat.id, message_id.message_id)
    time.sleep(0.5)
    bot.edit_message_text(basic_hearth.replace("🟥", "🟨"), message.chat.id, message_id.message_id)
    time.sleep(0.5)
    bot.edit_message_text(basic_hearth.replace("🟥", "🟦"), message.chat.id, message_id.message_id)
    time.sleep(0.5)
    bot.edit_message_text(basic_hearth.replace("🟥", "🟩"), message.chat.id, message_id.message_id).text
    basic_hearth1 = basic_hearth.replace("🟥", "🟩")
    counter = 1
    for i in basic_hearth1:
        if i == "🟩":
            bot.edit_message_text(basic_hearth1.replace(i, "⬜️", counter), message.chat.id, message_id.message_id)
            counter += 1
            time.sleep(0.01)
    




# todo: срез по вертикали и по горизонтали, плавное исчезновение блока. затем надпись (пользовательская)




bot.polling(non_stop=True)