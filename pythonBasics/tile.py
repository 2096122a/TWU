import random

class Tile:

    def __init__(self): # 0 == False == no connection
        self.up = False # 1 == True == connection exists
        self.down = False
        self.left = False
        self.right = False
        self.uncovered = False # False = tile has not been visited yet

    def __str__(self):
        if self.uncovered:
            return str(8*int(self.up)+4*int(self.down)+2*int(self.left)+int(self.right))
        else:
            return "16"

    def uncover(self):
        self.uncovered = True

    def generate(self,directions):
        print "called generate on ", directions
        for i in range(4):
            if directions[i] == None:
                directions[i] = (random.randint(1,3)<3)
        self.up = directions[0]
        self.down = directions[1]
        self.left = directions[2]
        self.right = directions[3]
        print "up= ", directions[0]
        print "down= ", directions[1]
        print "left= ", directions[2]
        print "right= ", directions[3]
        self.zombies = (random.randint(1,2))
        self.uncover()

