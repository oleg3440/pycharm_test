Вводится слово. Переменной msg присвоить строку "палиндром", если введенное слово
является палиндромом (одинаково читается и вперед и назад), а иначе присвоить
Sample Input:
Казак
Sample Output:
палиндром
a = input()

print("палиндром" if a.lower()==a[::-1].lower() else "не палиндром")
str = input().split(" ")
d = {}
for x in str:
    key = x[0:2]
    if key not in d.keys():
        d[key] = [x]
    else:
        d[key] += [x]
print(*sorted(d.items())



# phonenum = list(map(str, "+71234567890 +71234567854 +61234576890 +52134567890 +21235777890 +21234567110 +71232267890".split(" ")))
phonenum = list(map(str, input("Введите номера через пробел: ").split(" ")))

d = {num[:2]: [] for num in phonenum}

for num in phonenum:
    d[num[:2]].append(num)

print(*sorted(d.items()))
