import doctest
# TODO Написать 3 класса с документацией и аннотацией типов

class Person:
    def __init__(self, name: str, height: float, weight: float):
        """
        Создание и подготовка к работе объекта "Человек"

        :param name: Имя человека
        :param height: Рост человека в м
        :param weight: Вес человека в кг

        Примеры:
        >>> person = Person('Маша', 1.60, 50) # Инициализация экземпляра класса
        """
        if not isinstance(name, str):
            raise TypeError("Имя человека должно быть str")
        self.name = name

        if not isinstance(height, (int, float)):
            raise TypeError("Рост человека должен быть типа int или float")
        if height <= 0:
            raise ValueError("Рост человека должен быть положительным числом")
        self.height = height

        if not isinstance(weight, (int, float)):
            raise TypeError("Вес человека должен быть типа int или float")
        if weight <= 0:
            raise ValueError("Вес человека должен быть положительным числом")
        self.weight = weight

    def index_mass_tela(self) -> float:
        """
        Расчет индекса массы тела

        :return: Расчитанный индекс массы тела

        Примеры:
        >>> person = Person('Маша', 1.60, 50)
        >>> person.index_mass_tela()
        """
        ...

    def change_height(self, new_height: float) -> float:
        """
        Вычисление величины изменения роста

        :param new_height: Новый рост в м (например человек вырос)
        :return: Разница в росте

        Примеры:
        >>> person = Person('Маша', 1.60, 50)
        >>> person.change_height(1.70)
        """
        ...

class Good:
    def __init__(self, name: str, cost: float, num: int):
        """
        Создание и подготовка к работе объекта "Товар"

        :param name: Наименование товара
        :param cost: Стоимость товара (руб)
        :param num: Количество товара в наличии (шт)

        Примеры:
        >>> good = Good('Pencil', 20, 100)
        """
        if not isinstance(name, str):
            raise TypeError("Наименование товара должно быть str")
        self.name = name

        if not isinstance(cost, (int, float)):
            raise TypeError("Стоимость должна быть типа int или float")
        if cost <= 0:
            raise ValueError("Стоимость должна быть положительным числом")
        self.cost = cost

        if not isinstance(num, int):
            raise TypeError("Количество товара в наличии должно быть типа int")
        if num < 0:
            raise ValueError("Количество товара не может быть отрицательным")
        self.num = num

    def is_in_stock(self) -> bool:
        """
        Функция проверяет находится ли товар в наличии

        :return: Находится ли товар в наличии

        Примеры:
        >>> good = Good('Pencil', 20, 100)
        >>> good.is_in_stock()
        """
        ...

    def is_sold(self, num_sold: int) -> None:
        """
        Функция которая проверяет сколько товара осталось после продажи

        :param num_sold: Количество распроданного товара (шт)
        :return: Количество оставшегося товара (шт)
        Примеры:
        >>> good = Good('Pencil', 20, 100)
        >>> good.is_sold(40)
        """
        if not isinstance(num_sold, int):
            raise TypeError("Количество распроданного товара должно быть типа int")
        if num_sold < 0:
            raise ValueError("Количество распроданного товара не может быть отрицательным")
        ...

class Article:
    def __init__(self, authors: str, pages: int, num_mistakes: int):
        """
        Создание и подготовка к работе объекта "Статья"
        :param authors: Фамилия авторов статьи
        :param pages: Количество страниц
        :param num_mistakes: Количество неисправленных ошибок в статье

        Пример:
        >>> article = Article('Toiman', 15, 2)
        """
        if not isinstance(authors, str):
            raise TypeError("Авторы должны быть str")
        self.author = authors

        if not isinstance(pages, int):
            raise TypeError("Количество страниц должно быть типа int")
        if pages <= 0:
            raise ValueError("Количество страниц должно быть положительным числом")
        self.pages = pages

        if not isinstance(num_mistakes, int):
            raise TypeError("Количество ошибок должно быть типа int")
        if num_mistakes < 0:
            raise ValueError("Количество ошибок не должно быть отрицательным числом")
        self.mistakes = num_mistakes

    def co_authorship(self, co_authors: str) -> None:
        """
        Функция для добавления соавторов статьи

        :param co_authors: Фамилия соавтора статьи
        :return: Пополнение списка авторов статьи

        Пример:
        >>> article = Article('Toiman', 15, 2)
        >>> article.co_authorship('Fiden')
        """
        ...

    def corrected_mistakes(self, corrected_mistakes) -> None:
        """
        Функция считает количество оставшихся неисправленных ошибок
        :param corrected_mistakes: Количество исправленных ошибок

        Пример:
        >>> article = Article('Toiman', 15, 2)
        >>> article.corrected_mistakes(2)
        """
        ...

if __name__ == "__main__":
    # TODO работоспособность экземпляров класса проверить с помощью doctest
    doctest.testmod()
    pass
