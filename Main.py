import random
from time import sleep
import os
from enum import Enum
game_over = False


class Thing:

    def __init__(self, name, description):
        self.name = name
        self.description = description


class Treasure(Thing):
    def __init__(self, name, description, value):
        super().__init__(name, description)
        self.value = value


class ThingHolder(Thing):
    def __init__(self, name, description, things):
        super().__init__(name, description)
        self.things = things

    def add(self, thing):
        self.things.append(thing)

    def remove(self, thing):
        self.things.remove(thing)

    def get_things(self):
        if len(self.things) == 0:
            return "Nothing"
        print("Contents:")
        for thing in self.things:
            print("- " + thing.name)


class Player(ThingHolder):

    def __init__(self, name, description, things, room):
        super().__init__(name, description, things)
        self.room = room

    def move(self, rooms, direction):
        if direction == "n" and self.room.n != -1:
            self.room = rooms[self.room.n]
        elif direction == "s" and self.room.s != -1:
            self.room = rooms[self.room.s]
        elif direction == "w" and self.room.w != -1:
            self.room = rooms[self.room.w]
        elif direction == "e" and self.room.e != -1:
            self.room = rooms[self.room.e]
        else:
            print("You Can't Go There")

    def doors(self):
        if self.room.n != -1:
            print("North")
        if self.room.s != -1:
            print("South")
        if self.room.w != -1:
            print("West")
        if self.room.e != -1:
            print("East")


class Room(ThingHolder):
    def __init__(self, name, description, n, s, w, e, things):
        super().__init__(name, description, things)
        self.n = n
        self.s = s
        self.w = w
        self.e = e


# generate random treasures from a list of treasures
def generate_treasures(treasures):
    new_treasures = []
    for i in range(random.randint(0, 3)):
        new_treasures.append(treasures[random.randint(1, len(treasures)-1)])
    # if there are two or more of the same treasure, remove one
    if len(new_treasures) > 1:
        for i in range(len(new_treasures)):
            for j in range(i+1, len(new_treasures)):
                if new_treasures[i] == new_treasures[j]:
                    new_treasures.remove(new_treasures[i])
                    break
    return new_treasures


def main():
    # Game Initialisation
    treasures = [Treasure("Sword", "A sword", 10), Treasure("Shield", "A shield", 5), Treasure("Helmet", "A helmet", 3)]

    rooms = [
        Room("Outside", "Very Dark", 1, -1, -1, 2, []),
        Room("Entrance", "There is a dimly lit light bulb. Nothing else.", 3, 0, 4, -1, generate_treasures(treasures)),
        Room("Green House", "Its very green", -1, -1, 0, -1, generate_treasures(treasures)),
        Room("Hall", "The hall is extremely long", 5, 1, -1, -1, generate_treasures(treasures)),
        Room("Basement", "It's extremely dark, you need to turn on a light", -1, -1, -1, 1, generate_treasures(treasures)),
        Room("Living Room", "It's super cozy in here surprisingly", -1, 3, -1, -1, generate_treasures(treasures))
    ]
    player = Player("Player", "You are a player", [], rooms[0])
    # Main Game Loop
    while not game_over:
        command = input(">>> ").strip().lower()
        os.system("cls")
        if command == "where":
            print(player.room.name)
            print(player.room.description)
            print("Places You Can Go:")
            player.doors()
            player.room.get_things()

        elif command == "n":
            player.move(rooms, "n")
        elif command == "s":
            player.move(rooms, "s")
        elif command == "w":
            player.move(rooms, "w")
        elif command == "e":
            player.move(rooms, "e")
        elif command == "pick up":
            item = input("What do you want to pick up? ")
            for thing in player.room.things:
                if thing.name == item:
                    player.add(thing)
                    player.room.remove(thing)
                    print("You picked up " + item)
                    break
        elif command == "drop":
            item = input("What do you want to drop? ")
            for thing in player.things:
                if thing.name == item:
                    player.room.add(thing)
                    player.remove(thing)
                    print("You dropped " + item)
                    break
        elif command == "inventory":
            player.get_things()
        else:
            print("Not A Valid Command")


main()
