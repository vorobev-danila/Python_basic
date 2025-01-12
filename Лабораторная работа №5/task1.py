from typing import Union
import doctest


class Computer:
    def __init__(self, brand: str, processor_speed: float, ram_size: int):
        """
        Создание объекта "Компьютер".

        :param brand: Бренд компьютера
        :param processor_speed: Скорость процессора в ГГц
        :param ram_size: Размер оперативной памяти в ГБ

        Примеры:
        >>> computer = Computer("Dell", 3.5, 16)
        """
        if not isinstance(brand, str):
            raise TypeError("brand должен быть строкой")
        if not isinstance(processor_speed, (int, float)) or processor_speed <= 0:
            raise ValueError("processor_speed должен быть положительным числом")
        if not isinstance(ram_size, int) or ram_size <= 0:
            raise ValueError("ram_size должен быть положительным целым числом")
        self.brand = brand
        self.processor_speed = processor_speed
        self.ram_size = ram_size

    def turn_on(self) -> None:
        """
        Включить компьютер.

        Примеры:
        >>> computer = Computer("Dell", 3.5, 16)
        >>> computer.turn_on()
        """
        ...

    def turn_off(self) -> None:
        """
        Выключить компьютер.

        Примеры:
        >>> computer = Computer("Dell", 3.5, 16)
        >>> computer.turn_off()
        """
        ...

    def upgrade_ram(self, additional_ram: int) -> None:
        """
        Увеличить оперативную память.

        :param additional_ram: Дополнительный объем оперативной памяти в ГБ

        Примеры:
        >>> computer = Computer("Dell", 3.5, 16)
        >>> computer.upgrade_ram(8)
        """
        if not isinstance(additional_ram, int) or additional_ram <= 0:
            raise ValueError("additional_ram должен быть положительным целым числом")
        self.ram_size += additional_ram

class Thermos:
    def __init__(self, brand: str, capacity: float):
        """
        Создание объекта "Термос".

        :param brand: Бренд термоса
        :param capacity: Объем термоса в литрах

        Примеры:
        >>> thermos = Thermos("Thermos", 1.5)
        """
        if not isinstance(brand, str):
            raise TypeError("brand должен быть строкой")
        if not isinstance(capacity, (int, float)) or capacity <= 0:
            raise ValueError("capacity должен быть положительным числом")
        self.brand = brand
        self.capacity = capacity
        self.current_volume = 0

    def fill(self, volume: float) -> None:
        """
        Наполнить термос жидкостью.

        :param volume: Объем добавляемой жидкости в литрах

        Примеры:
        >>> thermos = Thermos("Thermos", 1.5)
        >>> thermos.fill(1)
        """
        if not isinstance(volume, (int, float)) or volume <= 0:
            raise ValueError("volume должен быть положительным числом")
        if self.current_volume + volume > self.capacity:
            raise ValueError("Термос переполнен")
        self.current_volume += volume

    def pour(self, volume: float) -> None:
        """
        Вылить жидкость из термоса.

        :param volume: Объем выливаемой жидкости в литрах

        Примеры:
        >>> thermos = Thermos("Thermos", 1.5)
        >>> thermos.pour(0.5)
        """
        if not isinstance(volume, (int, float)) or volume <= 0:
            raise ValueError("volume должен быть положительным числом")
        if volume > self.current_volume:
            raise ValueError("Недостаточно жидкости в термосе")
        self.current_volume -= volume

class Speaker:
    def __init__(self, brand: str, max_volume: int):
        """
        Создание объекта "Колонка".

        :param brand: Бренд колонки
        :param max_volume: Максимальная громкость колонки

        Примеры:
        >>> speaker = Speaker("JBL", 100)
        """
        if not isinstance(brand, str):
            raise TypeError("brand должен быть строкой")
        if not isinstance(max_volume, int) or max_volume <= 0:
            raise ValueError("max_volume должен быть положительным целым числом")
        self.brand = brand
        self.max_volume = max_volume
        self.current_volume = 0

    def play_music(self) -> None:
        """
        Воспроизведение музыки.

        Примеры:
        >>> speaker = Speaker("JBL", 100)
        >>> speaker.play_music()
        """
        ...

    def increase_volume(self, increment: int) -> None:
        """
        Увеличить громкость.

        :param increment: Значение увеличения громкости

        Примеры:
        >>> speaker = Speaker("JBL", 100)
        >>> speaker.increase_volume(10)
        """
        if not isinstance(increment, int) or increment <= 0:
            raise ValueError("increment должен быть положительным целым числом")
        if self.current_volume + increment > self.max_volume:
            raise ValueError("Превышена максимальная громкость")
        self.current_volume += increment

    def decrease_volume(self, decrement: int) -> None:
        """
        Уменьшить громкость.

        :param decrement: Значение уменьшения громкости

        Примеры:
        >>> speaker = Speaker("JBL", 100)
        >>> speaker.decrease_volume(10)
        """
        if not isinstance(decrement, int) or decrement <= 0:
            raise ValueError("decrement должен быть положительным целым числом")
        if self.current_volume - decrement < 0:
            raise ValueError("Громкость не может быть ниже 0")
        self.current_volume -= decrement

if __name__ == "__main__":
    doctest.testmod()  # тестирование примеров, которые находятся в документации

