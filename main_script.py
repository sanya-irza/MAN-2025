import pygame
import random as rand

Height = 10
Width = 10

Size = 70
wallWidth = 2

SChight = Height * Size
SCwidth = Width * Size

randPos = rand.randint(0, Height * Width)

pygame.init()
screen = pygame.display.set_mode((SCwidth, SChight))
clock = pygame.time.Clock()
running = True

class Cell:
    def __init__(self, x, y):
        self.x, self.y = x, y
        self.visited = False
        self.current = False
        self.way = False

        self.walls = {
            "top": True, 
            "bottom": True,
            "left": True,
            "right": True
            }
            
    def drawCell(self):
        x = self.x * Size
        y = self.y * Size

        if self.visited:
            pygame.draw.rect(screen, "darkolivegreen1", (x, y, Size, Size))
            
        if self.way:
            pygame.draw.rect(screen, "white", (x, y, Size, Size))

        if self.current:
            pygame.draw.rect(screen, "forestgreen", (x, y, Size, Size))

        if self.walls["top"]:
            pygame.draw.line(screen,"green",(x, y), (x + Size, y), wallWidth)
        if self.walls["bottom"]:
            pygame.draw.line(screen,"green",(x, y + Size), (x + Size, y + Size), wallWidth)
        if self.walls["left"]:
            pygame.draw.line(screen,"green",(x, y), (x, y + Size), wallWidth)
        if self.walls["right"]:
            pygame.draw.line(screen,"green",(x + Size, y), (x + Size, y + Size), wallWidth)

    def randNeighbour(self):
        Neighbours = []

        if checkCell(self.x - 1, self.y):
             Neighbours.append(checkCell(self.x - 1, self.y))
        if checkCell(self.x + 1, self.y):
             Neighbours.append(checkCell(self.x + 1, self.y))
        if checkCell(self.x, self.y + 1):
             Neighbours.append(checkCell(self.x, self.y + 1))
        if checkCell(self.x, self.y - 1):
             Neighbours.append(checkCell(self.x, self.y - 1))
        if not Neighbours:
            return None
        else:
            return rand.choice(Neighbours)

def drawCells():
    for cell in grid:
        cell.drawCell()   

grid = []
visited = []

def checkCell(x,y):
    index = y * Width + x

    if x >= Width or x < 0 or y >= Height or y < 0 or grid[index].visited:
        return False
    else:
        return(grid[index])

for y in range(Height):
    for x in range(Width):
        grid.append(Cell(x,y))


CurrentCell = grid[randPos]
CurrentCell.current = True

while running:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    screen.fill('white')
            
    NextCell = CurrentCell.randNeighbour()

    CurrentCell.current = False
    CurrentCell.visited = True
    
    visited.append(CurrentCell)
    
    if NextCell == None:
        while CurrentCell.randNeighbour() == None:
            CurrentCell.way = True
            visited.pop()
            if len(visited) == 0:
                
                break
            CurrentCell = visited[len(visited) - 1]       
    else:
        CurrentCell = NextCell     
        
    
    CurrentCell.current = True
    
    drawCells()
    
    pygame.display.flip()
 
    clock.tick(30)
    
pygame.quit()




    # screen.fill("white")
    # if CurrentCell == None:
    #     CurrentCell = visited.pop()
    # else:
    #     visited.append(CurrentCell)

    # CurrentCell.visited = True
    # CurrentCell.current = False
    # PrevCell = CurrentCell
    # CurrentCell = CurrentCell.randNeighbour()
    
    # if CurrentCell == None:
    #     PrevCell.visited = False
    #     drawCells()
    #     continue
    
    # CurrentCell.current = True