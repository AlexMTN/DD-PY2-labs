class Book:
    """ Базовый класс книги."""
    def __init__(self, name: str, author: str):
        """
        Создание и подготовка экземпляра 'книга'.
        ----------------------------
        Параметры:
        :param name: str - Название книги
        :param author: str - Автор книги
        ----------------------------
        Пример:
        >>> book = Book("Introducing Python", "Bill Lubanovic") # инициализация объекта
        >>> print(repr(book))
        Book(name='Introducing Python', author='Bill Lubanovic')
        """
        if isinstance(name, str):
            self._name = name
        else:
            raise ValueError("name must be a string.")

        if isinstance(author, str):
            self._author = author
        else:
            raise ValueError("author must be a string.")

    def __str__(self) -> str:
        return f"Книга {self.name}. Автор {self.author}"

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r})"

    @property   # Добавляем свойств, чтобы была возможность ТОЛЬКО ВЫВОДА значений защищенных атрибутов _name и _author
    def name(self) -> str:
        return self._name

    @property
    def author(self) -> str:
        return self._author


class PaperBook(Book):
    """Дочерний класс 'бумажная книга' """
    def __init__(self, name: str, author: str, pages: int):
        """
        Создание объекта 'бумажная книга'.
        ----------------------------
        Параметры:
        :param name: str - Название книги
        :param author: str - Автор книги
        :param pages: int, gt=0 - Количество страниц
        """
        super().__init__(name, author)  # Вызов конструктора экземпляра из базового класса
        self.pages = pages

    @property
    def pages(self) -> int:
        return self._pages

    @pages.setter   # Свойство с проверками при присвоении значения
    def pages(self, pages: int):
        if isinstance(pages, int) and pages > 0:
            self._pages = pages
        else:
            raise ValueError("pages must be a positive integer.")

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(name={self._name!r}, author={self._author!r}, pages={self._pages})"


class AudioBook(Book):
    """Дочерний класс 'аудио книга' """
    def __init__(self, name: str, author: str, duration: float):
        """
        Создание объекта 'аудио книга'
        ----------------------------
        Параметры:
        :param name: str - Название книги
        :param author: str - Автор книги
        :param duration: float, gt=0 - Продолжительность аудио книги
        """
        super().__init__(name, author)  # Вызов конструктора экземпляра из базового класса
        self.duration = duration

    @property
    def duration(self) -> float:
        return self._duration

    @duration.setter    # Свойство с проверками при присвоении значения
    def duration(self, duration: float):
        if isinstance(duration, float) and duration > 0:
            self._duration = duration
        else:
            raise ValueError("duration must be a positive float.")

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(name={self._name!r}, author={self._author!r}, duration={self._duration})"
