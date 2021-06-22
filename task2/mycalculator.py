#Імпорт потрібних модулів та бібліотек 
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import math
import sys
#Створення вікна
root = Tk() 
root.title("Calculator")
#Створення списку для майбутніх кнопок калькулятора
bttn_list = [
"7", "8", "9", "+", "*", 
"4", "5", "6", "-", "/",
"1", "2", "3",  "=", "Exit",
"0", "n!", ".", "±",  "C",
"tan", "ctg", "sin", "cos",
"(", ")","log","ln", "%", "bin" ]
#Створення кнопок для калькулятора
r = 1
c = 0
for i in bttn_list:
    rel = ""
    cmd=lambda x=i: calc(x)
    ttk.Button(root, text=i, command = cmd, width = 10).grid(row=r, column = c)
    c += 1
    if c > 4:
        c = 0
        r += 1
calc_entry = Entry(root, width = 33)
calc_entry.grid(row=0, column=0, columnspan=5)
#Логіка калькулятора
def calc(key):
    global memory
    if key == "=":
#Виключення ймовірності написання слів
        str1 = "-+0123456789.*/)(" 
        if calc_entry.get()[0] not in str1:
            calc_entry.insert(END, "Перший символ це не число!")
            messagebox.showerror("Помилка!", "Ви не ввели число!")
#Підрахунки
        try:
            result = eval(calc_entry.get())
            calc_entry.insert(END, "=" + str(result))
        except:
            calc_entry.insert(END, "Помилка!")
            messagebox.showerror("Помилка!", "Перевірте коректність даних")
#Очищення поля для введення інформації
    elif key == "C":
        calc_entry.delete(0, END)
#Функція для зміни мінуса на плюс
    elif key == "±":
        if "=" in calc_entry.get():
            calc_entry.delete(0, END)
        try:
            if calc_entry.get()[0] == "-":
                calc_entry.delete(0)
            else:
                calc_entry.insert(0, "-")
        except IndexError:
            pass
#Функція для виходу з програми
    elif key == "Exit":
        root.after(1,root.destroy)
#Функції для кнопок sin, cos, tan, ctg
    elif key == "sin":
        calc_entry.insert(END, "=" + str(math.sin(int(calc_entry.get()))))
    elif key == "cos":
        calc_entry.insert(END, "=" + str(math.cos(int(calc_entry.get()))))
    elif key == "tan":
        calc_entry.insert(END, "=" + str((math.sin(int(calc_entry.get()))/(math.cos(int(calc_entry.get()))))))
    elif key == "ctg":
        calc_entry.insert(END, "=" + str((math.cos(int(calc_entry.get()))/(math.sin(int(calc_entry.get()))))))
#Функції для дужок
    elif key == "(":
        calc_entry.insert(END, "(")
    elif key == ")":
        calc_entry.insert(END, ")")
#Функція для кнопки, яка відповідає за факторіал введеного числа
    elif key == "n!":
        calc_entry.insert(END, "=" + str(math.factorial(int(calc_entry.get()))))
#Функція для кнопки, яка переводить числа в двійковий код
    elif key == "bin":
        calc_entry.insert(END, "=" + bin(int(calc_entry.get())))
#Функція для кнопки ln
    elif key == "ln":
        calc_entry.insert(END, "=" + str(math.log(int(calc_entry.get()))))
#Функція для кнопки log
    elif key == "log":
        calc_entry.insert(END, "=" + str(math.log(int(calc_entry.get()))))
#Функція для кнопки %
    elif key == "%":
        calc_entry.insert(END, "=" + str(int(calc_entry.get())*(int(calc_entry.get())/100)))
#Функція, яка відповідає за очищення поля вводу при натисканні на кнопку "="
    else:
        if "=" in calc_entry.get():
            calc_entry.delete(0, END)
        calc_entry.insert(END, key)
        sys.exit
#Закриття вікна tkinker
root.mainloop()
