import json


def filter_and_sort(data):
    items = [item for item in data if item.get('state') == 'EXECUTED']
    items.sort(key=lambda x: x.get('date'), reverse=True)
    return items


def get_date(data):
    parts = data.split('T')[0].split('-')
    return '.'.join(reversed(parts))


def mask_number(number, is_card=True):
    if is_card:

        # Развернем строку, заменим цифры с 5 по 10 на звездочки и снова развернем
        reversed_number = ''.join(reversed(number))
        masked_number = ''.join('*' if 4 <= i < 10 else digit for i, digit in enumerate(reversed_number))
        masked_number = ''.join(reversed(masked_number))
        return f"Карта {masked_number}"
    else:
        return f"Счет {number[-4:]}"



def print_recent_operations(data):
    recent_operations = filter_and_sort(data)[:5]

    for operation in recent_operations:
        operation_date = get_date(operation['date'])
        operation_description = operation['description']

        # Проверка, является ли картой
        is_card = any(prefix in operation.get('from', '').lower() for prefix in ['mastercard', 'visa', 'maestro'])

        # Маскировка
        masked_number = mask_number(operation.get('from', ''), is_card)
        masked_account = mask_number(operation.get('to', ''),False)

        amount = operation['operationAmount']['amount']
        currency = operation['operationAmount']['currency']['name']

        print(f"{operation_date} {operation_description}")
        print(f"{masked_number} -> {masked_account}")
        print(f"{amount} {currency}\n")


# Чтение данных из JSON-файла
with open('operations.json', 'r') as file:
    data = json.load(file)


