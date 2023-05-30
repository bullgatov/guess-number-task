"""Игра угадай число
Компьютер сам загадывает и сам угадывает число.
Функция принимает загаданное число и возвращает число попыток
"""

import numpy as np


def random_predict(number: int = 1) -> int:
    """ Предполагаемое число - это рандомное число из диапазона от 1 до 100.
        На первой итерации проверяем предполагаемое число на равенство с загаданным числом 
        Если загаданное число не равно предполагаемому, то следующее предполагаемое число берем из уменьшеного диапазона,
        подставляя вместо левой или правой границы предполагаемое число с предыдущей итерации в зависимости от того,
        больше оно или меньше нужного.
    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    low_number = 1
    high_number = 101
    predict_number = np.random.randint(low_number, high_number) # предполагаемое число
    count = 0
    
    while number!=predict_number:
        count += 1
        if number > predict_number:
            low_number = predict_number
            predict_number = np.random.randint(low_number, high_number) # предполагаемое число
        elif number < predict_number:
            high_number = predict_number
            predict_number = np.random.randint(low_number, high_number) # предполагаемое число
        else:
            break  # выход из цикла если угадали
    return count


def score_game(random_predict) -> int:
    """За какое количство попыток в среднем за 1000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = []
    np.random.seed(1)  # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000))  # загадали список чисел

    for number in random_array:
        count_ls.append(random_predict(number))

    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за:{score} попыток")
    return score


if __name__ == "__main__":
    # RUN
    score_game(random_predict)