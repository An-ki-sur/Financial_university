import math


def task1(a, x):
    return (a/(x**2 + 1)) - math.cos(2*x-1)


print('Task 1 ^^^^^^^^^^^^^^^^^')
a = int(input('Enter a: '))
x = int(input('Enter x: '))
print(f"Here's the result: {task1(a, x)}")


def task2(x):
    return (x - 2 * math.sin(x)) / abs(8*x - 5*math.atan(3*x+1))


print('Task 2 ^^^^^^^^^^^^^^^^^')
x = int(input('Enter x: '))
print(f"Here's the result: {task2(x)}")


print('Task 3 ^^^^^^^^^^^^^^^^^')
r1 = int(input('Enter r1: '))
r2 = int(input('Enter r2: '))
print(f"Here's the results: S1 = {math.pi * r1}, S2 = {math.pi * r2}, S3 = {abs(math.pi * r1 - math.pi * r2)}")


print('Task 4 ^^^^^^^^^^^^^^^^^')
x1, y1 = map(int, input('Enter your first pair: ').split())
x2, y2 = map(int, input().split('Enter your second pair: '))
x3, y3 = map(int, input().split('Enter your third pair: '))
a = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
b = ((x3 - x2) ** 2 + (y3 - y2) ** 2) ** 0.5
c = ((x1 - x3) ** 2 + (y1 - y3) ** 2) ** 0.5
p = (a + b + c) / 2
s = math.sqrt(p * (p - a) * (p - c) * (p - b))
print(f"Here's your answer: S = {s}, P = {p*2}")


print('Task 5 ^^^^^^^^^^^^^^^^^')
a = int(input('Enter your angle: '))
print(f"Here's your result: {(a * math.pi) / 180}")


print('Task 6 ^^^^^^^^^^^^^^^^^')
a = float(input('Enter: '))
a2 = a * a
a4 = a2 * a2
a8 = a4 * a4
a10 = a8 * a2
print('''Algorythm:
Step 1: a * a = a^2
Step 2: a^2 * a^2 = a^4  
Step 3: a^4 * a^4 = a^8
Step 4: a^8 * a^2 = a^10
''')
print(f"a^10 = {a10}")
print(f"expected result is {a ** 10}")


print('Task 7 ^^^^^^^^^^^^^^^^^')
a = input('Enter your three-digit number: ')
print(f"Your first number is {a[0]}{a[2]}. Your second numder is {a[1:3]}")


print('Task 8 ^^^^^^^^^^^^^^^^^')
a = float(input('How money do you have: '))
print(f"You have {int(a)} dollars and {round((a - int(a)) * 100)} cents")


print('Task 9 ^^^^^^^^^^^^^^^^^')
a = input('Your phrase: ')
a = a.strip()
k = a.split(" ")
cou = 0
for i in range(len(k)):
    if k[i] != '':
        cou += 1
print(f"You've {cou} words in your phrase")


print('Task 10 ^^^^^^^^^^^^^^^^')
a = input('Your phrase: ')
a = a.strip().lower()
k = a.split(" ")
kk = []
cou = 0
for i in range(len(k)):
    if k[i] != '':
        kk.append(k[i])
for i in kk:
    if i[0] == i[-1]:
        cou += 1
print(f"You've {cou} words in your phrase that start and end with the same letter")










