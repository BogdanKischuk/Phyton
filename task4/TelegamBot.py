import http.client
import json
import telebot
from telebot import types
# Токен телеграм бота
bot = telebot.TeleBot('1846929948:AAEzd6Ehzvd4uRCMo6OAvtxBLTzG-5niqoU')
conn = http.client.HTTPSConnection("vaccovid-coronavirus-vaccine-and-treatment-tracker.p.rapidapi.com")

headers = {
    'x-rapidapi-key': "dfcc1ad973msh7b546150ccc552dp178e72jsn77e6cf1f406b",
    'x-rapidapi-host': "vaccovid-coronavirus-vaccine-and-treatment-tracker.p.rapidapi.com"
    }

# Бот реагує на команду /start
@bot.message_handler(commands=['start'])
def start(message):
    keyboard = types.ReplyKeyboardMarkup(True, False)
    keyboard.row('/file')
    keyboard.row('/search')
    bot.send_message(message.chat.id, "Hi!\nIm CovidBot\nMake your choice to continue", reply_markup=keyboard)
# Бот реагує на команду /search
@bot.message_handler(commands=['search'])
def textforsearch(message):
    # Бот просить ввести країну, яку потрібно знайти, після чого передає цю країну в наступну функцію search()
    keyboard = types.ReplyKeyboardMarkup(True, False)
    send = bot.send_message(message.chat.id, 'Input country', reply_markup=keyboard)
    bot.register_next_step_handler(send, search)
# Бот реагує на команду /file
@bot.message_handler(commands=['file'])
def file(message):
    # Бот завантажує останні данні з сайту
    import http.client
    import json
    conn.request("GET", "/api/npm-covid-data/africa", headers=headers)
    res = conn.getresponse()
    data = res.read()
    All_Info = data.decode("utf-8")
    json = json.loads(All_Info)
    # Створюємо файл для запису
    f=open('CovidStats.txt','w')
    f.write('=' * 30)
    f.write('\n')
    # Заповнення файлу інформацією
    for i in range(30):
            f.write('Country : ')
            f.write(str(json[i].get('Country')))
            f.write('\n')
            f.write('Continent : ')
            f.write(str(json[i].get('Continent')))
            f.write('\n')
            f.write('Total Cases : ')
            f.write(str(json[i].get('TotalCases')))
            f.write('\n')
            f.write('Total Deaths : ')
            f.write(str(json[i].get('TotalDeaths')))
            f.write('\n')
            f.write('Total Recovered : ')
            f.write(str(json[i].get('TotalRecovered')))
            f.write('\n')
            f.write('=' * 30)
            f.write('\n')
    f.close()
    # Відкриття файл для передачі
    f = open('CovidStats.txt', 'rb')
    bot.send_document(message.chat.id, f)
# Функція пошуку, в яку передається назва держави, яку потрібно знайти
def search(message):
    import json
    j=0 # змінна для того, щоб якщо серед всіх держав, що має бот не буде тієї, яку шукає користувач, то бот виведе мессейдж про те, що він не знайшов інформації
    conn.request("GET", "/api/npm-covid-data/africa", headers=headers)
    res = conn.getresponse()
    data = res.read()
    All_Info = data.decode("utf-8")
    json = json.loads(All_Info)
    # Перевірка, чи є введена держава в программі
    for i in range(30):
        GetCountry = json[i].get('Country')
        if message.text == GetCountry:
            # Якщо є то бот виведе всю інформацію про цю державу
            bot.send_message(message.chat.id, 'Country : ' + str(json[i].get('Country')) + '\n' +'Continent : '+str(json[i].get('Continent'))+'\n'+'Total Cases : '+str(json[i].get('TotalCases'))+'\n'+'Total Deaths : '+str(json[i].get('TotalDeaths'))+'\n'+'Total Recovered : '+str(json[i].get('TotalRecovered')))
        else : j+=1
        if j==30:
            bot.send_message(message.chat.id, 'I didnt found this country in my program')            
# Бескінечний цикл
bot.polling(none_stop=True)
