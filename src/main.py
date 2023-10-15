import json
from functions import read_json_data, print_recent_operations

# Путь к JSON-файлу
OPERATIONS_JSON_PATH = '/Users/nikolayyaroshenko/Desktop/develop/pythonProject/skypro/course_project/src/operations.json'

# Чтение данных из JSON-файла
data = read_json_data(OPERATIONS_JSON_PATH)

# Вызов функции для вывода операций
print_recent_operations(data)