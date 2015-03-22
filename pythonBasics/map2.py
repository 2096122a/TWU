from tile import Tile
from player import Player
import random
from map import *

class Mapmove:



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


    