# TODO решите задачу
import json

def task(path: str) -> float:
    """
    Функция читает JSON файл, вычисляет произведение значений ключей "score" и "weight"
    в каждом словаре, затем возвращает сумму этих произведений, округленную до 3 знаков.
    :return: Округленная сумма произведений "score" * "weight".
    """
    # Открываем файл data.json в режиме чтения
    with open(path, 'r') as file:
        # Загружаем содержимое файла в переменную data
        data = json.load(file)

    # Инициализируем сумму
    total = 0.0

    # Итерация по каждому словарю в списке
    for entry in data:
        # Извлекаем значения ключей "score" и "weight"
        score = entry.get("score", 0)  # Значение по умолчанию 0
        weight = entry.get("weight", 0)  # Значение по умолчанию 0

        # Добавляем произведение "score" и "weight" к общей сумме
        total += score * weight

    # Возвращаем сумму, округленную до 3 знаков после запятой
    return round(total, 3)

# Вызываем функцию и выводим результат
if __name__ == "__main__":
    path = 'input.json'
    print(task(path))

