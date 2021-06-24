import telebot
import config
from telebot import types
import http.client
import re


basictext = ''
updatetext = ''

def maindata():
    conn = http.client.HTTPSConnection("vaccovid-coronavirus-vaccine-and-treatment-tracker.p.rapidapi.com")
    headers = {
        'x-rapidapi-key': "364f309890msh9b888810f74017cp124f8fjsn00264e73f2e1",
        'x-rapidapi-host': "vaccovid-coronavirus-vaccine-and-treatment-tracker.p.rapidapi.com"
        }
    conn.request("GET", "/api/npm-covid-data/asia", headers=headers)
    res = conn.getresponse()
    data = res.read()
    data1=data.decode("utf-8")
    return data1
def getinfo(st):
    data1=maindata()
    if data1.find(st)!=-1 and st!='':
        country=re.search(st,data1)
        poccontr=country.start()
        data=data1[poccontr:]
        info=re.search('TotalCases',data)
        poc=info.start()
        res=''
        allres=''
        s1=True
        i=0
        while s1==True:
            if(data[i+poc]==':'):
                i+=1
                while True:
                    if data[i+poc]==',':
                        s1=False
                        break
                    res+=data[i+poc]
                    i+=1
                    allres=st+' total cases: '+res
            i+=1
        
    else:
        allres='incorrect data' 
    return allres
def getinfo_ppl(st):
    data1=maindata()
    if data1.find(st)!=-1 and st!='':
        country=re.search(st,data1)
        poccontr=country.start()
        data=data1[poccontr:]
        info=re.search('Population',data)
        poc=info.start()
        res=''
        allres=''
        s1=True
        i=0
        while s1==True:
            if(data[i+poc]==':'):
                i+=1
                while True:
                    if data[i+poc]==',':
                        s1=False
                        break
                    res+=data[i+poc]
                    i+=1
                    allres=st+' population: '+res
            i+=1
        
    else:
        allres='incorrect data' 
    return allres

def getinfo_tests(st):
    data1=maindata()
    if data1.find(st)!=-1 and st!='':
        country=re.search(st,data1)
        poccontr=country.start()
        data=data1[poccontr:]
        info=re.search('TotalTests',data)
        poc=info.start()
        res=''
        allres=''
        s1=True
        i=0
        while s1==True:
            if(data[i+poc]==':'):
                i+=1
                while True:
                    if data[i+poc]==',':
                        s1=False
                        break
                    res+=data[i+poc]
                    i+=1
                    allres=st+' total_tests: '+res
            i+=1
        
    else:
        allres='incorrect data' 
    return allres

def getinfo_recovery(st):
    data1=maindata()
    if data1.find(st)!=-1 and st!='':
        country=re.search(st,data1)
        poccontr=country.start()
        data=data1[poccontr:]
        info=re.search('Recovery_Proporation',data)
        poc=info.start()
        res=''
        allres=''
        s1=True
        i=0
        while s1==True:
            if(data[i+poc]==':'):
                i+=1
                while True:
                    if data[i+poc]==',':
                        s1=False
                        break
                    res+=data[i+poc]
                    i+=1
                    allres=st+' recovery_proporation: '+res
            i+=1
        
    else:
        allres='incorrect data' 
    return allres
def getinfo_fatality(st):
    data1=maindata()
    if data1.find(st)!=-1 and st!='':
        country=re.search(st,data1)
        poccontr=country.start()
        data=data1[poccontr:]
        info=re.search('Case_Fatality_Rate',data)
        poc=info.start()
        res=''
        allres=''
        s1=True
        i=0
        while s1==True:
            if(data[i+poc]==':'):
                i+=1
                while True:
                    if data[i+poc]==',':
                        s1=False
                        break
                    res+=data[i+poc]
                    i+=1
                    allres=st+' case_fatality_rate: '+res
            i+=1
        
    else:
        allres='incorrect data' 
    return allres
bot = telebot.TeleBot(config.TOKEN)

@bot.message_handler(commands=['start'])
def lala(message):
    bot.send_message(message.chat.id, getinfo('Bangladesh') + '\n' + getinfo('Maldives') + '\n' + getinfo('China') + '\n' + getinfo('S. Korea') + '\n' + getinfo('Japan'))
    bot.send_message(message.chat.id, 'To get more information write /show [country]')
    global basictext
    basictext = getinfo('Bangladesh') + '\n' + getinfo('Maldives') + '\n' + getinfo('China') + '\n' + getinfo('S. Korea') + '\n' + getinfo('Japan') + '\n'





@bot.message_handler(commands=['help'])
def lala(message):
    bot.send_message(message.chat.id, '/start - shows statistics of 5 countries\n/show [country] - shows [country] statistics\n/save - save data to text.txt')

@bot.message_handler(commands=['show'])
def lala(message):
    text = message.text
    text = text[6:]
    bot.send_message(message.chat.id, getinfo(str(text)) + '\n' + getinfo_ppl(str(text)) + '\n' + getinfo_tests(str(text)) + '\n' + getinfo_fatality(str(text)) + '\n' + getinfo_recovery(str(text)))
    global updatetext
    updatetext = getinfo(str(text)) + '\n' + getinfo_ppl(str(text)) + '\n' + getinfo_tests(str(text)) + '\n' + getinfo_fatality(str(text)) + '\n' + getinfo_recovery(str(text))
    




    
@bot.message_handler(commands=['save'])
def lala(message):
    f = open('text.txt', 'w')
    f.write(basictext)
    f.write(updatetext)
    f.close()
    file = open('text.txt', 'rb')
    bot.send_document(message.chat.id, file)
    file.close()



@bot.message_handler(content_types=['text'])
def lala(message):
    bot.send_message(message.chat.id, 'Unknown command\nTo find out the commands write /help')




bot.polling(none_stop=True)
