from abc import ABC, abstractmethod


class GameObject(ABC):
    def __init__(self, obj_id, name, x, y):
        self._id = obj_id
        self._name = name
        self._x = x
        self._y = y

    def get_id(self):
        return self._id

    def get_name(self):
        return self._name

    def get_x(self):
        return self._x

    def get_y(self):
        return self._y


class Attacker(ABC):
    def attack(self, unit):
        pass


class Moveable(ABC):
    def move(self, new_x, new_y):
        pass


class Unit(GameObject):
    def __init__(self, obj_id, name, x, y, hp):
        super().__init__(obj_id, name, x, y)
        self._hp = hp

    def is_alive(self):
        return self._hp > 0

    def get_hp(self):
        return self._hp

    def receive_damage(self, damage):
        self._hp -= damage
        if self._hp < 0:
            self._hp = 0


class Archer(Unit, Attacker, Moveable):
    def __init__(self, obj_id, name, x, y, hp, attack_power):
        super().__init__(obj_id, name, x, y, hp)
        self._attack_power = attack_power

    def attack(self, unit):
        if isinstance(unit, Unit) and unit.is_alive():
            unit.receive_damage(self._attack_power)

    def move(self, new_x, new_y):
        self._x = new_x
        self._y = new_y


class Building(GameObject):
    def __init__(self, obj_id, name, x, y, built=False):
        super().__init__(obj_id, name, x, y)
        self._built = built

    def is_built(self):
        return self._built


class Fort(Building, Attacker):
    def __init__(self, obj_id, name, x, y, built=False, attack_power=50):
        super().__init__(obj_id, name, x, y, built)
        self._attack_power = attack_power

    def attack(self, unit):
        if isinstance(unit, Unit) and unit.is_alive():
            unit.receive_damage(self._attack_power)


class MobileHome(Building, Moveable):
    def __init__(self, obj_id, name, x, y, built=False):
        super().__init__(obj_id, name, x, y, built)

    def move(self, new_x, new_y):
        self._x = new_x
        self._y = new_y


if __name__ == "__main__":
    archer = Archer(1, "Archer1", 0, 0, 100, 25)
    enemy = Unit(2, "Enemy1", 1, 1, 50)
    fort = Fort(3, "Fort1", 5, 5, built=True)
    mobile_home = MobileHome(4, "MobileHome1", 2, 2, built=True)

    print(f"Archer HP: {archer.get_hp()}")
    print(f"Enemy HP: {enemy.get_hp()}")

    archer.attack(enemy)
    print(f"Enemy HP after attack: {enemy.get_hp()}")

    mobile_home.move(10, 10)
    print(f"Mobile Home new position: ({mobile_home.get_x()}, {mobile_home.get_y()})")
