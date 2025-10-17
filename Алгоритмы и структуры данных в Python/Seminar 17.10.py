print('Task 1', '-' * 20)
'''
Получите строку, состоящую из первых двух и последних двух символов заданной строки.
Если длина строки меньше двух, то выведите соответствующее сообщение.
'''
a = input('Enter string: ')
if len(a) < 2:
    print('ERROR - len < 2')
else:
    print(a[:2] + a[-2:])


print('Task 2', '-' * 20)
'''
Получите строку из заданной, в которой все вхождения ее первого символа были изменены на 'S', кроме самого первого символа.
'''
a = input('Enter string: ')
k = a[0]
a_new = k
for i in range(1, len(a)):
    if a[i] == k:
        a_new += '$'
    else:
        a_new += a[i]
print('New array:', a_new)


print('Task 3', '-' * 20)
'''
Удалите из непустой строки каждый п-й символ, начиная с первого.
'''
n = int(input('Enter n: '))
a = input('Enter string: ')
a_new = ''
for i in range(len(a)):
    if i % n != 0:
        a_new += a[i]
print('New array:', a_new)


print('Task 4', '-' * 20)
'''
Удалите символы, которые имеют нечетные значения индексов в заданной строке.
'''
a = input('Enter string: ')
a_new = ''
for i in range(len(a)):
    if i % 2 == 0:
        a_new += a[i]
print('New array:', a_new)


print('Task 5', '-' * 20)
'''
Дана строка-предложение. Подсчитайте вхождение каждого слова в данное предложение.
'''
a = input('Enter string: ')
a = a.strip()
k = a.split(" ")
kk = []
cou = 0
for i in range(len(k)):
    if k[i] != '':
        kk.append(k[i])

p = set(kk)
p = list(p)
for i in p:
    print(f'word {i} is found {kk.count(i)} times.')


print('Task 6', '-' * 20)
'''
Переверните заданную строку в обратном порядке, если ее длина кратна четырем.
'''
a = input('Enter string: ')
if len(a) % 4 == 0:
    print(f'new a: {a[::-1]}')
else:
    print(f'old a: {a}')


print('Task 7', '-' * 20)
'''
Найти первый неповторяющийся символ в заданной строке.
'''
a = input('Enter string: ')
cou = 0
for i in range(len(a)):
    if a.count(a[i]) == 1:
        print('first unique:', a[i])
        cou += 1
        break
if cou == 0:
    print("Sorry, but you've not unique symbols.")


print('Task 8', '-' * 20)
'''
Введено четырехзначное число. Выяснить содержится ли в записи этого числа цифра 4?
'''
a = input('Enter number: ')
if '4' in a: print("HURRAY!")
else: print('plaki-plaki')


print('Task 9', '-' * 20)
'''
Из чисел А, В, С и D найти максимальное (использовать только If-else)
'''
a = int(input('a: '))
b = int(input('b: '))
c = int(input('c: '))
d = int(input('d: '))
if a >= b and a >= c and a >= d:
    print(f'max: {a}')
elif b >= a and b >= c and b >= d:
    print(f'max: {b}')
elif c >= b and c >= a and c >= d:
    print(f'max: {c}')
elif d >= b and d >= c and d >= a:
    print(f'max: {d}')

print('Task 10', '-' * 20)
'''
Выяснить сколько среди заданных чисел А, В, С и D нечетных.
'''
a = int(input('a: '))
b = int(input('b: '))
c = int(input('c: '))
d = int(input('d: '))
sp = [a, b, c, d]
cou = 0
for i in sp:
    if i % 2 != 0:
        cou += 1
print('result:', cou)


print('Task 11', '-' * 20)
'''
Пользователь вводит трехзначное число. Определить, является ли оно числом Армстронга.
Число Армстронга - натуральное число, которое равно сумме своих цифр, возведенных в степень,
равную количеству его цифр. Например число 153 является числом Армстронга (1**3+5**3+3**3=153).
'''
a = int(input('a: '))
sp = str(a)
cou = 0
for i in range(3):
    cou += int(sp[i]) ** 3
if a == cou:
    print(f"number {a} is Armstrong's number")
else:
    print(f"number {a} is NOT Armstrong's number")


print('Task 12', '-' * 20)
'''
Вводятся положительные a, b, c и d.
Определить, можно ли прямоугольник со сторонами a, b поместить внутри прямоугольника со сторонами с, d так,
чтобы каждая из сторон первого прямоугольника была параллельна или перпендикулярна каждой стороне второго прямоугольника.
'''
a = int(input('a: '))
b = int(input('b: '))
c = int(input('c: '))
d = int(input('d: '))
if (a <= c and b <= d) or (a <= d and b <= c):
    print('you can')
else:
    print("you can't")


print('Task 13', '-' * 20)
'''
Вводятся числа А, В и С. Упорядочить их по возрастанию (использовать только If-else)
'''
a = int(input('a: '))
b = int(input('b: '))
c = int(input('c: '))
if a <= b and a <= c:
    print(f'min: {a}')
    if b >= c:
        print(f'next is {b}')
        print(f'last is {c}')
    else:
        print(f'next is {c}')
        print(f'last is {b}')
elif b <= a and b <= c:
    print(f'min: {b}')
    if a <= c:
        print(f'next is {a}')
        print(f'last is {c}')
    else:
        print(f'next is {c}')
        print(f'last is {a}')
elif c <= a and c <= b:
    print(f'min: {c}')
    if a <= b:
        print(f'next is {a}')
        print(f'last is {b}')
    else:
        print(f'next is {b}')
        print(f'last is {a}')


print('Task 14', '-' * 20)
'''
Напечатать все положительные числа из диапазона от А до В (А<В) с шагом Н.
'''
a = int(input('a: '))
b = int(input('b: '))
h = int(input('h: '))
for i in range(a, b, h):
    if i >= 0:
        print(i)


print('Task 15', '-' * 20)
'''
Дано вещественное число А и целое число N (>0). Вывести все целые степени числа А от 1 до N.
'''
a = float(input('a: '))
n = int(input('n: '))
for i in range(1, n):
    print(a ** i)




