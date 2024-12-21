# TODO импортировать необходимые молули
import csv
import json

INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def task() -> None:
    # Читаем содержимое CSV файла
    with open(INPUT_FILENAME, "r", encoding="utf-8") as csv_file:
        reader = csv.DictReader(csv_file)  # Используем DictReader для преобразования строк в словари
        data = [row for row in reader]  # Собираем все строки в список словарей

    # Сериализуем данные в JSON формат с отступами равными 4
    with open(OUTPUT_FILENAME, "w", encoding="utf-8") as json_file:
        json.dump(data, json_file, ensure_ascii=False, indent=4)


if __name__ == '__main__':
    # Нужно для проверки
    task()

    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")
