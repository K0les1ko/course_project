import json
import pytest
from src.functions import *




OPERATIONS_JSON_PATH ='/Users/nikolayyaroshenko/Desktop/develop/pythonProject/skypro/course_project/src/operations.json'


def test_get_date():
    assert get_date('2023-09-27T14:30:00') == '27.09.2023'


def test_mask_number():
    assert mask_number('1234567890123456', is_card=True) == 'Карта 123456******3456'
    assert mask_number('1234567890123456', is_card=False) == 'Счет 3456'
    assert mask_number('12345678', is_card=False) == 'Счет 5678'


def test_print_recent_operations(capsys):
    with open(OPERATIONS_JSON_PATH, 'r') as file:
        data = json.load(file)

    # Проверка наличия данных в файле
    assert len(data) > 0

    # Проверка работы функции
    print_recent_operations(data)

    # Проверка вывода
    captured = capsys.readouterr()
    assert 'Карта' in captured.out
    assert 'Счет' in captured.out
    assert 'руб.' in captured.out
