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
        # If you don't have enough mana to use a specific ability, the ability should not be selectable

        # Putting abilities in a new list and appending the list with string "Regular Attack"
        all_enemy_attacks = self.abilities
        all_enemy_attacks.append("Regular Attack")

        # choice method returns a randomly selected item
        enemy_attack = choice(all_enemy_attacks)

        # print("Current Mana", self.current_mana)
        # print("Cost", enemy_attack.mana_cost)

        # isinstance checks to see if enemy_attack is an instance of Ability. current_mana is checked to see whether it's greater than or equal to the mana_cost of enemy_attack. 
        # Else, return Regular Attack.
        if isinstance(enemy_attack, Ability) and self.current_mana >= enemy_attack.mana_cost:
            return enemy_attack
        else:
            return "Regular Attack"
        
        

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
