import random


def get_player_guess(player, computer_number):
    """Получить ввод игрока и проверить его."""
    user_answer = player['get_input'](
        f'{player["name"]}, твоя очередь! Введи любое значение от 1 до 100: ',
        1,
        100
    )
    player['attempts'] += 1
    if user_answer == computer_number:
        return (f'Поздравляю {player["name"]}, '
                f'ты угадал число за {player["attempts"]} попыток!'), True
    elif user_answer > computer_number:
        return (f'Ой, {player["name"]}, загаданное число меньше! '
                f'Попробуй еще раз.'), False
    else:
        return (f'Не угадал, {player["name"]}! '
                f'Загаданное число больше, продолжай искать.'), False


def is_game_over(players, computer_number):
    """Проверить, завершена ли игра
    (есть ли победитель или все игроки исчерпали попытки)."""
    for player in players:
        if player['attempts'] < 3:
            return False  # Игра не завершена, если у игрока есть попытки
    return True  # Игра завершена, если все игроки исчерпали попытки


def start_game(players):
    """
    Основная логика игры. Каждый игрок по очереди пытается угадать число.
    :param players: Список словарей с игроками (имя и количество попыток).
    :return: Победитель или сообщение о завершении игры.
    """
    computer_number = random.randint(1, 100)
    print("Загадано число от 1 до 100. У каждого игрока будет 3 попытки.")

    while True:
        for player in players:
            if player['attempts'] < 3:
                result, guessed = get_player_guess(player, computer_number)
                print(result)

                if guessed:  # Если число угадано, заканчиваем игру.
                    return result

        # Если все игроки сделали 3 попытки, игра заканчивается
        if is_game_over(players, computer_number):
            return (f'Игра окончена. К сожалению, никто не угадал число.'
                    f'Загаданное число было: {computer_number}.')
