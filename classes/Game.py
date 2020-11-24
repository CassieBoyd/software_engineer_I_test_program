from random import choice

from black_magic import get_player_and_enemy_info_box_lines
from classes.ActionLog import ActionLog
from classes.Chicken import Chicken
from classes.Player import Player
from classes.Rabbit import Rabbit


class Game:
    class PlayerDiedException(Exception):
        pass

    def __init__(self, number_of_enemies_to_kill=5):
        self.number_of_enemies_to_kill = number_of_enemies_to_kill

        self.action_log = ActionLog()

        player_name = input("Player Name: ").strip()
        self.player = Player(self.action_log, player_name)

        # Add additional enemies here
        self.enemies = [
            Chicken,
            Rabbit
        ]

        self.current_enemy = None

    def run(self):
        try:
            for i in range(self.number_of_enemies_to_kill):
                self.fight()
        except self.PlayerDiedException:
            pass

        self.action_log.write_action_log_to_file()

    def fight(self):
        EnemyClass = self.get_random_enemy()
        self.current_enemy = EnemyClass(self.action_log)

        self.current_enemy.display_enemy_encounter_message()

        self.display_player_and_enemy_info()

        while self.current_enemy.current_health > 0 and self.player.current_health > 0:
            self.player.take_turn(self.current_enemy)
            self.current_enemy.take_turn(self.player)

            self.display_player_and_enemy_info()

        if self.player.current_health <= 0:
            raise self.PlayerDiedException("You died!")

        self.player.level_up()
        self.player.rest()

    def get_random_enemy(self):
        return choice(self.enemies)

    def display_player_and_enemy_info(self):
        for line in get_player_and_enemy_info_box_lines(self.player, self.current_enemy):
            print(line)

        print()
