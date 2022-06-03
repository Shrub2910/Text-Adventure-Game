from time import sleep
game_over = False
import os
class Thing:
  def __init__(self, name, description):
    self.name = name
    self.description = description
  
class Player:
  def __init__(self, room):
    self.room = room

  def move(self, Rooms, direction):
    if direction == "n" and self.room.n != -1:
      self.room = Rooms[self.room.n]
    elif direction == "s" and self.room.s != -1:
      self.room = Rooms[self.room.s]
    elif direction == "w" and self.room.w != -1:
      self.room = Rooms[self.room.w]
    elif direction == "e" and self.room.e != -1:
      self.room = Rooms[self.room.e]
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
    
class Room(Thing):
  def __init__(self, name, description,n, s, w, e):
    super().__init__(name, description)
    self.n = n
    self.s = s
    self.w = w
    self.e = e


def main():
  #Game Initialisation
  Rooms = [
    Room("Outside", "Very Dark", 1, -1, -1, 2),
    Room("Entrance", "There is a dimly lit light bulb. Nothing else.", 3, 0, 4, -1),
    Room("Green House", "Its very green", -1, -1, 0, -1),
    Room("Hall", "The hall is extremely long", 5, 1, -1, -1),
    Room("Basement", "It's extremely dark, you need to turn on a light", -1, -1, -1, 1),
    Room("Living Room", "It's super cozy in here suprisingly", -1, 3, -1, -1)
  ]
  player = Player(Rooms[0])
  #Main Game Loop
  while not game_over:
    command = input(">>> ").strip().lower()
    os.system("cls")
    if command == "where":
      print(player.room.name)
      print(player.room.description)
      print("Places You Can Go:")
      player.doors()
      
    elif command == "n":
      player.move(Rooms, "n")
    elif command == "s":
      player.move(Rooms, "s")
    elif command == "w":
      player.move(Rooms, "w")
    elif command == "e":
      player.move(Rooms, "e")
    else:
      print("ERROR")

main()
  
