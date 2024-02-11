class Book:
    """ Базовый класс книги. """
    def __init__(self, name: str, author: str):
        self._name = name
        self._author = author

    def __str__(self):
        return f"Книга {self.name}. Автор {self.author}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r})"

    @property
    def name(self):
        return self._name

    @property
    def author(self):
        return self._author

class PaperBook(Book):
    def __init__(self, name: str, author: str, pages: int):
        super().__init__(name,author)
        if isinstance(pages, int) and pages > 0:
            self.pages = pages
        else:
            raise ValueError("Количество страниц должно быть представлено положительным целым числом")

    def __str__(self):
        return f"Книга {self.name}. Автор {self.author}, Количество страниц {self.pages}"
    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, pages={self.pages!r})"

class AudioBook(Book):
    def __init__(self, name: str, author: str, duration: float):
        super().__init__(name, author)
        if isinstance(duration, (int, float)) and duration > 0:
            self.duration = duration
        else:
            raise ValueError("Продолжительность должна быть представлена положительным числом")

    def __str__(self):
        return f"Книга {self.name}. Автор {self.author}, Продолжительность {self.duration}"
    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, duration={self.duration!r})"


