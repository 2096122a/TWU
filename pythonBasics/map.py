from tile import Tile
class Map:

    def __init__(self,size):
        self.matrix = [[Tile() for i in range(size)] for j in range(size)]
        for i in range(size):
            self.matrix[0][i].uncover()
            self.matrix[i][0].uncover()
            self.matrix[size-1][i].uncover()
            self.matrix[i][size-1].uncover()
        self.matrix[size/2][size/2].generate([True,True,True,True])
        self.player_pos = [size/2,size/2]


    def print_matrix(self):
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[i])):
                to_print = "0"
                if int(str(self.matrix[i][j])) < 10:
                    to_print = to_print + str(self.matrix[i][j])
                else:
                    to_print = str(self.matrix[i][j])
                if self.player_pos == [i,j]:
                    to_print = to_print + "p"
                print to_print,
            print ""


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
        

    
mapp = Map(7)
mapp.print_matrix()
command = ""
while (command != "quit"):
    command = raw_input("Enter a command: ")
    mapp.move_player(command)
    mapp.print_matrix()
