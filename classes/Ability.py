from classes.ActionLog import ActionLog

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

        # print("Attacking character", attacking_character)
        # print("Defending character", defending_character)
        attacking_character.current_mana -= self.mana_cost
        defending_character.current_health -= self.damage
        print(f"{attacking_character.name} used {self.name}!")
        self.action_log.add_to_action_list(f"{attacking_character.name} used {self.name}!" + "\n")

        print(f"{defending_character.name} took {self.damage} damage!")
        self.action_log.add_to_action_list(f"{defending_character.name} took {self.damage} damage!" + "\n")
