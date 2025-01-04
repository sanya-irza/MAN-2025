import calculation 
import random
import enum

class CellSide(enum.Enum):
    left =1
    right = 2
    top = 3
    bottom = 4

class Cell:
    def __init__(self, x, y):
        self.x, self.y = x, y
        self.visited = False
        self.current = False
        self.way = False

        self.walls = {
            CellSide.left: True, 
            CellSide.right: True,
            CellSide.top: True,
            CellSide.bottom: True
            }
        
    def rand_neighbour(self):
        neighbours = []

        neighbour = calculation.check_cell(self.x - 1, self.y)
        if neighbour != None:
            neighbours.append(neighbour)
            
        neighbour = calculation.check_cell(self.x + 1, self.y)
        if neighbour != None:
            neighbours.append(neighbour)
            
        neighbour = calculation.check_cell(self.x, self.y + 1)       
        if neighbour != None:
            neighbours.append(neighbour)
            
        neighbour = calculation.check_cell(self.x, self.y - 1)
        if neighbour != None:
            neighbours.append(neighbour)
            
        if not neighbours:
            return None
        else:
            return random.choice(neighbours)
        