'''
Project: Car Repair Game
Programmers: Kamil Szwed, Antan Nguyen
Date: 2023-04-24
Description: A text-based game where the player must find the tools and parts to fix a car. 
    The player can move between locations, search for items, and fix the car's engine. 
    The player wins the game by fixing the car and driving it. 
Attachments: UML Diagram, doc_strings for each class.
'''


import time
import random

map = """ 
         [Bathroom]
            ^
            |
            v
[Garage]--->[Home]
    ^
    |
    v
[Store]<--->[Junkyard]

"""

class Location:
    def __init__(self, description, north=None, south=None, east=None, west=None):
        self.description = description
        self.north = north
        self.south = south
        self.east = east
        self.west = west

home = Location("\nYou are in your humble aboade.")
garage = Location("\nYou enter the garage and see a car with its hood up.")
store = Location("\nYoure inside a store full of tools.")
junkyard = Location("\nYou made it to junkyard filled with parts.")
bathroom = Location("\nYoure in the bathroom, you should probably wash your hands.")

rooms = {
    home: {'West': garage, 'North': bathroom},
    garage: {'East': home, 'South': store},
    store: {'North': garage, 'East': junkyard},
    junkyard: {'West': store},
    bathroom: {'South': home}
}

class Player:
    def __init__(self, name, dead=False, map=[]):
        self.name = name
        self.dead = dead
        self.map = map
        self.inventory = []

    def add_inventory(self, item):
        self.inventory.append(item)

    def add_map(self):
        self.map.append(map)

    def is_maybe_dead(self):
        if random.randint(1, 100) == 69: #nice
            self.dead = True
        else:
            self.dead = False

class Car:
    """Represents the car that needs to be repaired in the game.
    Attributes
        tools: list of tools for the repair
        engine: car engine object
        parts: list of car parts for the repair
    """
    def __init__(self):
        self.parts = []
        self.tools = []
        self.treasure_map = []
        self.engine = Engine()

    def add_tool(self, tool):
        self.tools.append(tool)

    def add_part(self, part):
        self.parts.append(part)

    def add_treasure_map(self, treasure_map):
        self.treasure_map.append(treasure_map)

    def open_treasure_map(self):
        if "map" not in self.treasure_map:
            print("\nYou don't have a treasure map!")
            return
        else:
            print(map)

    def fix_engine(self):
        if "Wrench" not in self.tools:
            print("\nYou can't fix the engine without a wrench!")
            return

        if "Spark Plug" not in self.parts:
            print("\nYou can't fix the engine without a spark plug!")
            return

        self.engine.fix()

    def drive(self):
        if not self.engine.is_fixed:
            print("\nThe car won't start without a working engine.")
            return

        print("\nYou start the car and take it for a spin. The engine sounds great!\n VROOOOOOM VROOOOOOM\nVROOOOOOOOOOOOOM\nzoom zoom zoom\n")

class Engine:
    def __init__(self):
        self.is_fixed = False

    def fix(self):
        print("\nYou use the wrench and spark plug to fix the engine.")
        time.sleep(1)
        print("The engine is now fixed!")
        self.is_fixed = True

class Game:
    """Manages the game state and main game loop.
    Attributes:
        player: player object
        car: car object
        inventory: list of items the player has collected
        current_location: players current location object
    """
    def __init__(self, player):
        self.player = player
        self.car = Car()
        self.inventory = []
        self.current_location = home

    def move(self, direction):
        try:
            next_location = rooms[self.current_location][direction]
            self.current_location = next_location
        except KeyError:
            print("You can't go in that direction.")

    def game_loop(self):
        commands = "search | fix engine | drive | move | inventory | map |exit"
        while True:
            print(self.current_location.description)
            command = input(f"\nWhat would you like to do? \n {commands}\n").lower()
            if command == "search":
                self.search()
            elif command == "fix engine":
                self.car.fix_engine()
            elif command == "drive":
                self.car.drive()
            elif command == "move":
                direction = input("\nWhich direction do you want to move? (North, South, East, West) ")
                self.move(direction.capitalize())
            elif command == "inventory":
                print("\nInventory: " + ", ".join(self.player.inventory))
            elif command == "map":
                self.car.open_treasure_map()
            elif command == "exit":
                print("\nThanks for playing!")
                break
            else:
                print("\nI don't understand that command.")

            self.player.is_maybe_dead()  
            if self.player.dead:
                print("\nYou died! Game over.")
                break

    def search(self):
        if self.current_location == garage:
            print("You search the garage and find a Milwakee wrench, you think to yourself, damn i didnt know i could afford that.")
            self.car.add_tool("Wrench")
            self.player.add_inventory("Wrench")
            time.sleep(1)
        elif self.current_location == store:
            print("You search the store, definintly didnt rob it, unfortunatly you didnt find anything useful.")
            self.player.add_inventory("Screwdriver")
            time.sleep(1)
        elif self.current_location == junkyard:
            print("You miraculously found a spark plug, you know what they say! \none mans trash is another mans treasure.")
            self.car.add_part("Spark Plug")
            self.player.add_inventory("Spark Plug")
            time.sleep(1)
        elif self.current_location == bathroom:
            print("Gross, take your hand out of the toilet. Nice map though!")
            self.car.add_treasure_map("map")
            self.player.add_inventory("map")  # Add map to the player's inventory
            time.sleep(1)
        else:
            print("There is nothing to search here.")

if __name__ == "__main__":
    print("\nWelcome to the car repair game!")
    time.sleep(1)
    print("Your objective is to find the tools and parts to fix the car.")
    time.sleep(2)
    name = input(("Let's start with your name: \n"))
    time.sleep(1)
    car = input((f"{name}, whats your favorite car? \n"))
    time.sleep(1)
    print(f"Good luck, {name}. Go drive your {car}.\n Its in the garage\n")
    time.sleep(1)
    print("Starting game...\n")
    time.sleep(3)
    player = Player(name)
    game = Game(player)
    game.game_loop()

