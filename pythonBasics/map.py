from tile import Tile
class Map:

    def __init__(self,size):
        self.matrix = [[Tile() for i in range(size)] for j in range(size)]
        for i in range(size):
            self.matrix[0][i].uncovered = True
            self.matrix[i][0].uncovered = True
            self.matrix[size-1][i].uncovered = True
            self.matrix[i][size-1].uncovered = True


    def print_matrix(self):
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[i])):
                print self.matrix[i][j],
            print ""


Map(7).print_matrix()
