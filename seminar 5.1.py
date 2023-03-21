# расчитать нод двух чисел(быстрый и медленный способ)

def get_prime-factors(value: int

):
multipliers_list = []
i = 2
while value != 1:
    if not value % i:
        value = value / i
        multiplierd_list.append(i)
    else:
        i += 1
return multipliers_list

numberA = int(input("Введите первое число: "))
numberA = int(input("Введите второе число: "))
result_list = []
listA = get_prime_factors(numberA)
listB = get_prime_factors(numberB)
print(listA)
print(listB)
if len(listA) > len(listB):
    for i in listA:
        if i in listB:
            result_list.append(i)
else:
    for i in listB:
        if i in listA:
            result_list.append(i)
if len(result_list) != 0:
    grosDiv = 1
    for i in result_list:
        grosDiv *= i
    print(grosDiv)
else:
    print("Error")


# Вариант 2
ef get_prime_factors(value:int):
    multipliers_list = []
    i = 2
    while value != 1:
        if not value % i:
            value = value/i
            multipliers_list.append(i)
        else: i+=1
    return multipliers_list
N = int(input('Please, enter an integer:\n'))
print(get_prime_factors(N))


Вариант 3
def PrimeFactorization(N):
    i = 2
    factor = []
    while N >= i * 2:
        if N % i == 0:
            result = PrimeFactorization(N // i)
            result.append(i)
            factor += result
            return sorted(factor)
        i += 1
    if len(factor) == 0:
        factor.append(N)
    return sorted(factor)


prime_a = PrimeFactorization(int(input("Введите a: ")))
prime_b = PrimeFactorization(int(input("Введите b: ")))

j = 0
result = 1
if len(prime_a) > len(prime_b):
    for i in range(len(prime_a)):
        if prime_a[i] == prime_b[j]:
            result *= prime_a[i]
            j += 1
else:
    for i in range(len(prime_b)):
        if prime_b[i] == prime_a[j]:
            result *= prime_b[i]
            j += 1

print(f'НОД: {result}')


Вариант 4
a=20
b=58

if a < b :
    a, b = b, a

while b!=0:
    a, b = b, a % b

print(a)


_____________________________


a=20
b=75



while a != b:
    if a > b:
        a -= b
    else:
        b -= a

print(a)
