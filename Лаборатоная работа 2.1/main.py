# TODO Написать 3 класса с документацией и аннотацией типов
import doctest
from typing import Union
class Particle:
    def __int__(self, name: str, energy: Union[int, float], mass: Union[int, float]):
        """
         Создание и подготовка к работе объекта "Частица"
        :param name: название частицы
        :param energy: энергия частицы в МэВ
        :param mass: масса частицы в а.е.м.
        Пример:
        >>> particle = Particle("Протон",160,1)
        """
        if not isinstance(name, str):
            raise TypeError ("По рузкэ")
        if not isinstance(energy, (int, float)):
            raise TypeError ("Энергия это число")
        if not energy >= 0:
            raise ValueError ("Частица не может иметь в данном случае отрицателую энергию")
        if not isinstance(mass, (int, float)):
            raise TypeError ("Масса это число")
        if not mass >= 0:
            raise ValueError ("Частица не может иметь в данном случае отрицателую массу")
        self.energy = energy
        self.mass = mass
        self.name = name
    def relative_or_not(self) -> bool:
        """
        Функция, которая проверяет движется ли частица со скростью порядка с
        :return: Является ли частица релятивисткой
        Пример:
        >>> particle = Particle("Протон",160,1)
        >>> particle.relative_or_not()
        """
        ...

    def depth_of_penetration_in_water(self) -> int:
        """
        Функция расчитывающая путь (см) пройденный частицей в воде
        :return depth
        Пример:
        >>> particle = Particle("Протон",160,1)
        >>> depth = particle.depth_of_penetration_in_water()

        """
        ...

from typing import Dict

class Fridge:
    def __int__(self, list_of_animals: dict) -> Dict[str: int]:
        """
        Создание и заполнение холодильник животными
        :param dict_of_animals: словарь животных помещенных в холодильник
        Пример:
        >>> fridge = Fridge({'слон':1, 'крот':2})

        """
        if not isinstance(list_of_animals, dict):
            raise TypeError ("Нужен словарь живности")
        if not isinstance(list_of_animals, (str, int)):
            raise TypeError ("Нужно указать имя животоного str и его количество int")
        self.list_of_animals = list_of_animals

    def add_animal(self, animal: str, count: int) -> None:

        """
        Изменяет наполнение холодильника
        :param animal:  какое жиотное добавить
        :param count: сколько добавить
        :return: обновленный холодильник
         Пример:
        >>> fridge = Fridge({'слон':1, 'крот':2})
        >>> fridge.add_animal('шиншилла', 3)
        """
        if not isinstance(animal, str):
            raise TypeError ("Нужно название животного str")
        if not isinstance(count, int):
            raise TypeError ("Нужно колличество животного int")
        ...

class Soldier:
    def __int__(self, name: str, hp: Union[int,float], atc: Union[int,float]):
        """
        Созание бойца
        :param name: Позывной
        :param hp: Здоровье
        :param atc: Атака
        Пример:
        >>> soldier = Soldier("Goust",200, 15)
        """
        if not isinstance(name, str):
            raise TypeError ("Позывной str")
        if not isinstance(hp, str) or not isinstance(atc, (int, float)):
            raise TypeError ("Характеристики в числах int, float")

    def upgrade(self, type_of_equipment: int  ) -> None:

        """
        Меняет экипировку под поле битвы
        :param type_of_equipment: тип экипровки
        :return: Обновленные характеистики бойца
        Пример:
        >>> soldier = Soldier("Goust",200 , 15)
        >>> soldier.upgrade(2)
        """

        if not isinstance(type_of_equipment, int):
            raise TypeError("выбери класс экипировки int")
        if type_of_equipment < 1 or type_of_equipment > 5:
            raise ValueError("Выбери экипировку из номеров (1,2,3,4,5)")
        ...

if __name__ == "__main__":
    # TODO работоспособность экземпляров класса проверить с помощью doctest

    doctest.testmod()
print(particle.depth_of_penetration_in_water())
print(fridge.add_animal())
print(soldier.upgrade())

