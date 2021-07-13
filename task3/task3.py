# Кнопка пошуку працює некоректно, не розумію  чим це пов'язано
from tkinter import messagebox
from tkinter import ttk
import http.client
import json
from tkinter import *
import tkinter as tk
root = Tk()
root.title("Work with API")
root.geometry('500x500')
root['bg']='darkgray'

conn = http.client.HTTPSConnection("vaccovid-coronavirus-vaccine-and-treatment-tracker.p.rapidapi.com")

headers = {
    'x-rapidapi-key': "dfcc1ad973msh7b546150ccc552dp178e72jsn77e6cf1f406b",
    'x-rapidapi-host': "vaccovid-coronavirus-vaccine-and-treatment-tracker.p.rapidapi.com"
    }

conn.request("GET", "/api/npm-covid-data/europe", headers=headers)

res = conn.getresponse()
data = res.read()
Info = data.decode("utf-8")

json = json.loads(Info)
n = 10
frametop=Frame(root)
framebot=Frame(root)
frametop.pack()
framebot.pack()
# Функція оновлення, видаляє все, що є в полі Текст і заповнює новою інформацією, отриманою на даний момент
def Refresh():
    import json
    TextBox.delete(1.0,END)
    conn.request("GET", "/api/npm-covid-data/africa", headers=headers)
    res = conn.getresponse()
    data = res.read()
    Info = data.decode("utf-8")
    json = json.loads(Info)
    TextBox.insert('1.0', '\n')
    TextBox.insert('1.0', '=' * 30)
    for i in range(n):
        TextBox.insert('1.0', '\n')
        TextBox.insert('1.0', list(json[i].items())[14])
        TextBox.insert('1.0', '\n')
        TextBox.insert('1.0', list(json[i].items())[12])
        TextBox.insert('1.0', '\n')
        TextBox.insert('1.0', list(json[i].items())[11])
        TextBox.insert('1.0', '\n')
        TextBox.insert('1.0', list(json[i].items())[10])
        TextBox.insert('1.0', '\n')
        TextBox.insert('1.0', list(json[i].items())[4])
        TextBox.insert('1.0', '\n')
        TextBox.insert('1.0', list(json[i].items())[3])
        TextBox.insert('1.0', '\n')
        TextBox.insert('1.0', list(json[i].items())[2])
        TextBox.insert('1.0', '\n')
        TextBox.insert('1.0', '=' * 30)
# Створення клавіші оновлення
Refreshbutton = Button(frametop, text="REFRESH",command=Refresh)
Refreshbutton['bg']='darkgray'
Refreshbutton['fg']='blue'
Refreshbutton.pack(side=LEFT)
# Пошук, Программа перевіряє, чи є така держава в json.
def Search():
    j=0
    for i in range(n):
        InputedCountry = EntryCountry.get()
        GetCountry = json[i].get('Country')
        if InputedCountry == GetCountry:
                TextBox.insert('1.0', '*' * 30)
                TextBox.insert('1.0', '\n')
                TextBox.insert('1.0', '         We found!')
                TextBox.insert('1.0', '\n')
                TextBox.insert('1.0', '*' * 30)
                TextBox.insert('1.0', '\n')
                TextBox.insert('1.0', '=' * 30)
                TextBox.insert('1.0', json[i].get('Country'))
                TextBox.insert('1.0', 'Country : ')
                TextBox.insert('1.0', '\n')
                TextBox.insert('1.0', json[i].get('Continent'))
                TextBox.insert('1.0', 'Continent : ')
                TextBox.insert('1.0', '\n')
                TextBox.insert('1.0', json[i].get('TwoLetterSymbol'))
                TextBox.insert('1.0', 'TwoLetterSymbol : ')
                TextBox.insert('1.0', '\n')
                TextBox.insert('1.0', json[i].get('TotalCases'))
                TextBox.insert('1.0', 'TotalCases : ')
                TextBox.insert('1.0', '\n')
                TextBox.insert('1.0', json[i].get('NewCases'))
                TextBox.insert('1.0', 'NewCases : ')
                TextBox.insert('1.0', '\n')
                TextBox.insert('1.0', json[i].get('TotalDeaths'))
                TextBox.insert('1.0', 'TotalDeaths : ')
                TextBox.insert('1.0', '\n')
                TextBox.insert('1.0', '\n')
                TextBox.insert('1.0', json[i].get('TotalRecovered'))
                TextBox.insert('1.0', 'TotalRecovered : ')
                TextBox.insert('1.0', '\n')           
        else : j+=1
        if j==20:
            TextBox.insert('1.0', '\n')
            TextBox.insert('1.0', '*' * 30)
            TextBox.insert('1.0', '\n')
            TextBox.insert('1.0', '          We didnt found')
            TextBox.insert('1.0', '\n')
            TextBox.insert('1.0', '*' * 30)
# Створення поля вводу
EntryCountry = Entry(frametop, width=50, borderwidth=5)
EntryCountry['bg']='darkgray'
EntryCountry['fg']='blue'
EntryCountry.pack(side=LEFT)
# Створення клавіші пошуку
Searchbutton = Button(frametop, text="SEARCH", command=Search)
Searchbutton.pack(side=LEFT)
Searchbutton['bg']='darkgray'
Searchbutton['fg']='blue'
# Створення поля тексу для інформації
TextBox = Text(framebot,width=500, height=500)
TextBox['bg']='darkgray'
TextBox['fg']='black'
TextBox.pack()
# Перший виклик функції для заповнення при запуску
Refresh()
root.mainloop()
