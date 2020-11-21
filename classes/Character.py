import math


class Character:
    def __init__(self, action_log, name, strength, defense, max_mana, max_health):
        self.action_log = action_log
        self.name = name
        self.strength = strength
        self.defense = defense
        self.max_mana = max_mana
        self.max_health = max_health

        self.abilities = []
        self.current_mana = max_mana
        self.current_health = max_health

    def __str__(self):
        return self.name

    @property
    def mana_ratio_string(self):
        return str(self.current_mana) + "/" + str(self.max_mana)

    @property
    def health_ratio_string(self):
        return str(self.current_health) + "/" + str(self.max_health)

    def use_regular_attack(self, defending_character):
        damage = self.strength * (1 - self.defense)
        print(self.name, "hit", defending_character.name + ".")
        defending_character.take_damage(damage)

    def take_damage(self, damage):
        damage = math.floor(damage)
        self.current_health -= damage
        print(self.name, "took", damage, "damage!")

    def use_ability(self, ability, defending_character):
        ability.cast(self, defending_character)
