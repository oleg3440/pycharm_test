# Напишите программу, которая принимает на вход координаты двух точек и
# находит расстояние между ними в 2D пространстве.
# Пример:
# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21

A1, A2 = int(input()), int(input())
B1, B2 = int(input()), int(input())
C = ((A1-B1)**2+(A2-B2)**2)**(0.5)
C = int(C*100)
C = float(C/100)
print(C)

