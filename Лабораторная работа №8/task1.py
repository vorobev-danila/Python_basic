class Mug:
    """
    Базовый класс для кружек.
    """

    def __init__(self, material: str, capacity: int) -> None:
        """
        Инициализация кружки.
        :param material: Материал кружки (например, керамика, стекло, металл)
        :param capacity: Вместимость кружки в миллилитрах
        """
        self._material = material  # Инкапсуляция, т.к. материал не должен изменяться напрямую
        self.capacity = capacity

    def __str__(self) -> str:
        """
        Человеко-читаемое представление кружки.
        """
        return f"Кружка из {self._material}, вместимость {self.capacity} мл"

    def __repr__(self) -> str:
        """
        Формальное представление объекта кружки.
        """
        return f"Mug(material='{self._material}', capacity={self.capacity})"

    def drink(self, amount: int) -> str:
        """
        Симулирует процесс питья из кружки.
        :param amount: Количество миллилитров для питья
        :return: Сообщение о результате
        """
        return f"Вы выпили {amount} мл из кружки."


class RegularMug(Mug):
    """
    Обычная кружка, наследуется от базового класса Mug.
    """

    def __init__(self, material: str, capacity: int, has_handle: bool = True) -> None:
        """
        Инициализация обычной кружки.
        :param material: Материал кружки
        :param capacity: Вместимость кружки
        :param has_handle: Есть ли у кружки ручка
        """
        super().__init__(material, capacity)
        self.has_handle = has_handle

    def __str__(self) -> str:
        """
        Перегрузка метода __str__, добавляя информацию о ручке.
        """
        handle_text = "с ручкой" if self.has_handle else "без ручки"
        return f"Обычная кружка из {self._material}, {handle_text}, вместимость {self.capacity} мл"


class ThermoMug(Mug):
    """
    Термокружка, наследуется от базового класса Mug.
    """

    def __init__(self, material: str, capacity: int, heat_retention: int) -> None:
        """
        Инициализация термокружки.
        :param material: Материал кружки
        :param capacity: Вместимость кружки
        :param heat_retention: Время удержания тепла в минутах
        """
        super().__init__(material, capacity)
        self.heat_retention = heat_retention

    def __str__(self) -> str:
        """
        Перегрузка метода __str__, добавляя информацию о времени сохранения тепла.
        """
        return f"Термокружка из {self._material}, сохраняет тепло {self.heat_retention} минут, вместимость {self.capacity} мл"

    def drink(self, amount: int) -> str:
        """
        Перегрузка метода drink().
        Причина: термокружки обычно имеют крышку, поэтому пить можно только небольшими глотками.
        :param amount: Количество миллилитров для питья
        :return: Сообщение о результате
        """
        if amount > 100:
            return "Нельзя выпить сразу так много, термокружка имеет крышку!"
        return super().drink(amount)



if __name__ == "__main__":
    # Пример использования
    mug = RegularMug("керамика", 300)
    thermo_mug = ThermoMug("металл", 500, 120)

    print(mug)
    print(thermo_mug)
    print(thermo_mug.drink(150))
