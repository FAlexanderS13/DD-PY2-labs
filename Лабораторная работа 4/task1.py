class Vehicle:
    """
    Базовый класс для представления транспортного средства.

    Attributes:
        brand (str): Марка транспортного средства.
        model (str): Модель транспортного средства.
        year (int): Год выпуска транспортного средства.
    """
    def __init__(self, brand: str, model: str, year: int):
        """
        Инициализирует транспортное средство с заданными маркой, моделью и годом выпуска.

        Args:
            brand (str): Марка транспортного средства.
            model (str): Модель транспортного средства.
            year (int): Год выпуска транспортного средства.
        Raises:
            ValueError: Если год выпуска меньше 1900 или больше текущего года.
        """
        if not isinstance(brand, str) or not brand:
            raise ValueError("Brand должен быть непустой строкой.")
        if not isinstance(model, str) or not model:
            raise ValueError("Model должна быть непустая строка.")
        if not isinstance(year, int) or year < 1900 or year > 2024: # Предполагая, что текущий год - 2024
            raise ValueError("Year должен быть между 1900 и 2024 годами.")

        self.brand = brand
        self.model = model
        self.year = year

    def __str__(self) -> str:
        """
        Возвращает строковое представление объекта Vehicle.
        """
        return f"{self.brand} {self.model} ({self.year})"

    def __repr__(self) -> str:
        """
        Возвращает строковое представление объекта Vehicle для отладки.
        """
        return f"Vehicle(brand='{self.brand}', model='{self.model}', year={self.year})"

    def get_description(self) -> str:
        """
        Возвращает краткое описание транспортного средства.
        """
        return f"Это {self.brand} {self.model} сделана в {self.year}."

    def start_engine(self) -> str:
        """
        Имитирует запуск двигателя транспортного средства.
        """
        return "Двигатель заработал."


class Car(Vehicle):
    """
    Дочерний класс для представления легкового автомобиля, наследуемый от Vehicle.

    Attributes:
        brand (str): Марка транспортного средства.
        model (str): Модель транспортного средства.
        year (int): Год выпуска транспортного средства.
        num_doors (int): Количество дверей у автомобиля.
    """
    def __init__(self, brand: str, model: str, year: int, num_doors: int):
        """
        Инициализирует легковой автомобиль, наследуя атрибуты от базового класса Vehicle и добавляя атрибут num_doors.

        Args:
            brand (str): Марка транспортного средства.
            model (str): Модель транспортного средства.
            year (int): Год выпуска транспортного средства.
            num_doors (int): Количество дверей у автомобиля.

        Raises:
            ValueError: Если количество дверей меньше 2 или больше 5.
        """
        super().__init__(brand, model, year)
        if not isinstance(num_doors, int) or num_doors < 2 or num_doors > 5:
            raise ValueError("Количество дверей должно быть от 2 до 5.")

        self.num_doors = num_doors

    def __str__(self) -> str:
        """
        Перегруженный метод __str__ для добавления информации о количестве дверей.
        Причина перегрузки: Необходимо отображать специфическую для легковых автомобилей информацию.
        """
        return f"{super().__str__()} с {self.num_doors} дверьми."

    def __repr__(self) -> str:
        """
        Перегруженный метод __repr__ для добавления информации о количестве дверей.
        """
        return f"Машина(brand='{self.brand}', model='{self.model}', year={self.year}, num_doors={self.num_doors})"

    def get_description(self) -> str:
        """
        Перегруженный метод get_description для добавления информации о количестве дверей.
        Причина перегрузки: Необходимо предоставить более детализированное описание легкового автомобиля, чем у базового транспортного средства.
        """
        return f"{super().get_description()} Она имеет {self.num_doors} двери."

    def honk(self) -> str:
        """
        Имитирует звуковой сигнал автомобиля.
        """
        return "Бип-бип!"

    def start_engine(self) -> str:
        """
        Имитирует запуск двигателя транспортного средства.
        """
        return "Двигатель автомобиля завелся"

if __name__ == "__main__":
    # Пример использования
    try:
        my_car = Car("Toyota", "Camry", 2022, 4)
        print(my_car)  # Output: Toyota Camry (2022) with 4 doors.
        print(repr(my_car))  # Output: Car(brand='Toyota', model='Camry', year=2022, num_doors=4)
        print(my_car.get_description())  # Output: This is a Toyota Camry made in 2022. It has 4 doors.
        print(my_car.start_engine())
        print(my_car.honk())  # Output: Beep beep!

        my_vehicle = Vehicle("Generic", "Model", 2000)
        print(my_vehicle.start_engine())

    except ValueError as e:
        print(f"Error: {e}")