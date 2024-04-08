import numpy as np

def random_predict(number: int = 1) -> int:
    """Просто угадываем на random, никак не используя информацию о больше или меньше.
       Функция принимает загаданное число и возвращает число попыток

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    count = 0

    while True:
        count += 1
        predict_number = np.random.randint(1, 101)  # предполагаемое число
        if number == predict_number:
            break  # выход из цикла если угадали

    return count

def game_core_v2(number: int = 1) -> int:
    """Сначала устанавливаем любое random число, а потом уменьшаем
    или увеличиваем его в зависимости от того, больше оно или меньше нужного.
       Функция принимает загаданное число и возвращает число попыток

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    count = 0
    predict = np.random.randint(1, 101)

    while number != predict:
        count += 1
        if number > predict:
            predict += 1
        elif number < predict:
            predict -= 1

    return count

def game_core_v3(number: int = 1) -> int:

    # Ваш код начинается здесь

    """Сначала устанавливаем (загадываем) любое  число из диапазона то 1 до 100,
    а потом уменьшаем или увеличиваем его в зависимости от того,
    больше оно или меньше нужного с использованием алгоритма бинарного поиска.
       Функция принимает загаданное число и возвращает число попыток.

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """ 
    # Загадываем случайное число от 1 до 100
    predict_number = np.random.randint(1, 100)
    # Определяем начальные значения границ диапазона
    low = 1
    high = 100
    # Количество попыток
    count = 0

    while True:
        # Угадываем число, используя середину текущего диапазона
        guess = (low + high) // 2
        count += 1

        # Проверяем, угадали ли число
        if guess == predict_number:
            break
        # Обновляем границы диапазона в зависимости от результата
        elif guess < predict_number:
            low = guess + 1
        else:
            high = guess - 1

    # Ваш код заканчивается здесь
    
    return count

def score_game(random_predict) -> int:
    """За какое количество попыток в среднем за 10000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = []
    np.random.seed(1)  # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(10000))  # загадали список чисел

    for number in random_array:
        count_ls.append(random_predict(number))

    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за: {score} попытки")  
    
#Run benchmarking to score effectiveness of all algorithms

if __name__ == '__main__':
    print('Run benchmarking for random_predict: ', end='')
    score_game(random_predict)

    print('Run benchmarking for game_core_v2: ', end='')
    score_game(game_core_v2) 

    print('Run benchmarking for game_core_v3: ', end='')
    score_game(game_core_v3)