class Creature:
    """Базовый класс существа"""
    def __init__(self, name: str, level: int):
        """

        :param name: Имя существа | protected, изменять имя после иннициализации экземпляра нельзя
        :param level: Уровень существа | protected, изменять уровень после иннициализации можно только методом level_up()
        :param hp: Здоровье существа | Рассчитвыется автоматически | protected, изменяется автоматически на основе level
        """
        if isinstance(name, str):
            self._name = name
        else:
            raise TypeError("The name must be a string.")

        if isinstance(level, int) and level > 0:
            self._level = level
        else:
            raise TypeError("The level must be a positive integer.")

        self._hp = round(self._level_hp_checker() * self._level)

    def _level_hp_checker(self) -> int or float:
        """
        Метод, определяющий домножающий коэффициент для расчета здоровья (HP)
        protected, используется только внутри классов
        :return: hp_factor -> float
        """
        hp_factor = 0
        if self._level in range(1, 11):
            hp_factor += 10
        elif self._level in range(11, 21):
            hp_factor += 12.5
        elif self._level > 20:
            hp_factor += 15
        return hp_factor

    def level_up(self, level: int):
        """
        Метод увеличивающий уровень существа и обновляет значение здоровья (hp)

        :param level: Количество добавляемых уровней
        :return: Печатает сообщение об увеличении уровня
        """
        if isinstance(level, int) and level > 0:
            self._level += level
            self._hp = round(self._level_hp_checker() * self._level)
        else:
            raise TypeError("The level must be a positive integer.")
        return print(f"Level up! {self._name} gained {level} levels.\nNew stats are: LVL:{self._level} | HP:{self._hp}")

    @property # getter только для чтения атрибута
    def name(self):
        return self._name

    @property # getter только для чтения атрибута
    def level(self):
        return self._level

    @property # getter только для чтения атрибута
    def hp(self):
        return self._hp

    def __str__(self):
        return f"Type: {self.__class__.__name__}\n" \
               f"Name: {self._name}\n" \
               f"Stats: LVL:{self._level} | HP:{self.hp}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self._name}, level={self._level})"


class Humanoid(Creature):
    """Дочерний класс существа 'гуманоид'"""
    HUMANOID_RACE_LIST = ["Dwarf", "Elf", "Goblin"]

    def __init__(self, name: str, level: int, race: str):
        """

        :param name: Имя гуманоида | protected, изменять имя после иннициализации экземпляра нельзя
        :param level: Уровень гуманоида | protected, изменять уровень после иннициализации можно только методом level_up()
        :param hp: Здоровье существа | Рассчитвыется автоматически | protected, изменяется автоматически на основе level
        :param race: Раса гуманоида | protected, изменять расу после иннициализации экземпляра нельзя
        """
        super().__init__(name, level)

        if not isinstance(race, str):
            raise TypeError("The race must be a string.")
        if race not in Humanoid.HUMANOID_RACE_LIST:
            raise ValueError("Available races: Dwarf, Elf, Goblin")
        self._race = race

    @property # getter только для чтения атрибута
    def race(self):
        return self._race

    def __str__(self):
        return f"Type: {self.__class__.__name__}\n" \
               f"Name: {self._name}\n" \
               f"Race: {self._race}\n" \
               f"Stats: LVL:{self._level} | HP:{self.hp}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self._name}, level={self._level}, race={self._race})"


class Monster(Creature):
    def __init__(self, name: str, level: int):
        """

        :param name: Имя монстра | protected, изменять имя после иннициализации экземпляра нельзя
        :param level: Уровень монстра | protected, изменять уровень после иннициализации можно только методом level_up()
        :param hp: Здоровье существа | Рассчитвыется автоматически | protected, изменяется автоматически на основе level
        :param anger: Злость монстра | Рассчитвыется автоматически | protected, изменяется автоматически на основе level
        """
        super().__init__(name, level)
        self._anger = round(self.__level_anger_checker() * self._level)

    def _level_hp_checker(self) -> int or float:
        """
        Метод, определяющий домножающий коэффициент для расчета здоровья Monster (HP)
        protected, метод должен использоваться лишь внутри классов
        hp_factor увеличен
        """
        hp_factor = 0
        if self._level in range(1, 11):
            hp_factor += 12.5
        elif self._level in range(11, 21):
            hp_factor += 15
        elif self._level > 20:
            hp_factor += 20
        return hp_factor

    def __level_anger_checker(self) -> float:
        """
        Метод, определяющий домножающий коэффициент для расчета злости Monster (anger)
        private, метод должен использоваться лишь внутри класса Monster
        :return: anger_factor -> int
        """
        anger_factor = 1
        if self._level in range(1, 11):
            anger_factor += 0.2
        elif self._level in range(11, 21):
            anger_factor += 0.5
        elif self._level > 20:
            anger_factor += 0.7
        return anger_factor

    @property   # getter только для чтения атрибута
    def anger(self):
        return self._anger

    def __str__(self):
        return f"Type: {self.__class__.__name__}\n" \
               f"Name: {self._name}\n" \
               f"Anger: {self._anger}\n" \
               f"Stats: LVL:{self._level} | HP:{self.hp}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self._name}, level={self._level}, anger={self._anger})"


if __name__ == "__main__":
    creature = Creature("Some kind of creature", 15)
    bob = Humanoid("Bob", 11, "Dwarf")
    vivern = Monster("Vivern", 11)
    print(f"{creature}\n"
          f"\n{bob}\n"
          f"\n{vivern}")
    bob.level_up(15)