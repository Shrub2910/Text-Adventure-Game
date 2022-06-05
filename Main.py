import random


class Thing:

    def __init__(self, name, description):
        self.name = name
        self.description = description


class Treasure(Thing):
    def __init__(self, name, description, value, weight):
        super().__init__(name, description)
        self.value = value
        self.weight = weight


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
        print("You can see:")
        for thing in self.things:
            print("- " + thing.name)


class Player(ThingHolder):

    def __init__(self, name, description, things, room):
        super().__init__(name, description, things)
        self.room = room
        self.health = 100
        self.money = 0

    def move(self, rooms, direction):
        if direction == "n" and self.room.n != -1:
            self.room = rooms[self.room.n]
            print(self.room.name)
            print(self.room.description)
            print("Places You Can Go:")
            self.doors()
            self.room.get_things()
        elif direction == "s" and self.room.s != -1:
            self.room = rooms[self.room.s]
            print(self.room.name)
            print(self.room.description)
            print("Places You Can Go:")
            self.doors()
            self.room.get_things()
        elif direction == "w" and self.room.w != -1:
            self.room = rooms[self.room.w]
            print(self.room.name)
            print(self.room.description)
            print("Places You Can Go:")
            self.doors()
            self.room.get_things()
        elif direction == "e" and self.room.e != -1:
            self.room = rooms[self.room.e]
            print(self.room.name)
            print(self.room.description)
            print("Places You Can Go:")
            self.doors()
            self.room.get_things()
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

    def get_things(self):
        if len(self.things) == 0:
            print("You have nothing")
            return "Nothing"
        print("Inventory:")
        for thing in self.things:
            if thing.value != -1:
                print("Name:", thing.name, "Description:", thing.description, "Value:", thing.value, "Weight:", thing.weight)
            else:
                print("Name:", thing.name, "Description:", thing.description, "Value: Nothing", "Weight:", thing.weight)

    def damage(self, damage):
        self.health -= damage

    def heal(self, heal):
        self.health += heal
        if self.health > 100:
            self.health = 100

    def is_dead(self):
        if self.health <= 0:
            return True
        else:
            return False

    def is_in_room(self, room):
        if self.room.name == room:
            return True
        else:
            return False

    def has_item(self, item):
        for thing in self.things:
            if thing.name.strip().lower() == item.strip().lower():
                return True
        return False


class Room(ThingHolder):
    def __init__(self, name, description, n, s, w, e, things):
        super().__init__(name, description, things)
        self.n = n
        self.s = s
        self.w = w
        self.e = e

    def is_haunted(self):
        return False

    def is_shop(self):
        return False


class HauntedRoom(Room):
    def __init__(self, name, description, n, s, w, e, things, ghost):
        super().__init__(name, description, n, s, w, e, things)
        self.ghost = ghost

    def ghost_scan(self):
        print("There is a ghost in this room")
        print("Its name is:", self.ghost.name)
        print("It says", self.ghost.message)
        print("The ghost does", self.ghost.damage, "damage")
        return self.ghost.damage

    def remove_ghost(self):
        self.ghost = None

    def is_haunted(self):
        if self.ghost is not None:
            return True
        return False


class ShopRoom(Room):
    def __init__(self, name, description, n, s, w, e, things):
        super().__init__(name, description, n, s, w, e, things)

    def is_shop(self):
        return True

    def shop(self, money, items):
        print("Welcome to the shop")
        print("Buy or sell?")
        choice = input("")
        if choice == "buy":
            print("What would you like to buy?")
            for thing in self.things:
                print("-", thing.name, thing.value)
            choice = input("").strip().lower()
            for thing in self.things:
                if thing.name.strip().lower().startswith(choice):
                    if money >= thing.value:
                        print("You bought", thing.name)
                        self.remove(thing)
                        money -= thing.value
                        return thing, money, False
                    else:
                        print("You don't have enough money")
                        return "Nothing", money, False
        elif choice == "sell":
            print("What would you like to sell?")
            for thing in items:
                print("-", thing.name, thing.value)
            choice = input("").strip().lower()
            for thing in items:
                if thing.name.strip().lower().startswith(choice):
                    print("You sold", thing.name)
                    self.add(thing)
                    money += thing.value
                    return thing, money, True
                    break
            print("You don't have that")
        return "Nothing", money, False


class Ghost(Thing):
    def __init__(self, name, description, message, damage):
        super().__init__(name, description)
        self.message = message
        self.damage = damage


# generate random treasures from a list of treasures
def generate_treasures(treasures):
    new_treasures = []
    for i in range(random.randint(0, 3)):
        new_treasures.append(treasures[random.randint(1, len(treasures)-1)])
    # Remove duplicate treasures so there is only one of each
    new_treasures = list(dict.fromkeys(new_treasures))
    return new_treasures


def generate_ghost_drops(treasures):
    drops = []
    for i in range(random.randint(1, 3)):
        drops.append(treasures[random.randint(1, len(treasures)-1)])
    return drops


def generate_ghost(ghosts):
    return ghosts[random.randint(1, len(ghosts)-1)]


def where(player):
    print(player.room.name)
    print(player.room.description)
    print("Places You Can Go:")
    player.doors()
    player.room.get_things()


