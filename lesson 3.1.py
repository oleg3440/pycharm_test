# Орел и решка
#
# Дана строка текста, состоящая из букв русского алфавита "О" и "Р". Буква "О" – соответствует выпадению Орла, а буква "Р" – соответствует выпадению Решки.
# Напишите программу, которая подсчитывает наибольшее количество подряд выпавших Решек.
#
# Формат входных данных
# На вход программе подается строка текста, состоящая из букв русского алфавита "О" и "Р".
#
# Формат выходных данных
# Программа должна вывести наибольшее количество подряд выпавших Решек.
#
# Примечание. Если выпавших Решек нет, то необходимо вывести число
# 0
# 0.
#
# Тестовые данные
# Sample Input 1:
# ОРРОРОРООРРРО
# Sample Output 1:
# 3
# Sample Input 2:
# ООООООРРРОРОРРРРРРР
# Sample Output 2:
# 7
# Sample Input 3:
# ООООРРРРОРОРРРРРРРРООРОРОРРРРРРРРРРРРРРРРРРРРРРРРРРРРРРР
# Sample Output 3:
# 31

s=input()
t=0
while "Р"*(t+1) in s:
    t+=1
if t!=0:
    print(t)
else:
    pr

# string1 = "ОРОРОРОРОРОРООРРРОРОРОРОРОРРОРОРОРРОРРРРРРРРРРРРРРР"
# find1 = "Р"
#
# while string1.count(find1) > 0:
#     count = len(find1)
#     find1 += "Р"
#
# print(count);
#
#
# s=input()
# t = 0
# while "Р" (t+1) in s:
#     t+=1
# if t!=0
#     print(t)
# else:
#     print(0)

text = input("Text: ")
max = 1
count = 1
for i in ragne(1, len(text)):
    if text[i] == text[i-1] and text[i] == 'Р':
        count += 1
    else:
        if count > max:
            max = count
        count = 1

if count > max:
            max = count

print(max)