"""Игра угадай число
Компьютер сам загадывает и сам угадывает число
"""

import numpy as np

def avg_predict(number: int = 1) -> int:
    """Угадываем число по алгоритму деления на 2

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    count = 0

    range_min = 0
    range_max = 101

    while True:
        count += 1
        avg_num = int((range_max + range_min) / 2)
        if number < avg_num:
            range_max = avg_num
        elif number > avg_num:
            range_min = avg_num
        else:
            break

    return count


def score_game(avg_predict) -> int:
    """За какое количство попыток в среднем за 1000 подходов угадывает наш алгоритм

    Args:
        avg_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = []
    np.random.seed()  # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000))  # загадали список чисел

    for number in random_array:
        count_ls.append(avg_predict(number))

    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за:{score} попыток")
    return score


if __name__ == "__main__":
    # RUN
    score_game(avg_predict)