def main():
    game_over = False
    # Game Initialisation
    ghosts = [
        Ghost("Steve", "It's a ghost", "Ayeup mate", 10),
        Ghost("Satan", "It's a ghost", "You shouldn't of come here!", 90),
        Ghost("Dave", "It's a ghost", "I'm bald", 72)
    ]

    treasures = [
        # Bad items
        Treasure("T-Shirt", "Has a hole in it", 1, 1),
        Treasure("Wheel chair", "It's broken", 1, 8),
        Treasure("Stapler", "There is no staples", 1, 2),
        Treasure("Pen", "There is no ink in it", 1, 1),
        Treasure("Hat", "Its very tiny", 1, 1),
        Treasure("Football", "Its deflated", 2, 1),
        # Good items
        Treasure("Bag", "It's full of money", 25, 4),
        Treasure("Guitar", "One of the strings are snapped but still works", 30, 6),
        Treasure("Boots", "They are very comfortable", 10, 2),
        Treasure("Titanic photos", "They're very old", 50, 1),
    ]

    shop_items = [
        Treasure("Torch", "Use command 'light' to see in the basement", 10, 2),
        Treasure("EMF detector", "Use command 'scan' to look for ghosts", 100, 1),
        Treasure("Potion", "Use command 'drink' to heal", 10, 1),
    ]

    ghost_drops = [
        Treasure("Ectoplasm", "It's a ghost's ectoplasm", 50, 0),
        Treasure("Slime", "It's a ghost's slime", 1, 1),
        Treasure("Soul", "You can hear it screaming", 50, 0),
    ]

    rooms = [
        Room("Outside", "Very Dark", 1, 7, -1, 2, []),
        Room("Entrance", "There is a dimly lit light bulb. Nothing else.", 3, 0, 4, -1, generate_treasures(treasures)),
        HauntedRoom("Green House", "Its very green", 8, -1, 0, -1, generate_treasures(treasures), generate_ghost(ghosts)),
        Room("Hall", "The hall is extremely long", 5, 1, -1, 8, generate_treasures(treasures)),
        Room("Basement", "It's extremely dark, you need to turn on a light", -1, -1, -1, 1, generate_treasures(treasures)),
        Room("Living Room", "It's super cozy in here surprisingly", -1, 3, -1, -1, generate_treasures(treasures)),
        HauntedRoom("Satanic Room", "It's a room filled with a lot of dead bodies", -1, -1, -1, 4, generate_treasures(treasures), ghosts[1]),
        ShopRoom("Shop", "It's a shop", 0, -1, -1, -1, shop_items),
        Room("Conservatory", "Its very cold", -1, 2, 3, -1, generate_treasures(treasures))
    ]

    player = Player("Player", "You are a player", [], rooms[0])
    # Main Game Loop
    while not game_over:
        item_found = False
        command = input(">>> ").strip().lower()
        if command == "look":
            where(player)

        elif command == "n":
            player.move(rooms, "n")

        elif command == "s":
            player.move(rooms, "s")

        elif command == "w":
            player.move(rooms, "w")

        elif command == "e":
            player.move(rooms, "e")

        elif command == "pick up":
            if not player.room.is_shop():
                item = input("What do you want to pick up? ").strip().lower()
                for thing in player.room.things:
                    if thing.name.strip().lower().startswith(item):
                        player.add(thing)
                        player.room.remove(thing)
                        print("You picked up " + thing.name)
                        break
            else:
                print("You can't pick up anything in a shop")

        elif command == "drop":
            if not player.room.is_shop():
                item = input("What do you want to drop? ").strip().lower()
                for thing in player.things:
                    if thing.name.strip().lower().startswith(item):
                        player.room.add(thing)
                        player.remove(thing)
                        print("You dropped " + thing.name)
                        break
            else:
                print("You can't drop anything in a shop")

        elif command == "inventory":
            player.get_things()

        elif command == "light":
            if player.is_in_room("Basement"):
                if player.has_item("Torch"):
                    player.room.w = 6
                    player.room.description = "The room is no longer dark"
                    print("You shine your torch\nYou can see now")
                else:
                    print("You don't have a torch")
            else:
                print("You can't do that")

        elif command == "health":
            print("Your health is:", player.health)

        elif command == "scan":
            if player.has_item("EMF detector"):
                if player.room.is_haunted():
                    player.damage(player.room.ghost_scan())
                    for i in generate_ghost_drops(ghost_drops):
                        player.add(i)
                        print("You received a " + i.name)
                    player.room.remove_ghost()
                else:
                    print("There is no ghost in this room")
            else:
                print("You don't have an EMF detector")
        elif command == "drink":
            if player.has_item("Potion"):
                player.heal(100)
                for thing in player.things:
                    if thing.name == "Potion":
                        player.remove(thing)
                        print("You drank a potion")
                        print("Your health is:", player.health)
                        break
        elif command == "shop":
            if player.room.is_shop():
                new_item, new_money, sell = player.room.shop(player.money, player.things)
                if new_item != "Nothing" and sell == False:
                    player.add(new_item)
                    player.money = new_money
                elif new_item != "Nothing" and sell == True:
                    player.remove(new_item)
                    player.money = new_money
                else:
                    player.money = new_money
            else:
                print("You can't do that")
        elif command == "money":
            print("You have", player.money, "money")
        elif command == "help":
            print("""
            You can use the following commands:
            where - shows you where you are
            n - moves you north
            s - moves you south
            w - moves you west
            e - moves you east
            pick up - picks up an item
            drop - drops an item
            inventory - shows you your inventory
            light - turns on your torch
            health - shows you your health
            scan - scans for ghosts
            drink - heals you
            shop - opens the shop
            money - shows you your money
            help - shows this help message
            """)
        else:
            print("Not A Valid Command")

        print("\n")
        if player.is_dead():
            print("You died")
            input("Press enter to exit...")
            game_over = True


main()
