from random import randint
array = [randint(-100,100) for i in range(30)]
print(array)
num = array[0]
pos = 0
for i in range(1, len(array)):
 if array[i] > num:
  num = array[i]
  pos = i
print("Max element of this array is:", num, "\nIt`s position in it is:", pos)
print("The negative numbers forming this pair:")
for i in range(len(array)-1):
    print(array[i],array[i+1])if array[i]<0 and array[i+1]<0 else None
