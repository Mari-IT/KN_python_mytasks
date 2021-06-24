import http.client
from tkinter import *
import re

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

def update():
    line1=Label(root,text=getinfo('Bangladesh'), width=40,anchor=W)
    line1.place(x=5,y=5)
    line2=Label(root,text=getinfo('Maldives'), width=40,anchor=W)
    line2.place(x=5,y=25)
    line3=Label(root,text=getinfo('China'), width=40,anchor=W)
    line3.place(x=5,y=45)
    line4=Label(root,text=getinfo('S. Korea'), width=40,anchor=W)
    line4.place(x=5,y=65)
    line5=Label(root,text=getinfo('Japan'), width=40,anchor=W)
    line5.place(x=5,y=85)
    line6=Label(root,text=getinfo(str(countryentr.get())), width=40,anchor=W)
    line6.place(x=5,y=125)
    line6=Label(root,text=getinfo_ppl(str(countryentr.get())), width=40,anchor=W)
    line6.place(x=5,y=145)
    line6=Label(root,text=getinfo_tests(str(countryentr.get())), width=40,anchor=W)
    line6.place(x=5,y=165)
    line6=Label(root,text=getinfo_fatality(str(countryentr.get())), width=40,anchor=W)
    line6.place(x=5,y=185)
    line6=Label(root,text=getinfo_recovery(str(countryentr.get())), width=40,anchor=W)
    line6.place(x=5,y=205)
root=Tk()
root.title('Maria`s covid_info_tracker')
root.geometry('500x500')
line1=Label(root,text=getinfo('Bangladesh'))
line1.place(x=5,y=5)
line2=Label(root,text=getinfo('Maldives'))
line2.place(x=5,y=25)
line3=Label(root,text=getinfo('China'))
line3.place(x=5,y=45)
line4=Label(root,text=getinfo('S. Korea'))
line4.place(x=5,y=65)
line5=Label(root,text=getinfo('Japan'))
line5.place(x=5,y=85)

countryentr=Entry()
countryentr.place(x=5,y=105)
Button(text='Update information',command= lambda: update()).place(x=350,y=5)

