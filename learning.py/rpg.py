#!/usr/bin/env python
# Scraped from https://github.com/jusdepatate/rpg
import random


class Player:
    health = 50
    name = ""
    isfighting = False
    golds = 20
    kills = 0
    isplaying = True

    inventory = [
        "Dagger"
    ]


class Game:

    def __init__(self):
        self.ennemyhealth = 0
        self.ennemy = ""

        print("Welcome to this little textual RPG")
        print("Made by Jus de Patate_")

        while Player.name == "":
            Player.name = input("What's the name of your character ?\n")

        print("You have", Player.golds, "golds and your weapon is", Player.inventory[0])

    def explore(self):
        print(Player.name, "finds a new room and explore it...")

        if Player.isfighting:
            print("You can't explore while in fight")
            return 0

        rng = random.randint(0, 45)

        if rng < 25:
            # fight room
            Player.isfighting = True
            self.ennemyhealth = 25
            self.ennemy = "Goblin"

            print("Oh no, it's a", self.ennemy, "! Fight him or die !")
        elif rng < 40:
            # loot room
            rng = random.randint(1, 3)

            if rng == 1:
                Player.inventory.append("Gem")
                loot = "a gem"
            elif rng == 2:
                Player.inventory.append("Ancient Scroll")
                loot = "an ancient scroll"
            elif rng == 3:
                Player.golds += 5
                loot = "5 golds"

            print(Player.name, "finds a room with a chest,", Player.name, "opens it and finds", loot)
        else:
            # empty room
            print("You find an empty room.")

    def fight(self):
        if Player.isfighting:
            rng = random.randint(0, 15)
            if rng == 0:
                print(Player.name, "misses", self.ennemy)
            else:
                print(Player.name, "hits ennemy for", rng, "HP")
                self.ennemyhealth = self.ennemyhealth - rng
        else:
            print("You cannot fight yourself")

    def sheet(self):
        print(Player.name, "killed", Player.kills, "monsters.")
        print(Player.name, "has", Player.health, "HP.")
        print("Your bag contains:")
        print(Player.golds, "golds")
        for i in Player.inventory:
            print(i)

    def checks(self):
        if Player.isfighting:
            rng = random.randint(0, 15)
            if rng == 0:
                print(self.ennemy, "misses", Player.name)
            else:
                print(self.ennemy, "hits", Player.name, "for", rng, "HP")
                Player.health = Player.health - rng

            if Player.health <= 0:
                print(Player.name, "is dead.")
                quit()
            if self.ennemyhealth <= 0:
                print(self.ennemy, "is dead.")
                Player.isfighting = False
                self.ennemy = ""
                Player.kills += 1


def detect(cmd):
    if cmd == "explore" or cmd == "e":
        Game.explore(Game)
    elif cmd == "fight" or cmd == "f":
        Game.fight(Game)
    elif cmd == "sheet" or cmd == "s":
        Game.sheet(Game)
    elif cmd == "quit" or cmd == "q":
        print(Player.name, "killed himself inside the dungeon")
        Player.isplaying = False

    else:
        print("Command List:")
        print("e / explore : explore the dungeon")
        print("f / fight : available only in fights")
        print("s / sheet : See character (" + Player.name + ") sheet")
        print("q / quit : suicide\n")


Game()
print("")

while Player.isplaying:
    Game.checks(Game)

    print("What do you want to do ? (? for command list)")
    cmd = input()
    print("\n")

    detect(cmd)
