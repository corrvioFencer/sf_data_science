"""Игра угадай число
Компьютер сам загадывает и сам угадывает числа
"""
    
import numpy as np


def predict_number(number: int = 1) -> int:
    """Угадываем число учитывая больше или меньше заданное число.

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """     
    count = 0
    prediction = 50  # предпологаемое число - середина диапазона загадываемого
    period = 26
    
    while True:
        count += 1
        if period != 3:
            if prediction == number:
                break  # выход из цикла если угадали
            elif prediction > number:
                prediction -= period
                period //= 2
            elif prediction < number:
                prediction += period
                period //= 2
        elif period == 3:
            if prediction == number:
                break  # выход из цикла если угадали
            elif prediction > number:
                prediction -= period
                period += 1
            elif prediction < number:
                prediction += period
                period -= 1
            
    return count


def score_game(predict_number) -> int:
    """За какое количство попыток в среднем за 1000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = []
    #np.random.seed(1)  # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000))  # загадали список чисел

    for number in random_array:
        count_ls.append(predict_number(number))

    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за:{score} попыток")
    return score


if __name__ == "__main__":
    # RUN
    score_game(predict_number)             
        