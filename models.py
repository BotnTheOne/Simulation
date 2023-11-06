class Entity:
    def __init__(self):
        self.health = 0
        self.speed = 0
        self.move = 0
        self.strength = 0


class Objects(Entity):
    def __init__(self):
        super().__init__()


class Grass(Objects):
    def __init__(self):
        super().__init__()
        self.health = 1


class Rock(Objects):
    def __init__(self):
        super().__init__()
        self.health = 999


class Tree(Objects):
    def __init__(self):
        super().__init__()
        self.health = 499


class Creature(Entity):
    def __init__(self):
        super().__init__()
        self.health = 10
        self.speed = 1
        self.move = 1
        self.strength = 1

    def make_move(self):
        pass


class Herbivore(Creature):
    def __init__(self):
        super().__init__()
        self.health = 20
        self.strength = 0


class Predator(Creature):
    def __init__(self):
        super().__init__()
        self.speed = 2


class Map:
    pass


class Simulation:
    def next_turn(self):
        pass

    def start_simulation(self):
        pass

    def pause_simulation(self):
        pass


class Actions:
    def init_actions(self):
        pass

    def turn_actions(self):
        pass


if __name__ == '__main__':
    x = Entity()
    print('Entity: ', vars(x))
    y = Objects()
    print('Objects: ', vars(y))
    z = Grass()
    print('Grass: ', vars(z))
    r = Predator()
    print('Predator: ', vars(r))
