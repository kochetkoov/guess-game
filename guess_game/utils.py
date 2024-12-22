import prompt


def get_valid_number_input(prompt_message, min_value, max_value):
    """
    Функция для безопасного ввода числа с проверкой на диапазон.
    :param prompt_message: Сообщение для пользователя.
    :param min_value: Минимальное значение.
    :param max_value: Максимальное значение.
    :return: Валидное число.
    """
    while True:
        try:
            user_input = prompt.string(prompt_message)
            user_input = int(user_input)
            if min_value <= user_input <= max_value:
                return user_input
            else:
                print(f"Ошибка: число от {min_value} до {max_value}.")
        except ValueError:
            print("Ошибка: введено не число. Попробуй снова.")
