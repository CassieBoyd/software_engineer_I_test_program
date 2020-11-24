from classes.Ability import Ability
from classes.Enemy import Enemy


class Rabbit(Enemy):
    # https://www.youtube.com/watch?v=cCI18qAoKq4
    name = "Rabbit"
    strength = 5
    defense = 0.1
    max_mana = 20
    max_health = 90

    def __init__(self, action_log):
        super(Rabbit, self).__init__(action_log, self.name, self.strength, self.defense, self.max_mana, self.max_health)

        self.abilities += [
            Ability(self.action_log, "Ravage", 30, 4),
            Ability(self.action_log, "Nibble Grass", 0, 1)
        ]