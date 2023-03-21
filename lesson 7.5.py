# Напишите программу, которая подсчитает и выведет сумму квадратов всех двузначных чисел, делящихся на 9.
# При решении задачи используйте комбинацию функций filter, map, sum.
#
# Обратите внимание: на 9 должно делиться исходное двузначное число, а не его квадрат.

print(sum(map(lambda x: x*x, filter(lambda x: not x%9, range(0,100)))))



вариант 2
l = [i for i in range(10, 100)]
l1 = list(filter(lambda x: x % 9 == 0, l))
l2 = sum(list(map(lambda x: x**2, l1)))
print(l2)