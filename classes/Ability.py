class Ability:
    def __init__(self, action_log, name, damage, mana_cost):
        self.action_log = action_log
        self.name = name
        self.damage = damage
        self.mana_cost = mana_cost

    def cast(self, attacking_character, defending_character):
        # The attacking_character should reduce their mana to use the attack
        # The defending_character should reduce their health
        # A message should be displayed for the ability use
        pass
