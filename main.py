import config
import telebot
import requests
from bs4 import BeautifulSoup as BS

r = requests.get('https://sinoptik.ua/погода-тюмень')
html = BS(r.content, 'html.parser')
bot = telebot.TeleBot(config.token)

for el in html.select('#content'):
    t_min = el.select('.temperature .min')[0].text
    t_max = el.select('.temperature .max')[0].text
    text = el.select('.wDescription .description')[0].text
    den = el.select('.infoTimes .clock .descr')[0].text
    prazdnik = el.select('.oDescription .rSide')[0].text
    
@bot.message_handler(commands=['pogoda', 'help'])
def main(message):
	bot.send_message(message.chat.id, "Привет, погода на сегодня:\n" +
        t_min + ', ' + t_max + '\n' + text + '\n' +
        den + ', ' '\n' + prazdnik)

        
@bot.message_handler(content_types=['text'])        
def get_text_messages(message):        
    if message.text == "Привет":
        bot.send_message(message.from_user.id, "Привет, сейчас я расскажу тебе гороскоп на сегодня.")
    elif message.text == "/help":

        bot.send_message(message.from_user.id, "Напиши Привет")



if __name__ == '__main__':
    bot.polling(none_stop=True)