# Дан список, вывести отдельно буквы и цифры.
#
# a = ( "a", 'b', '2', '3' ,'c')
# b = ( 'a' , 'b' , 'c')
# c = ( '1', '2', '3')

a = ( "a", 'b', '2', '3' ,'c')
b = ( 'a' , 'b' , 'c')
c = ( '1', '2', '3')
x = a+b+c
print(x)
number_list = []
char_list = []
for i in x:
    try:
        int(i)
        number_list.append(i)
    except:
        char_list.append(i)
print(number_list)
print(char_list)



Вариант 2 только для положительных чисел
b= filter(str.isalpha, a)
c= filter(str.isdigit, a)

print(*b)
print(*c)
