import math


# Task 1
print('------------ Task 1 ------------')
def task1(a, b, op):
    if op == '*':
        return a * b
    if op == '+':
        return a + b
    if op == '-':
        return a - b
    if op == '/':
        if b != 0:
            return a / b
        return "you can't division by 0"
    return 'Unknown operation'

a, b = map(int, input('Enter your numbers (by ,): ').split(", "))
op = input('Your operation: ')
print(f'Your answer is: {task1(a, b, op)}')



# Task 2
print('------------ Task 2 ------------')
def task2(r):
    return round(math.pi * r ** 2), round(math.pi * 2 * r)

r = float(input('Your radius: '))
print(f'Your square and perimetr are: {task2(r)}')


# Task 3
print('------------ Task 3 ------------')
def t3(x, y, z):
    d1 = (x**2 + y**2 - z**2) / 2 * x * y
    return math.degrees(math.acos(d1))

def task3(x, y, z):
    d1 = t3(x, y, z)
    d2 = t3(y, z, x)
    d3 = t3(z, x, y)
    return d1, d2, d3

x = int(input('x: '))
y = int(input('y: '))
z = int(input('z: '))
print(task3(x, y, z))



# Task 4
print('------------ Task 4 ------------')
def task4(a, b):
    if a == 0:
        return abs(b)
    if b == 0:
        return abs(a)
    a, b = abs(a), abs(b)
    
    while b != 0:
        a, b = b, a % b
    
    return a

a = int(input('Enter first number: '))
b = int(input('Enter second number: '))
print(f'your NOD: {task4(a, b)}')


# Task 5
print('------------ Task 5 ------------')
def task5(n, m):
    if m == 0:
        return ("Знаменатель не может быть равен нулю")

    divisor = task4(n, m)

    p = n // divisor
    q = m // divisor

    if q < 0:
        p = -p
        q = -q
    
    return (p, q)

n = int(input('Enter first number: '))
m = int(input('Enter second number: '))
print(task5(n, m))




