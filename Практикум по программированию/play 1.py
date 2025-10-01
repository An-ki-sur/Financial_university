# Быки и коровы
'''
1.	Реализовать программу, с которой можно играть в логическую игру «Быки и коровы» (правила).
Программа загадывает число, пользователь вводит очередной вариант отгадываемого числа,
программа возвращает количество быков и коров и в случае выигрыша игрока сообщает о победе и завершается.
Сама программа НЕ ходит, т.е. не пытается отгадать число, загаданное игроком.
Взаимодействие с программой производится через консоль,
при запросе данных от пользователя программа сообщает,
что ожидает от пользователя и проверяет корректность ввода
'''

import random


def check_guess(secret, guess):
    bulls = 0
    cows = 0

    for i in range(4):  # Проверяем быков (правильные цифры на правильных позициях)
        if secret[i] == guess[i]:
            bulls += 1

    for i in guess:  # Проверяем коров (правильные цифры на неправильных позициях)
        if i in secret and i != secret[guess.index(i)]:  # если знак в загаданном числе и индекс не совпадает
            cows += 1

    return bulls, cows


def secrett():  # задаем рандомно наше число для игры
    secret = ''
    a = random.randint(0, 9)
    b = random.randint(0, 9)
    c = random.randint(0, 9)
    d = random.randint(0, 9)
    sec = str(a) + str(b) + str(c) + str(d)
    if len(set(sec)) == 4:  # проверяем, что у нас уникальное значение
        secret = sec
    if secret == '':  # если не нашли, то по новой
        return secrett()
    return secret


def play_game():
    secret_number = secrett()
    attempts = 0

    print('''Добро пожаловать в игру 'Быки и коровы'!
Я загадал четырехзначное число с неповторяющимися(!) цифрами.
Попробуйте угадать его!
Быки - правильные цифры на правильных позициях
Коровы - правильные цифры на неправильных позициях''')
    print("-" * 50)

    while True:
        while True:
            guess = input('Введите четырехзначное число (или "выход" для завершения): ')

            if guess.lower() == 'выход':
                print(f"Игра завершена. Загаданное число было: {secret_number}")
                return

            if not guess.isdigit() or len(guess) != 4:
                print("Ошибка! Пожалуйста, введите четырехзначное число.")
                continue

            if len(set(guess)) != 4:
                print("Ошибка! Все цифры должны быть разными.")
                continue
            break
        attempts += 1

        if guess == secret_number:
            print(f"ПОЗДРАВЛЯЮ! Вы угадали число {secret_number} за {attempts} попыток!")
            break

        bulls, cows = check_guess(secret_number, guess)
        print(f"Попытка {attempts}: {guess} -> Быки: {bulls}, Коровы: {cows}")


play_game()

