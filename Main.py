from time import sleep
import sys
import os
game_over = False

class Thing:

  
  def __init__(self, name, description):
    self.name = name
    self.description = description


class Room(Thing):

  
  def __init__(self, name, description, n, s, w, e):
    super().__init__(name, description)
    self.n = n
    self.s = s
    self.w = w
    self.e = e


class Player(Thing):

  
  def __init__(self, name, description, room):
    super().__init__(name, description)
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
      typing_effect("You Can't Go There")


  def doors(self, rooms):
    if self.room.n != -1:
      typing_effect("North")
    if self.room.s != -1:
      typing_effect("South")
    if self.room.w != -1:
      typing_effect("West")
    if self.room.e != -1:
      typing_effect("East")
      

def typing_effect(text):
    for char in text:
        sleep(0.05)
        sys.stdout.write(char)
        sys.stdout.flush()
    sys.stdout.write("\n")
    sys.stdout.flush()
      
def main(name):
  os.system("cls")
  
  #Game Initialisation
  command = ""
  rooms = [
    Room("Outside", "It is very dark", 1, -1, -1, -1),
    Room("Reception", "For a reception it isn't very welcoming.", -1, 0, -1, 2),
    Room("Hallway", "It's a very long passage.", 3, -1, 1, -1),
    Room("Conference Room","The room is rusty, crusty and dusty",-1, 2, -1, -1)
  ]
  player = Player(name, "player", rooms[0])

  typing_effect(
  """
  COMMANDS:
  • Help
  • Where
  • N/S/W/E 
  """
  )
  
  #Main Game Loop
  while command != "q" and not game_over:
      command = input(">>> ").strip().lower()
      os.system("cls")
      if command == "where":
        typing_effect(f"Your location is {player.room.name}")
        typing_effect(player.room.description)
        typing_effect("Places You Can Go:")
        player.doors(rooms)
      elif command == "help":
          typing_effect(
        """
        COMMANDS:
        • Help
        • Where
        • N/S/W/E 
        """
        )
      elif command == "n":
        player.move(rooms, "n")
        typing_effect("You Moved North")
      elif command == "s":
        player.move(rooms, "s")
        typing_effect("You Moved South")
      elif command == "w":
        player.move(rooms, "w")
        typing_effect("You Moved West")
      elif command == "e":
        player.move(rooms, "e")
        typing_effect("You Moved East")
      elif command == "q":
        typing_effect("You Have Quit. Saving...")
      else:
        typing_effect("That isn't a command.")

        
      
    





