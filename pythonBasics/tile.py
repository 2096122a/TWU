class Tile:

    def __init__(self):
        self.up = False
        self.down = False
        self.right = False
        self.left = False
        self.uncovered = False

    def __str__(self):
        if self.uncovered:
            return "tu"
        else:
            return "tn"

    def uncover(self):
        self.uncovered = True

    
