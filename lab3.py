class Singleton:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(Singleton, cls).__new__(cls, *args, **kwargs)
        return cls._instance

    def do_something(self):
        print("Singleton's working")

#Пример
singleton1 = Singleton()
singleton2 = Singleton()
print(singleton1 is singleton2)
singleton1.do_something()

from abc import ABC, abstractmethod

class Animal(ABC):
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

class AnimalFactory:
    def create_animal(animal_type):
        if animal_type == "dog":
            return Dog()
        elif animal_type == "cat":
            return Cat()
        else:
            raise ValueError("Unknown animal type")

# Пример работы AnimalFactory
if __name__ == "__main__":
    try:
        dog = AnimalFactory.create_animal("dog")
        print(f"собака говорит: {dog.speak()}")
        cat = AnimalFactory.create_animal("cat")
        print(f"кошка говорит: {cat.speak()}")
        unknown_animal = AnimalFactory.create_animal("bird")
        print(unknown_animal.speak())
    except ValueError as e:
        print(f"Error: {e}") #а кто это...


# Abstract Factory
class GUIFactory(ABC):
    @abstractmethod
    def create_button(self):
        pass

    @abstractmethod
    def create_checkbox(self):
        pass

class WindowsFactory(GUIFactory):
    def create_button(self):
        return WindowsButton()

    def create_checkbox(self):
        return WindowsCheckbox()

class MacFactory(GUIFactory):
    def create_button(self):
        return MacButton()

    def create_checkbox(self):
        return MacCheckbox()

class Button(ABC):
    @abstractmethod
    def click(self):
        pass

class WindowsButton(Button):
    def click(self):
        return "Windows button clicked!"

class MacButton(Button):
    def click(self):
        return "Mac button clicked!"

class Checkbox(ABC):
    @abstractmethod
    def check(self):
        pass

class WindowsCheckbox(Checkbox):
    def check(self):
        return "Windows checkbox checked!"

class MacCheckbox(Checkbox):
    def check(self):
        return "Mac checkbox checked!"

def application(factory: GUIFactory):
    button = factory.create_button()
    checkbox = factory.create_checkbox()
    print(button.click())
    print(checkbox.check())


windows_factory = WindowsFactory()
application(windows_factory)



# Builder Pattern
class House:
    def __init__(self):
        self.walls = None
        self.roof = None
        self.doors = None
        self.windows = None

class HouseBuilder:
    def __init__(self):
        self.house = House()

    def build_walls(self, walls):
        self.house.walls = walls
        return self

    def build_roof(self, roof):
        self.house.roof = roof
        return self

    def build_doors(self, doors):
        self.house.doors = doors
        return self

    def build_windows(self, windows):
        self.house.windows = windows
        return self

    def get_house(self):
        return self.house

#Пример билдера
builder = HouseBuilder()
house = (
    builder.build_walls("Brick walls")
           .build_roof("Tile roof")
           .build_doors("Wooden doors")
           .build_windows("Double-glazed windows")
           .get_house()
)

print("House details:")
print(f"Walls: {house.walls}")
print(f"Roof: {house.roof}")
print(f"Doors: {house.doors}")
print(f"Windows: {house.windows}")
