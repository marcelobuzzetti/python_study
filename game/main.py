import os
import sys
import platform
from classes.game import Player, Enemy

print(platform.system())

def main():
    player = Player("Player", 100)
    enemy = Enemy("Enemy", 100)

    while player.is_alive() and enemy.is_alive():
        print(player)
        print(enemy)
        player.take_damage(10)
        enemy.take_damage(10)

if __name__ == "__main__":
    main()