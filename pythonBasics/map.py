from tile import Tile
class Map:

    def __init__(self,size):
        self.matrix = [[Tile() for i in range(size)] for j in range(size)]

    def print_matrix(self):
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[i])):
                print self.matrix[i][j],
            print ""


Map(7).print_matrix()
