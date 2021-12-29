#Telegram bot using the machine learning model we trained earlier
from model import Model
import telebot

API_KEY = "5045310707:AAFIMIDwth0Xc3B2y1TpC7TId1lp6CSWFxc"
bot = telebot.TeleBot(API_KEY)
myModel = Model()

@bot.message_handler(commands = ['Start'])
def welcome(pm):
    sent_msg = bot.send_message(pm.chat.id, "Welcome to the Fake News Classifier Bot. Please paste your news text.")
    bot.register_next_step_handler(sent_msg, text_handler) #Next message will call the name_handler function

def text_handler(pm):
    user_news = [pm.text]
    print(user_news)
    prediction = "REAL" if myModel.predict(user_news) == "REAL" else "FAKE"
    sent_msg = bot.send_message(pm.chat.id, f"This model predicts the user pasted {prediction} news")
    disclaimer_msg = bot.send_message(pm.chat.id, "DISCLAIMER: This model is built for learning purposes only and it's prediction may not be entirely accurate")


bot.polling()
