class Enemy():
    def __init__(self):
        raise NotImplementedError("Do not create raw Enemy objects.")

    def __str__(self):
        return self.name

    def is_alive(self):
        return self.hp > 0


class Looter(Enemy):
    def __init__(self):
        self.name = "Looter"
        self.hp = 10
        self.damage = 2

class Pirate(Enemy):
    def __init__(self):
        self.name = "Pirate"
        self.hp = 25
        self.damage = 7

class Ghoul(Enemy):
    def __init__(self):
        self.name = "Ghoul"
        self.hp = 50
        self.damage = 12

class Jinn(Enemy):
    def __init__(self):
        self.name = "Jinn"
        self.hp = 70
        self.damage = 20