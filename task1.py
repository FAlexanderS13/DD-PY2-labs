import doctest


class Vk:
    def __init__(self, views_number: int, likes_number: int):
        """
        Создание и подкотовка объекта "Соцсеть"

        :param views_number: количество просмотров
        :param likes_number: количество лайков

        Примеры:
        >>> vk = Vk(500, 600)  # инициализация экземпляра класса
        """
        if not isinstance(views_number, (int)):
            raise TypeError("Количество просмотров должно быть типа int")
        if views_number < 0:
            raise ValueError("Количество просмотров должно быть неотрицательным числом")
        self.views_number = views_number

        if not isinstance(likes_number, (int)):
            raise TypeError("Количество лайков должно быть типа int")
        if likes_number < 0:
            raise ValueError("Количество лайков должно быть неотрицательным числом")
        self.likes_number = likes_number

    def system_operation(self) -> bool:
        """
        Функция которая проверяет есть ли просмотры и лайки

        :return: Работает ли программа

        Примеры:
        >>> vk = Vk(500,600)
        >>> vk.system_operation()
        """
        ...

    def detection_of_violation(self) -> bool:
        """
        Обнаружение обана программы (накрутка)

        :return: Есть ли факт нарушения

        Примеры:
        >>> vk = Vk(500,600)
        >>> vk.detection_of_violation()
        """
        ...


class Fuel_tank:
    def __init__(self, tank_volume: float, occupied_volume: float):
        """
        Создание и подготовка к работе объекта "Бензобак"
        :param tank_volume: Объем бака
        :param occupied_volume: Объем занимаемого топлива

        Примеры:
        >>> fuel_tank = Fuel_tank(100,50) # инициализация экземпляра класса
        """
        if not isinstance(tank_volume, (int, float)):
            raise TypeError("Объем бака должен быть типа int или float")
        if tank_volume <= 0:
            raise ValueError("Объем топливного бака должен быть положительным")
        self.tank_volume = tank_volume

        if not isinstance(occupied_volume, (int, float)):
            raise TypeError("Объем топлива должен быть типа int или float")
        if occupied_volume < 0:
            raise ValueError("Количество топлива должно быть неотрицательным")
        self.occupied_volume = occupied_volume

    def fuel_waste(self, spent_fuel: float) -> None:
        """
        Расход бензина из-за отработки

        :param spent_fuel: объем отработанного бензина
        :raise ValueError: Если количество отработанного топлива превышает количество топлива в баке,
        то возвращается ошибка.

        :return: объем отработанного топлива

        Примеры:
        >>> fuel_tank = Fuel_tank(100,50)
        >>> fuel_tank.fuel_waste(50)
        """
        ...

    def tank_filling(self, fuel: float) -> None:
        """
        Заправка топливного бака
        :param fuel: количество заправляемого топлива

        :raise ValueError: Если количество заправляемого топлива превышает свободное место в баке, то вызываем ошибку

        Примеры:
        >>> fuel_tank = Fuel_tank(100,50)
        >>> fuel_tank.tank_filling(45)
        """

    ...


class Geometric_figure:
    def __init__(self, color: str, area: float):
        """
        Создание и подготовка к работе объекта "Гемоетрическая фигура"

        :param color: Цвет фигуры
        :param area: Площадь фигуры

        Примеры:
        >>> geometric_figure = Geometric_figure("красный", 100) # инициализация экземпляра класса
        """
        if not isinstance(color, (str)):
            raise TypeError("Цвет фигуры должен быть типа str")
        self.color = color

        if not isinstance(area, (int, float)):
            raise TypeError("Площадь фигуры должна быть типа int или float")
        if area <= 0:
            raise ValueError("Площадь фигуры должна быть положительным числом")
        self.area = area

    def init(self) -> str:
        """
        Функция инициализирует фигуру с заданным цветом

        :raise ValueError: Если строка "Цвет" - пустая вызываем ошибку

        Примеры:
        >>> geometric_figure = Geometric_figure("red",100)
        """
        ...

    def color_change(self, new_color: str) -> None:
        """
        Изменение цвета фигуры
        :param new_color: Новый цвет фигуры

         :raise ValueError: Если new_color - пустая строка

         Примеры:
         >>> geometric_figure = Geometric_figure("red",100)
         >>> geometric_figure.color_change("blue")
        """
        ...


if __name__ == "__main__":
    doctest.testmod()  # тестирование примеров, которые находятся в документации
