import telebot
import config
import time

bot = telebot.TeleBot(config.TOKEN)

basic_hearth = "\
🤍️🤍️🤍️🤍️🤍️🤍️🤍️🤍️🤍️\n\
🤍️🤍️❤️❤️🤍️❤️❤️🤍️🤍️\n\
🤍️❤️❤️❤️❤️❤️❤️❤️🤍️\n\
🤍️❤️❤️❤️❤️❤️❤️❤️🤍️\n\
🤍️❤️❤️❤️❤️❤️❤️❤️🤍️\n\
🤍️🤍️❤️❤️❤️❤️❤️🤍️🤍️\n\
🤍️🤍️🤍️❤️❤️❤️🤍️🤍️🤍️\n\
🤍️🤍️🤍️🤍️❤️🤍️🤍️🤍️🤍️\n\
🤍️🤍️🤍️🤍️🤍️🤍️🤍️🤍️🤍️"


@bot.message_handler(content_types=['text'])
def hearth(message):
    message_id = bot.send_message(message.chat.id, basic_hearth)
    time.sleep(0.5)
    bot.edit_message_text(basic_hearth.replace("❤️", "🧡"), message.chat.id, message_id.message_id)
    time.sleep(0.5)
    bot.edit_message_text(basic_hearth.replace("❤️", "💛"), message.chat.id, message_id.message_id)
    time.sleep(0.5)
    bot.edit_message_text(basic_hearth.replace("❤️", "💙"), message.chat.id, message_id.message_id)
    time.sleep(0.5)
    bot.edit_message_text(basic_hearth.replace("❤️", "💚"), message.chat.id, message_id.message_id).text
    basic_hearth1 = basic_hearth.replace("❤️", "💚")
    counter = 1
    for i in basic_hearth1:
        if i == "💚":
            bot.edit_message_text(basic_hearth1.replace(i, "🤍", counter), message.chat.id, message_id.message_id)
            counter += 1
            time.sleep(0.01)

    for cycle in range(8, 0, -1):
        string = ""
        for vert in range(cycle, 0, -1):
            for horiz in range(cycle, 0, -1):
                string += "🤍"
            string += "\n"
        bot.edit_message_text(string, message.chat.id, message_id.message_id)
        time.sleep(1)
    bot.edit_message_text(message.text, message.chat.id, message_id.message_id)









bot.polling(non_stop=True)