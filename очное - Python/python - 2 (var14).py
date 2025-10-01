'''
# Task 1
print('-----------------------')
print('Task 1')
import math
def task1(x):
    return math.cos(2*x-1)+ math.sin(x)
x = float(input('Enter your number: '))
print(f"Here's your answer: {task1(x)}")

# Task 2
def task21(a, b):
    return a**2 - b**2
def task22(a, b):
    return a**2 + b**2
def task23(a, b):
    return a**2 * b**2
def task24(a, b):
    return a**2 / b**2

print('-----------------------')
print('Task 2')
a = float(input('Enter yor fist number: '))
b = float(input('Enter yor second number: '))

print(f"here's your summ: {task22(a, b)}, \
substraction: {task21(a, b)}, \
multiply: {task23(a, b)}, \
division: {task24(a, b)}")


# Task 3
print('-----------------------')
print('Task 3')
def task3(x):
    if x > math.pi / 2:
        return math.cos(x)
    return math.sin(x)
x = float(input('Enter your number: '))
print(f'Your answer is: {task3(x)}')
'''


# Task 4
n = int(input('Enter your number: '))
print(f'Your answer is {int(n ** 0.5)}')


# Task 5
def f(x):
    if x == 1:
        return 1
    return f(x-1) * x

x = int(input('Enter your x: '))
n = int(input('Enter your n: '))
su =  1
for i in range(1, n+1):
    su += ((x ** i) / f(i))

print(f'Yor answer is: {su}')    































