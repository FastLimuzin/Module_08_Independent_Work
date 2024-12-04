# Задача 1:
class Circle:
    def __init__(self, radius):
        self.radius = radius

    def length(self):
        return 2 * 3.14159 * self.radius

    def area(self):
        return 3.14159 * (self.radius ** 2)


class Square:
    def __init__(self, side):
        self.side = side

    def perimeter(self):
        return 4 * self.side

    def area(self):
        return self.side ** 2


class CircleInSquare(Circle, Square):
    def __init__(self, radius, side):
        Circle.__init__(self, radius)
        Square.__init__(self, side)


# Задача 2:
class Wheels:
    def __init__(self, material, size):
        self._material = material
        self._size = size

    @property
    def material(self):
        return self._material

    @property
    def size(self):
        return self._size


class Engine:
    def __init__(self, power, type_engine):
        self._power = power
        self._type_engine = type_engine

    @property
    def power(self):
        return self._power

    @property
    def type_engine(self):
        return self._type_engine

class Doors:
    def __init__(self, count, lock_type):
        self._count = count
        self._lock_type = lock_type

    @property
    def count(self):
        return self._count

    @property
    def lock_type(self):
        return self._lock_type

    @lock_type.setter
    def lock_type(self, lock_type):
        self._lock_type = lock_type


class Car:
    def __init__(self, wheels: Wheels, engine: Engine, doors: Doors):
        self._wheels = wheels
        self._engine = engine
        self._doors = doors

    @property
    def wheels(self):
        return self._wheels

    @property
    def engine(self):
        return self._engine

    @property
    def doors(self):
        return self._doors


# Задача 3:
class Pet:
    def __init__(self, name):
        self._name = name

    def get_name(self):
        return self._name

    def get_sound(self):
        raise NotImplementedError("Этот метод должен быть переопределён в подклассе")

    def get_type(self):
        raise NotImplementedError("Этот метод должен быть переопределён в подклассе")


class Dog(Pet):
    def get_sound(self):
        return "Гав!"

    def get_type(self):
        return "Собака"


class Cat(Pet):
    def get_sound(self):
        return "Мяу!"

    def get_type(self):
        return "Кошка"


class Parrot(Pet):
    def get_sound(self):
        return "Чик чирик!"

    def get_type(self):
        return "Попугай"


class Hamster(Pet):
    def get_sound(self):
        return "Пи-пи!"

    def get_type(self):
        return "Хомяк"


# Задача 4:
class Employer:
    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age

    def print(self):
        print("Это базовый класс Employer")


class President(Employer):
    def print(self):
        print(f"Президент: {self.name} {self.surname}, Возраст: {self.age}")


class Manager(Employer):
    def print(self):
        print(f"Менеджер: {self.name} {self.surname}, Возраст: {self.age}")


class Worker(Employer):
    def print(self):
        print(f"Рабочий: {self.name} {self.surname}, Возраст: {self.age}")


# Задача 5:
class Employer:
    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age

    def print(self):
        print("Это базовый класс Employer")

    def __str__(self):
        return f"Служащий: {self.name} {self.surname}, Возраст: {self.age}"

    def __int__(self):
        return self.age