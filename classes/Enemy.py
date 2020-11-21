from classes.Ability import Ability
from random import choice
from classes.Character import Character


class Enemy(Character):
    # If you add any new messages here, they need to have n_or_no_n and enemy_name
    ENEMY_ENCOUNTER_MESSAGES = [
        "You see a{n_or_no_n} {enemy_name}!", "A{n_or_no_n} {enemy_name} has crossed your path!"
    ]

    def get_action(self):
        # Randomly choose between all abilities and a regular attack
        # Regular attack should be returned as "Regular Attack"
        # If you don't have enough mana to use a specific abiilty, the ability should not be selectable
        pass

    def display_enemy_encounter_message(self):
        enemy_encounter_message = choice(Enemy.ENEMY_ENCOUNTER_MESSAGES)
        n_or_no_n = ""

        if self.name[0].lower() in ["a", "e", "i", "o", "u"]:
            n_or_no_n = "n"

        print(enemy_encounter_message.format(n_or_no_n=n_or_no_n, enemy_name=self.name))
        print()

    def take_turn(self, player):
        action = self.get_action()

        if isinstance(action, Ability):
            self.use_ability(action, player)
        elif action == "Regular Attack":
            self.use_regular_attack(player)
        else:
            print(self, "did nothing.")

        print()
