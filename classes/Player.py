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

            # Using .lower() to lowercase user input and .split to turn input into a list
            choices = input("Enter your 3 choices separated by spaces: ").lower().split(" ")

            valid_choices = ["s", "d", "m", "h"]


            # Validate the choices
            # Check that there are 3 selections by checking the list length. 
            # choices is converted to a set so that .difference can be used to compare valid_choices to choices. The result is passed to list(), which lists the differences (if any) between the two. The length of the resulting list is checked.
            if len(choices) == 3 and len(list(set(choices).difference(valid_choices))) == 0:
            # If both conditionals are true, choices_are_valid is set to True and the for loop executes.
                choices_are_valid = True
                for stat in choices:
                    if (stat == "s"):
                        print("Strength increased!")
                    elif (stat == "d"):
                        print("Defense increased!")
                    elif (stat == "m"):
                        print("Mana increased!")
                    elif (stat == "h"):
                        print("Health increased!")
                

            # Else, give an error message.
            else:
                print("Error! Invalid input!")


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
