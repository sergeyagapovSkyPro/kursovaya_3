from config import *
import json
from datetime import datetime
import re


def load_json_file():
    """
    Функция читает json файл
    """
    with open(OPERATIONS, encoding='utf-8') as file:
        json_user_operations = json.load(file)
    return json_user_operations


def get_operations_date(values):
    """
    Функция получает одобренные операции
    """
    executed_operations = []
    for value in values:
        if value == {}:
            continue
        elif value["state"] == "EXECUTED":
            executed_operations.append(value)
    return executed_operations


def sort_operations_date(operations):
    """
    Функция выводит 5 последних операций
    """
    sort_listing = sorted(operations, key=lambda x: datetime.strptime(x["date"], "%Y-%m-%dT%H:%M:%S.%f"), reverse=True)
    list_operations = sort_listing[:5]
    return list_operations


def change_data(date):
    """
    Функция сортирует дату
    """
    data_operations = []
    for sort_date in date:
        sort_operations = datetime.strptime(sort_date["date"], "%Y-%m-%dT%H:%M:%S.%f")
        format_date = f"{sort_operations:%d.%m.%Y}"
        data_operations.append(format_date)
    return data_operations


def mask_card_number(card_numbers):
    """Функция скрывает номер карты
    """
    list_card = []
    for card in card_numbers:
        if card["description"] == "Открытие вклада":
           card["from"] = f"Счет пользователя: {card['to'][5:]}"
        from_format_check = card['from'].split()
        from_format_check_copy = from_format_check.copy()
        del from_format_check_copy[-1]
        from_check_spaces = re.findall('....', from_format_check[-1])
        from_cipher_check = (from_check_spaces[0], from_check_spaces[1][0:2] + '**',
                             from_check_spaces[2].replace(from_check_spaces[2], "****"), from_check_spaces[3:])
        frpm_join_cipher_check = ' '.join(from_cipher_check[3])
        list_card.append(f"{' '.join(from_format_check_copy)} {' '.join(list(from_cipher_check[0:3]))} "
                         f"{frpm_join_cipher_check}")
    return list_card


def mask_amount_number(amount_number):
    """
    Функция скрывает номер счета
    """
    list_check = []
    for check in amount_number:
        format_to_check = re.findall('....', check['to'])
        check_to_index = format_to_check[4:]
        check_tuple = check_to_index[0].replace(check_to_index[0], "**"), check_to_index[1]
        to_check = ''.join(list(check_tuple))
        list_check.append(to_check)
    return list_check