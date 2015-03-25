import random

# Keeps a record of all of the information associated with each tile of the map
# i.e: connections available, whether tile is uncovered and number of zombies on that tile.
class Tile:

    # Instantiates a new non-uncovered tile with no zombies on it
    def __init__(self): # 0 == False == no connection
        self.up = False # 1 == True == connection exists
        self.down = False
        self.left = False
        self.right = False
        self.uncovered = False # False = tile has not been visited yet
        self.zombies = 0

    # Custom casts each tile to sting, used to represent map in HTML
    # Each tile is given a number between 0 and 15
    def __str__(self):
        if self.uncovered:
            return str(8*int(self.up)+4*int(self.down)+2*int(self.left)+int(self.right))
        else:
            return "16" # 'Escape code' for a non-uncovered tile

    def uncover(self):
        self.uncovered = True

    # Generates a new tile based on directions provided
    # Directions are an ordered list [UP,DOWN,LEFT,RIGHT]
    # If a direction is not specified (i.e. None) the connection is
    # randomly generated
    def generate(self,directions):
        for i in range(4):
            if directions[i] == None:
                directions[i] = (random.randint(1,3)<3) #66.(6)% chance to have a connection
        self.up = directions[0]
        self.down = directions[1]
        self.left = directions[2]
        self.right = directions[3]
        # Adds a random number of zombies on the newly generated tile
        self.zombies = (random.randint(1,2))
        self.uncover() # The tile is now uncovered
