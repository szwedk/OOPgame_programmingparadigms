import time

rooms = {
    'Home': {'West': 'Garage'},
    'Garage': {'East': 'Home', 'South': 'Store'},
    'Store': {'North': 'Garage', 'East': 'Junkyard'},
    'Junkyard': {'West': 'Store'},
}

class Location:
    def __init__(self, description, north=None, south=None, east=None, west=None):
        self.description = description
        self.north = north
        self.south = south
        self.east = east
        self.west = west


home = Location("You are in your cozy home.")
garage = Location("You enter the garage and see a car with its hood up.")
store = Location("You are inside a store full of car parts and tools.")
junkyard = Location("You find yourself in a junkyard filled with old car parts and rusty machinery.")

class Player:
    def __init__(self, name):
        self.name = name
        self.inventory = []

    def add_inventory(self, item):
        self.inventory.append(item)

class Car:
    def __init__(self):
        self.parts = []
        self.tools = []
        self.engine = Engine()

    def show_status(self):
        print("The car has a bad engine and is missing some parts.")
        print("Current parts: " + ", ".join(self.parts))
        print("Current tools: " + ", ".join(self.tools))

    def add_tool(self, tool):
        self.tools.append(tool)

    def add_part(self, part):
        self.parts.append(part)

    def fix_engine(self):
        if "Wrench" not in self.tools:
            print("You can't fix the engine without a wrench!")
            return

        if "Spark Plug" not in self.parts:
            print("You can't fix the engine without a spark plug!")
            return

        self.engine.fix()

    def drive(self):
        if not self.engine.is_fixed:
            print("The car won't start without a working engine.")
            return

        print("You start the car and take it for a spin. The engine sounds great!")


class Engine:
    def __init__(self):
        self.is_fixed = False

    def fix(self):
        print("You use the wrench and spark plug to fix the engine.")
        time.sleep(1)
        print("The engine is now fixed!")
        self.is_fixed = True


class Game:
    def __init__(self, player):
        self.player = player
        self.car = Car()
        self.inventory = []
        self.current_location = home

    def move(self, direction):
        if direction == 'North':
            next_location = rooms[self.current_location.description][direction]
            self.current_location = next_location
        elif direction == 'South':
            next_location = rooms[self.current_location.description][direction]
            self.current_location = next_location
        elif direction == 'East':
            next_location = rooms[self.current_location.description][direction]
            self.current_location = next_location
        elif direction == 'West':
            next_location = rooms[self.current_location.description][direction]
            self.current_location = next_location
        else:
            print("Invalid direction.")


    def game_loop(self):
        commands = "search | fix engine | drive | move | inventory | exit"
        while True:
            print(self.current_location.description)
            command = input(f"\nWhat would you like to do? \n {commands}\n")
            if command == "search":
                self.search()
            elif command == "fix engine":
                self.car.fix_engine()
            elif command == "drive":
                self.car.drive()
            elif command == "move":
                direction = input("Which direction do you want to move? (North, South, East, West) ")
                self.move(direction)
            elif command == "inventory":
                print("Inventory: " + ", ".join(self.player.inventory))
            elif command == "exit":
                print("Thanks for playing!")
                break
            else:
                print("I don't understand that command.")

    def search(self):
        if self.current_location == garage:
            print("You search the garage and find some tools and spare parts.")
            self.car.add_tool("Wrench")
            time.sleep(1)
        elif self.current_location == store:
            print("You search the store and find some useful items.")
            self.player.add_inventory("Screwdriver")
            time.sleep(1)
        elif self.current_location == junkyard:
            print("You search the junkyard and find some useful parts.")
            self.car.add_part("Spark Plug")
            time.sleep(1)
        else:
            print("There is nothing to search here.")

if __name__ == "__main__":
    print("Welcome to the car repair game!")
    print("Let's start with your name: \n")
    name = input()
    time.sleep(1)
    print("Good luck, " + name + ".\n")
    time.sleep(1)
    print("Starting game...\n")
    time.sleep(3)
    player = Player(name)
    game = Game(player)
    game.game_loop()

