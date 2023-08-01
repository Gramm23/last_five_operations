import json
from datetime import datetime

data_file = "/home/gramm23/PycharmProjects/last_five_operations/main/operations.json"


def open_json(data_file):
    with open(data_file, encoding='utf-8') as file_json:
        operations_list = json.load(file_json)
        return operations_list


data_list = open_json(data_file)


def get_filtered_list(data_list):
    """
    Фильтрует список данных, удаляя все пустые словари.
    :param data_list: Список операций, который нужно отфильтровать.
    :return: Отфильтрованный список, содержащий только непустые и истинные значения.
    """
    data_file = [operation for operation in data_list if operation]
    return data_file


filtered_list = get_filtered_list(data_list)


def get_sorted_list(filtered_list):
    """
    Возвращает отсортированный список по дате операций.
    :param filtered_list: Список операций, который требуется отсортировать. Каждая операция представлена в виде словаря,
        содержащего ключ "date" с датой операции.
    :return: Отсортированный список операций по убыванию даты.
    """
    sorted_filtered_list = sorted(filtered_list, key=lambda operations: operations['date'], reverse=True)
    return sorted_filtered_list


sorted_list = get_sorted_list(filtered_list)


def get_last_operations(sorted_list):
    """
    Возвращает последние пять выполненных операций из отсортированного списка.
    :param sorted_list: Отсортированный список, содержащий операции.
    :return: Список последних пяти выполненных операций. Каждая операция представлена в виде словаря.
    """
    five_last_operation = []
    for operation in sorted_list:
        if operation['state'] == 'EXECUTED':
            five_last_operation.append(operation)
    return five_last_operation[0:5]


last_operations = get_last_operations(sorted_list)


def formatted_date(last_operations):
    """
    Форматирует дату в каждом элементе списка last_operations в новый формат.
    :param last_operations: Список словарей, представляющих операции, где каждый словарь имеет ключ 'date',
    содержащий строку с датой в формате "%Y-%m-%dT%H:%M:%S.%f".
    :return: Обновленный список last_operations с значениями 'date', отформатированными в "%d.%m.%Y".
    """
    for item in last_operations:
        date_str = item['date']
        date_obj = datetime.strptime(date_str, "%Y-%m-%dT%H:%M:%S.%f")
        new_date_str = date_obj.strftime("%d.%m.%Y")
        item['date'] = new_date_str
    return last_operations


format_date = formatted_date(last_operations)


def mask_number(data_list, key1, key2):
    """
    Маскирует номера счетов и банковских карт в списке словарей.
    :param data_list: Список словарей, представляющих элементы данных.
    :param key1: Ключ 'from' в каждом словаре, содержащий первый номер для маскировки.
    :param key2: Ключ 'to' в каждом словаре, содержащий второй номер для маскировки.
    :return: Измененная версия входного списка data_list с замаскированными номерами.
    """
    for item in data_list:
        if key1 in item:
            number = item[key1].split()
            if len(number[-1]) >= 20:
                item[key1] = f'{"".join(number[0:-1])} **{number[-1][-4:]}'
            elif len(number[-1]) <= 16:
                item[key1] = f'{" ".join(number[0:-1])} {number[-1][0:4]} {number[-1][4:6]}** **** {number[-1][-4:]}'
        if key2 in item:
            number_to = item[key2].split()
            if len(number_to[-1]) >= 20:
                item[key2] = f'{"".join(number_to[0:-1])} **{number_to[-1][-4:]}'
            elif len(number_to[-1]) <= 16:
                item[key2] = (f'{" ".join(number_to[0:-1])} {number_to[-1][0:4]} '
                              f'{number_to[-1][4:6]}** **** {number_to[-1][-4:]}')

    return data_list


operations = mask_number(format_date, 'from', 'to')
