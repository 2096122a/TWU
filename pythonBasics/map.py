from tile import Tile
class Map:

    def __init__(self,size):
        self.matrix = [[Tile() for i in range(size)] for j in range(size)]
        for i in range(size):
            self.matrix[0][i].uncover()
            self.matrix[i][0].uncover()
            self.matrix[size-1][i].uncover()
            self.matrix[i][size-1].uncover()
        self.matrix[size/2][size/2].make_crossroads()
        self.player_position = [size/2,size/2]


    def print_matrix(self):
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[i])):
                to_print = "0"
                if int(str(self.matrix[i][j])) < 10:
                    to_print = to_print + str(self.matrix[i][j])
                else:
                    to_print = str(self.matrix[i][j])
                if self.player_position == [i,j]:
                    to_print = to_print + "p"
                print to_print,
            print ""

    def move_player(self,direction):
        size = len(self.matrix)
        if direction == "up":
            if self.player_position[0]>1:
                self.player_position[0]-=1
        if direction == "down":
            if self.player_position[0]<size-2:
                self.player_position[0]+=1
        if direction == "left":
            if self.player_position[1]>1:
                self.player_position[1]-=1
        if direction == "right":
            if self.player_position[1]<size-2:
                self.player_position[1]+=1


mapp = Map(7)
mapp.print_matrix()
command = ""
while (command != "quit"):
    command = raw_input("Enter a command: ")
    mapp.move_player(command)
    mapp.print_matrix()
