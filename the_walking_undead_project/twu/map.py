from tile import Tile
from player import Player
import random

class Map:

    def __init__(self,size):
        self.matrix = [[Tile() for i in range(size)] for j in range(size)]
        for i in range(size):
            self.matrix[0][i].uncover()
            self.matrix[i][0].uncover()
            self.matrix[size-1][i].uncover()
            self.matrix[i][size-1].uncover()
        self.matrix[size/2][size/2].generate([True,True,True,True])
        self.player = Player()
        self.player_pos = [size/2,size/2]


    def print_matrix(self):
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[i])):
                to_print = "0"
                if int(str(self.matrix[i][j])) < 10:
                    to_print = to_print + (self.matrix[i][j]).to_string()
                else:
                    to_print = (self.matrix[i][j]).to_string()
                if self.player_pos == [i,j]:
                    to_print = to_print + "p"
                print to_print,
            print ""
        print "Player: ", self.player.health
        print "Zombies at tile: ", self.get_current_tile().zombies


    def render(self):
        return [[(x).to_string() for x in row] for row in self.matrix]


    def move_player(self,direction):
        size = len(self.matrix)
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
            self.generate()


    def get_neighbours(self):
        return [ self.matrix[self.player_pos[0]-1][self.player_pos[1]], #up
                 self.matrix[self.player_pos[0]+1][self.player_pos[1]], #down
                 self.matrix[self.player_pos[0]][self.player_pos[1]-1], #left
                 self.matrix[self.player_pos[0]][self.player_pos[1]+1]  #right
                ]

    def get_current_tile(self):
        return self.matrix[self.player_pos[0]][self.player_pos[1]]


    def generate(self):
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
        self.get_current_tile().generate(directions)

    
    def kill_zombies(self, number):
        self.get_current_tile().zombies -= number


    def perform_attack(self, damage):
        if self.get_current_tile().zombies > 0:
            if self.player.ranged_used and self.player.bullets>0:
                self.player.bullets -= 1
                if damage >= self.player.ranged_power:
                    self.kill_zombies(1)
                    return 1
            else:
                if damage >= self.player.melee_power:
                    self.kill_zombies(1)
                    return 1

    def hurt_player(self):
        damage = 0
        for zombie in range(self.get_current_tile().zombies):
            if random.randint(1,3) < 3:
                damage += 1
        self.player.lose_health(damage)
        return damage
