# OOPgame_programmingparadigms


The Car Repair Game is a text-based adventure game about finding the tools and parts to fix a car, driving it, then winning the game. The game takes place at your humble abode, the goal being fixing your car in your garage, you must navigate through different locations to find tools and car parts to fix the car’s engine. Locations include your home, garage, the store, a junkyard, and THE bathroom. You move by typing the direction you want to go, each location has a description that gives the player an idea of what they can expect to find there. With many commands such as search, fix engine, drive, move, inventory, map, and exit, follow the given instructions in the game terminal to fix your car and drive your way to victory. Don’t die along the way… Good luck.


The game was built using 5 classes, Location, Player, Car, Engine, and Game. Each class has their specific attributes and behaviors. For example, Location has 5 attributes being the  cardinal directions and descriptions of locations. Player has 4 attributes being name, inventory, dead, and map, with behaviors of adding items to your inventory, the chance of potentially dying, and getting a map. Car has 4 attributes, parts, tools, engine, and treasure map. Car has 6 behaviors: adding tools and parts to your inventory, fixing the engine, driving the car, as well as adding the treasure map or opening the treasure map. Engine has 1 attribute and 1 behavior, in relation to checking if the car has been fixed and fixing the car respectively. Lastly, Game has 4 attributes, player, car, inventory, and current location with the behaviors being for the driver of the game and managing the game’s state and game loop.