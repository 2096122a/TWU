class Tile:

    def __init__(self): # 0 == False == no connection
        self.up = False # 1 == True == connection exists
        self.down = False
        self.left = False
        self.right = False
        self.uncovered = False

    def __str__(self):
        if self.uncovered:
            return str(8*int(self.up)+4*int(self.down)+2*int(self.left)+int(self.right))
        else:
            return "16"

    def uncover(self):
        self.uncovered = True

    
