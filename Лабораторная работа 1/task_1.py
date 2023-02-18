# TODO Написать 3 класса с документацией и аннотацией типов
import doctest
from abc import ABC, abstractmethod

class SocialNetwork:
    """ Класс социальной сети"""
    def __init__(self, users: int, likes: int, groups:int):
        """
        Атрибуты:
        :param users (int): Количество пользователей
        :param likes (int): Количество лайков
        :param groups (int): Количество групп
        """
        if isinstance(users, int) and users > 0:
            self.users = users
        else:
            raise TypeError("Parameter 'users' must be a positive integer")
        if isinstance(likes, int) and likes > 0:
            self.likes = likes
        else:
            raise TypeError("Parameter 'likes' must be a positive integer")
        if isinstance(groups, int) and groups > 0:
            self.groups = groups
        else:
            raise TypeError("Parameter 'likes' must be a positive integer")

    def new_users(self, n: int) -> str:
        """
        Метод для увеличения количества пользователей социальной сети
        :param n: число новых юзеров
        :return: Печатает сообщение об увеличении количества пользователей (str)

        Пример:
        >>> vk = SocialNetwork(10, 100, 15)
        >>> print(vk.new_users(5))
        Количество пользователей возросло на 5! | Число пользователей: 15
        """
        self.users += n
        return f"Количество пользователей возросло на {n}! | Число пользователей: {self.users}"

    def add_like(self, n: int):
        """
        Метод для увеличения количества лайков
        :param n: число новых лайков
        :return: None
        """
        ...

    def remove_groups(self, n: int):
        """
        Метод для удаления n-го количества групп из социальной сети
        :param n: число удаляемых групп
        :return: None
        """
        ...


class Animal(ABC):
    """Базовый абстрактный класс животного"""
    @abstractmethod
    def sound(self):
        pass

    @abstractmethod
    def walk(self):
        pass


class Dog(Animal):
    """Дочерний класс 'собака'"""
    def __init__(self, name: str, breed: str):
        """

        Атрибуты:
        :param name (str): Имя собаки
        :param breed (str): Порода собаки
        """
        assert isinstance(name, str), "Parameter 'name' must be a string"
        assert isinstance(breed, str), "Parameter 'bread' must be a string"
        self.name = name
        self.breed = breed

    def sound(self):
        """
        Метод показывающий как звучит собака
        :return: "Гав!" (str)
        """
        return "Гав!"

    def walk(self):
        """
        Метод показывающий на скольки ногах ходит собака
        :return: "Ходит на четырех ногах" (str)
        """
        return "Ходит на четырех ногах"


class Square:
    """Класс для прямоугольника"""
    def __init__(self, side_a: int, side_b: int):
        """

        Атрибуты:
        :param side_a (int):
        :param side_b (int):
        """
        if isinstance(side_a, int) and side_a > 0:
            self.side_a = side_a
        else:
            raise TypeError("Side 'a' must be a positive integer")
        if isinstance(side_b, int) and side_b > 0:
            self.side_b = side_b
        else:
            raise TypeError("Side 'b' must be a positive integer")

    def area(self) -> int:
        """
        Метод для подсчета площади прямоугольника
        :return: Площадь прямоугольника (int)
        """
        return self.side_a * self.side_b

    def perimeter(self) -> int:
        """
        Метод для посчета периметра прямоугольника
        :return: Периметр прямогольника (int)
        """
        return (self.side_a + self.side_b) * 2


if __name__ == "__main__":
    # TODO работоспособность экземпляров класса проверить с помощью doctest
    doctest.testmod()
