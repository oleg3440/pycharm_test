#Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

text = input("Введите текст через пробел:\n")
print(f"Исходный текст: {text}")
text2 = "абв"
lst = [i for i in text.split() if text2 not in i]
print(f'Результат: {" ".join(lst)}')

2 вариант
string = list(map(str, input("Введите строку: ").split()))

print(*[x for x in string if "абв" not in x])

3 вариант

def del_some_words(my_text):
    my_text = list(filter(lambda x: 'абв' not in x, my_text.split()))
    return " ".join(my_text)

my_text = del_some_words(my_text)
print(my_text)