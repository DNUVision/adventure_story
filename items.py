class Weapon():
    def __init__(self):
        raise NotImplementedError("Do not create raw Weapon objects.")
    def __str__(self):
        return self.name

class Rock(Weapon):
    def __init__(self):
        self.name = "Rock"
        self.description = "A fist-sized rock, suitable for bludgeoning"
        self.damage = 5

class Dagger(Weapon):
    def __init__(self):
        self.name = "Dagger"
        self.description = "A small dagger with some rust. " \
                           "Somewhat more dangerous than a rock."
        self.damage = 10

class RustySword(Weapon):
    def __init__(self):
        self.name = "Rusty Sword"
        self.description = "This sword is showing its age." \
                           "but still has some fight in it."
        self.damage = 20

class Sword(Weapon):
    def __init__(self):
        self.name = "Sword"
        self.description = "A crude sword." \
                           "it is fine for a melee combat."
        self.damage = 25

class Consumable:
    def __init__(self):
        raise NotImplementedError("Do not create raw Consumable objects.")

    def __str__(self):
        return "{} (+{}HP).".format(self.name, self.healing_value)

class CrustyBread(Consumable):
    def __init__(self):
        self.name = "Crusty Bread"
        self.healing_value = 10

class Dates(Consumable):
    def __init__(self):
        self.name = "Dates"
        self.healing_value = 15

