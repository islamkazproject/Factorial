# *6. Определить, является ли число простым.
# Напишите программу, которая на вход принимает любое не отрицательное число, а
# выводит строку «Простое» или же «Составное», в случае, если число не является
# простым.

from math import sqrt

chislo = int(input())

prime_number = True

i = 2
while i <= sqrt(chislo) and prime_number is True:
    if chislo % i == 0:
        prime_number = False
    i += 1

if prime_number:
    print("Простое число")
else:
    print("Составное")