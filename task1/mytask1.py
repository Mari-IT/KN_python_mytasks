import re
reznums = []
string = input("Введіть рядок, який бажаєте опрацювати:")
#Відокремлення чисел від літер
numsarr = re.findall(r'\d+',string)
string = re.sub(r"\d+","",string,flags=re.UNICODE)
#Перетворення масиву рядків у числа
numsarr = [int(i) for i in numsarr]
print("Рядок із слів:\n", string, sep='')
print("Рядок з чисел, вибраних з початкового масиву:\n", numsarr, sep='')
#Функція, що змінює в словах рядка першу та останню літери:
def cap(string):
    string,result = string.title(),""
    for word in string.split():
        result += word[:-1]+word[-1].upper()+" "
    return result[:-1]
print("\nРядок у якому кожне слово починається та закінчується великою літерою:\n ", cap(string),sep='')
#Пошук максимального числа у масиві
print("Максимальне занчення знайдене в масиві:",max(numsarr))
max_index=numsarr.index(max(numsarr))
#Створення масиву із всіх інших чисел піднесених до степеня:
i=0
for i in range(len(numsarr)):
    if i==max_index:
        continue
    temp = numsarr[i] ** i
    reznums.append(temp)
print("Масив чисел піднесених до степеня:\n", reznums)
