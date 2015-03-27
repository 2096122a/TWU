from tile import Tile
from player import Player
import random

# Holds all of the informaton about the current game, i.e. the state of the map,
# the state of the player and the current position of the player on the map.
# The map also provides ability to be randomly generated
class Map:

    # Creates a new instance of the map object with a specified size.
    # Tiles at the end of the map are set to blank space. Player is
    # placed at the centre of the map, which is set to be a crossroads.
    def __init__(self,size):
        # create a new matrix to hold the tiles
        self.matrix = [[Tile() for i in range(size)] for j in range(size)]
        # set all the edges to blank space
        for i in range(size):
            self.matrix[0][i].uncover()
            self.matrix[i][0].uncover()
            self.matrix[size-1][i].uncover()
            self.matrix[i][size-1].uncover()
        # starting tile set to crossroads
        self.matrix[size/2][size/2].generate([True,True,True,True])
        # store data for a new player
        self.player = Player()
        self.player_pos = [size/2,size/2]

    # Provids the ability to randomly spawn zombies to increase the zombie horde
    def add_zombies(self):
        for row in self.matrix:
            for tile in row:
                # spawn zombies on other uncovered tiles
                if tile.uncovered and str(tile) != "0" and self.get_current_tile() != tile:
                    if random.randint(0,3) == 0:
                        tile.zombies+=1
                        
    # Provide the information stored in the map in an easily useable format
    def render(self):
        rendered = [[str(x) for x in row] for row in self.matrix]
        rendered[self.player_pos[0]][self.player_pos[1]] += "p"
        return rendered

    # Move the player around the map. If a tile has not been uncovered, a new
    # one is randomly generated. Player score is increased by 1000 points for
    # each tile. Zombies are added on each movement.
    def move_player(self,direction):
        size = len(self.matrix)
	self.add_zombies()
        if direction == "up":
            if self.player_pos[0]>1 and self.get_current_tile().up:
                self.player_pos[0]-=1
        if direction == "down":
            if self.player_pos[0]<size-2 and self.get_current_tile().down:
                self.player_pos[0]+=1
        if direction == "left":
            if self.player_pos[1]>1 and self.get_current_tile().left:
                self.player_pos[1]-=1
        if direction == "right":
            if self.player_pos[1]<size-2 and self.get_current_tile().right:
                self.player_pos[1]+=1
        if not self.matrix[self.player_pos[0]][self.player_pos[1]].uncovered:
            self.player.score += 1000
            self.generate()

    # Returns a list of the four neighbouring tiles in specified order
    def get_neighbours(self):
        return [ self.matrix[self.player_pos[0]-1][self.player_pos[1]], #up
                 self.matrix[self.player_pos[0]+1][self.player_pos[1]], #down
                 self.matrix[self.player_pos[0]][self.player_pos[1]-1], #left
                 self.matrix[self.player_pos[0]][self.player_pos[1]+1]  #right
                ]

    # Returns the tile that the player is currently on.
    def get_current_tile(self):
        return self.matrix[self.player_pos[0]][self.player_pos[1]]

    # Randomly generates the current tile, based on restrictions from neighbouring tiles
    def generate(self):
        # Get restrictions:
        tiles = self.get_neighbours()
        up = None
        down = None
        right = None
        left = None
        if tiles[0].uncovered:
            up = tiles[0].down
        if tiles[1].uncovered:
            down = tiles[1].up
        if tiles[2].uncovered:
            left = tiles[2].right
        if tiles[3].uncovered:
            right = tiles[3].left
        directions = [up,down,left,right]
        # pass restrictions onto function from the tile class
        self.get_current_tile().generate(directions)

    # Kill the given number of zombies on the current tile
    def kill_zombies(self, number):
        self.player.score += number*200
        self.get_current_tile().zombies -= number

    # Performs an attack with the damage supplied. If damage is large enough,
    # kills a zombie on the current tile
    def perform_attack(self, damage):
        # Are there any zombies?
        if self.get_current_tile().zombies > 0:
            # Using ranged weapon?
            if self.player.ranged_used:
                # Do we have bullets?
                if self.player.bullets>0:
                    # Use a bullet
                    self.player.bullets -= 1
                    # Perform attack
                    if int(damage) >= int(self.player.ranged_power):
                        self.kill_zombies(1)
                        return "You killed 1 zombies."
                    else:
                        return "You missed!"
                # Default to melee if no bullets
                else:
                    self.player.switch_active()
            else:
                # Perform melee attack
                if int(damage) >= int(self.player.melee_power):
                    self.kill_zombies(1)
                    return "You killed 1 zombies."
                else:
                    return "You missed!"
        # No zombies
        else:
            return "There are no zombies here"

    # Simulates the zombies trying to hurt the player
    def hurt_player(self):
        damage = 0
        # 33,(3)% chance to hit player per zombie
        for zombie in range(self.get_current_tile().zombies):
            if random.randint(1,3) < 3:
                damage += 1
        self.player.lose_health(damage)
        # Inform the player
        if damage > 0:
            return "The zombies hurt you for " + str(damage) + " damage."
        else:
            return "You took no damage."

    # How many zombies here?
    def tile_info(self):
        return "There are " + str(self.get_current_tile().zombies) + " zombies on this tile."
