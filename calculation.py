import const
from classes import *
import drawer
import random
import pygame


rand_pos = random.randint(0, const.MAZE_HEIGHT * const.MAZE_WIDTH)

grid = []
visited = []

for y in range(const.MAZE_HEIGHT):
    for x in range(const.MAZE_WIDTH):
        grid.append(Cell(x,y))

def check_cell(x,y):
    index = y * const.MAZE_WIDTH + x

    if x >= const.MAZE_WIDTH or x < 0 or y >= const.MAZE_HEIGHT or y < 0 or grid[index].visited:
        return None
    else:
        return(grid[index])
    
def break_wall(next_cell, current_cell):
    if current_cell.x + 1 == next_cell.x:
        current_cell.walls[CellSide.right] = False
        next_cell.walls[CellSide.left] = False
        
    if current_cell.x - 1 == next_cell.x:
        current_cell.walls[CellSide.left] = False
        next_cell.walls[CellSide.right] = False
        
    if current_cell.y + 1 == next_cell.y:
        current_cell.walls[CellSide.bottom] = False
        next_cell.walls[CellSide.top] = False
        
    if current_cell.y - 1 == next_cell.y:
        current_cell.walls[CellSide.top] = False
        next_cell.walls[CellSide.bottom] = False
    
def prepare_maze():
    clock = pygame.time.Clock()
    CurrentCell = grid[rand_pos]
    
    while True:
        NextCell = CurrentCell.rand_neighbour()

        CurrentCell.current = False
        CurrentCell.visited = True
        
        visited.append(CurrentCell)
        
        if NextCell == None:
            while CurrentCell.rand_neighbour() == None:
                CurrentCell.way = True
                visited.pop()
                
                if len(visited) == 0:
                    break
                
                NextCell = visited[len(visited) - 1]
                break_wall(NextCell, CurrentCell)
                CurrentCell = NextCell      
        else:
            break_wall(NextCell, CurrentCell)
            CurrentCell = NextCell
            CurrentCell.current = True
        
        drawer.draw_cells()
        
        if len(visited) == 0:
            break
        
        clock.tick(const.CLOCK_TICK)
        
        
        
        
    