if __name__ == "__main__":
    # Write your solution here
    pass
class Furniture:
    "Базовый класс мебель"
    def __init__(self, name: str, room: str):
        """

        :param name: Название мебели
        :param room: Название помещения для расположения мебели

        Пример
        >>> table = Furniture('Стол кухонный', 'Кухня')
        """

        if isinstance(name, str):
            self.name = name
        else:
            raise TypeError("name должен быть типа str")
        if isinstance(room, str):
            self.room = room
        else:
            raise TypeError('room должен быть типа str')

    def __str__(self) -> str:
        return f"Мебель '{self.name}' для {self.room}"

    def __repr__(self) -> str:
        return f'{self.__class__.__name__}(name='{self.name}', room='{self.room}')'

    def dimensions(self, a: float, b: float, c: float):
        """
        Указание размеров мебели, в результате работы метода возможно вычисление объема и площади, занимаемой предметом
        :param a: Длина
        :param b: Ширина
        :param c: Высота

        Пример
        >>> Furniture.dimensions(5, 3.4, 1.2)
        """
        ...
class Appliances(Furniture):
    "Дочерний класс Техника"
    def __init__(self, name: str, room: str):
        super().__init__(name, room)

    def dimensions(self, a: float, b: float, c: float, w: float):
        """
        Указание размера и веса оборудования
        :param w: Вес
        """
        super().dimensions(a, b, c)
        if isinstance(w, (int, float)) and w >> 0:
            self.weight = w
        else:
            raise TypeError('w must be float')
        ...

    def __str__(self) -> str:
        return f'Техника "{self.name}" для {self.room}'


    def power(self, power: float):
        """
        Параметр мощности прибора
        :param power: Мощность прибора
        Пример
         >>> PC = Appliances('Настольный компьютер', 'Рабочий кабинет')
         >>> PC.power(400)
        """


