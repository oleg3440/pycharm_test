# Объявите анонимную (лямбда) функцию для определения вхождения в переданную ей строку фрагмента "plr".
# То есть, функция должна возвращать True, если такой фрагмент присутствует в строке и False - в противном случае.
string = input("Введите строку: ")

a = lambda string : "plr" in string

print(a(string))


Вариант 2
s = '123plrjkkbb'
a = 'plr'

find_in_string = lambda a,s: True if a in s else False

print(find_in_string(a, s))


Варианте 3
str = "fdgdfgplrdfgdfg"

uns = lambda str: str.count("plr") > 0
print(bool(str.count("plr")))
