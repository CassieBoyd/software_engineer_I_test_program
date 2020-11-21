from classes.Ability import Ability
from classes.Character import Character


class Player(Character):
    AMOUNT_TO_INCREASE_STRENGTH_PER_LEVEL_UP_POINT = 1
    AMOUNT_TO_INCREASE_DEFENSE_PER_LEVEL_UP_POINT = 0.05
    AMOUNT_TO_INCREASE_MAX_MANA_PER_LEVEL_UP_POINT = 1
    AMOUNT_TO_INCREASE_MAX_HEALTH_PER_LEVEL_UP_POINT = 10

    strength = 10
    defense = 0.25
    max_mana = 10
    max_health = 100

    def __init__(self, action_log, name):
        super(Player, self).__init__(action_log, name, self.strength, self.defense, self.max_mana, self.max_health)

        self.abilities += [
            Ability(self.action_log, "Smash", 50, 5)
        ]

    def rest(self):
        self.current_mana += 3
        self.current_health += 30

        if self.current_mana > self.max_mana:
            self.current_mana = self.max_mana

        if self.current_health > self.max_health:
            self.current_health = self.max_health

    def level_up(self):
        # Finish the remainder of this function including validation and appropriate assignment

        print("You have 3 actions you can take:")
        print("    s = Increase strength by", self.AMOUNT_TO_INCREASE_STRENGTH_PER_LEVEL_UP_POINT)
        print("    d = Increase defense by", self.AMOUNT_TO_INCREASE_DEFENSE_PER_LEVEL_UP_POINT)
        print("    m = Increase max mana by", self.AMOUNT_TO_INCREASE_MAX_MANA_PER_LEVEL_UP_POINT)
        print("    h = Increase max health by", self.AMOUNT_TO_INCREASE_MAX_HEALTH_PER_LEVEL_UP_POINT)

        choices_are_valid = False

        while not choices_are_valid:

            # Example 1: s s d
            # Example 2: d h m
            # Example 3: m s d

            # Using .split to turn input into a list
            choices = input("Enter your 3 choices separated by spaces: ").split(" ")

            print(choices)

            # Validate the choices
            # Check that there are 3 selections by checking the list length. If the length is 3, set choices_are_valid to True. Else, give an error message.
            if len(choices) == 3:
                choices_are_valid = True
                print("success")
            else:
                print("Error! Please enter 3 choices separated by spaces: ")


        print()

    def take_turn(self, enemy):
        is_invalid_input = True

        while is_invalid_input:
            is_invalid_input = False

            print("r = Regular Attack")
            print("s = Smash")
            action = input("Choose an action: ")

            print()

            if action == "r":
                self.use_regular_attack(enemy)
            elif action == "s":
                # IMPLEMENT: If the player doesn't have enough mana, they can't cast the ability
                self.use_ability(self.abilities[0], enemy)

                # Temporary code until abilities are in place
                print("You did nothing.")
            else:
                is_invalid_input = True
