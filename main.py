from telebot import TeleBot

bot = TeleBot("7554387711:AAFQBS8oK2vbvaqw6CI5K7OboC1V0cfJGcg")


@bot.message_handler(commands=["start"])
def botbot(message):
    bot.send_message(message.chat.id, "Привет! Введи /commands")


@bot.message_handler(commands=["commands"])
def bot1(message):
    bot.send_message(message.chat.id, "Список команд:")
    bot.send_message(message.chat.id, "/start")
    bot.send_message(message.chat.id, "/commands")
    bot.send_message(message.chat.id, "/whatcanabotdo")
    bot.send_message(message.chat.id, "/creator")
    bot.send_message(message.chat.id, "/bye")


@bot.message_handler(commands=["bye"])
def bot2(message):
    bot.send_message(message.chat.id, "Пока!")


@bot.message_handler(commands=["whatcanabotdo"])
def bot2(message):
    bot.send_message(message.chat.id, "Больше бот ничего не может :(")


@bot.message_handler(commands=["creator"])
def bot3(message):
    bot.send_message(message.chat.id, "Создатель этого бота:@rikitikitavi2022_2022")


bot.infinity_polling()