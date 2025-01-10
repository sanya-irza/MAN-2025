import pygame
import const
import calculation
from classes import *
from datetime import datetime



def draw_cell(cell: Cell, screen):
    x = cell.x * const.CELL_SIZE
    y = cell.y * const.CELL_SIZE

    pygame.draw.rect(screen, const.WAY_CELL_COLOR, (x, y, const.CELL_SIZE, const.CELL_SIZE))
    
    if cell.visited:
        pygame.draw.rect(screen, const.VISITED_CELL_COLOR, (x, y, const.CELL_SIZE, const.CELL_SIZE))
        
    if cell.way:
        pygame.draw.rect(screen, const.WAY_CELL_COLOR, (x, y, const.CELL_SIZE, const.CELL_SIZE))

    if cell.current:
        pygame.draw.rect(screen, const.CURRENT_CELL_COLOR, (x, y, const.CELL_SIZE, const.CELL_SIZE))

    if cell.walls[CellSide.top]:
        pygame.draw.line(screen,const.WALL_LINE_COLOR,(x, y), (x + const.CELL_SIZE, y), const.WALL_LINE_THICKNESS)
    if cell.walls[CellSide.bottom]:
        pygame.draw.line(screen,const.WALL_LINE_COLOR,(x, y + const.CELL_SIZE), (x + const.CELL_SIZE, y + const.CELL_SIZE), const.WALL_LINE_THICKNESS)
    if cell.walls[CellSide.left]:
        pygame.draw.line(screen,const.WALL_LINE_COLOR,(x, y), (x, y + const.CELL_SIZE), const.WALL_LINE_THICKNESS)
    if cell.walls[CellSide.right]:
        pygame.draw.line(screen,const.WALL_LINE_COLOR,(x + const.CELL_SIZE, y), (x + const.CELL_SIZE, y + const.CELL_SIZE), const.WALL_LINE_THICKNESS)
        
def draw_cells(screen):
    for cell in calculation.grid:
        draw_cell(cell, screen)
    pygame.display.flip()
    
def save_image(screen):
    image_name = f'image_{datetime.now().time()}'.replace(':', '_').replace('.', '_') + '.jpg' 
    pygame.image.save(screen, image_name)