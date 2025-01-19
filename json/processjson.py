import json

from typing import Callable

# Функция для обработки json
# Функция для обработки должна принимать параметры:

# строку с json;
# список ключей, которые необходимо обработать;
# список токенов, которые нужно найти;
# функцию-обработчик ключа и токена.
# json для задания всегда имеет вид словаря с ключами и значениями из строк.

# Функция парсит строку с json библиотечными средствами. Для каждого ключа json, который совпадает с одним из переданных ключей для обработки, функция должна искать вхождения токенов в строку-значение по данному ключу. Для каждого найденного токена должна быть вызвана функция-обработчик с ключом и токеном.

# Поиск ключей должен зависеть от регистра, а поиск токенов должен быть регистронезависимым.


def formatter(key: str, token: str):
    return f"{key=}, {token=}"


def process_json(
    json_str: str,
    required_keys: list[str],
    tokens: list[str],
    callback: Callable[[str, str], None] | None = formatter,
) -> None:
    if not required_keys:
        print('Список required_keys не должен быть пуст')
    if not tokens:
        print('Список tokens не должен быть пуст')
    json_str = json.loads(json_str)
    low_tokens = list(map(lambda i: i.lower(), tokens))

    for key, value in json_str.items():
        if key in required_keys:
            value_list = list(map(lambda i: i.lower(), value.split()))

            for ind, token in enumerate(low_tokens):
                if token in value_list:
                    print(callback(key, tokens[ind]))
