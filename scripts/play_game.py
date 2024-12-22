#!/usr/bin/env python3

from guess_game.game import start_game
from guess_game.utils import get_valid_number_input
import prompt

def play_game():
    """
    Главная функция, которая запускает игру.
    """
    print('''
    Привет, игрок! Давай сыграем в увлекательную игру! Я загадаю число от 1 до 100, 
    а ты и твои друзья будете пытаться угадать его за 3 попытки. 
    После каждого ответа я буду давать подсказки: число больше или меньше твоего. 
    Максимальное количество игроков — 4 человека. 
    Готовы? Давайте начнем!''')

    while True:
        try:
            num_players = prompt.string('Сколько человек будет участвовать в игре? (максимум 4): ')
            num_players = int(num_players)
            if 1 <= num_players <= 4:
                break
            else:
                print("Ошибка: количество игроков должно быть от 1 до 4.")
        except ValueError:
            print("Ошибка: введите корректное число.")

    players = []
    for i in range(num_players):
        player_name = prompt.string(f'Отлично! Как тебя зовут {i+1} искатель приключений?: ')
        players.append({'name': player_name, 'attempts': 0, 'get_input': get_valid_number_input})

    # Запуск игры
    result = start_game(players)
    print(result)