import telebot
import wikipedia

API_TOKEN = "7070666215:AAH2Y75SVSXlb6YaOEAXE7WoYO8wFW3R6qM"
wikipedia.set_lang('uz')

bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(commands=["start"])
def send_welcome(message):
    bot.reply_to(message, "Salom sizga qanday yordam bera olamiz! \nYozing: (Hozircha faqat o'zbek tilida)")

@bot.message_handler(func=lambda message: True)
def senWiki(message):
    try:
        respond = wikipedia.summary(message.text)
        bot.send_message(message.chat.id, respond)
    except wikipedia.exceptions.PageError:
        bot.send_message(message.chat.id, "Bu maqola yo'q!")

bot.polling(none_stop=True)
