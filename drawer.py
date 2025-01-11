import pygame
import const
import settings
import calculation
from classes import *
from datetime import datetime 



def draw_cell(cell: Cell, screen):
    
    x = cell.x * settings.cell_size() + settings.x_offset()
    y = cell.y * settings.cell_size() + settings.y_offset()

    pygame.draw.rect(screen, const.WAY_CELL_COLOR, (x, y, settings.cell_size(), settings.cell_size()))
    
    if cell.visited:
        pygame.draw.rect(screen, const.VISITED_CELL_COLOR, (x, y, settings.cell_size(), settings.cell_size()))
        
    if cell.way:
        pygame.draw.rect(screen, const.WAY_CELL_COLOR, (x, y, settings.cell_size(), settings.cell_size()))

    if cell.current:
        pygame.draw.rect(screen, const.CURRENT_CELL_COLOR, (x, y, settings.cell_size(), settings.cell_size()))

    if cell.walls[CellSide.top]:
        pygame.draw.line(screen,const.WALL_LINE_COLOR,(x, y), (x + settings.cell_size(), y), const.WALL_LINE_THICKNESS)
    if cell.walls[CellSide.bottom]:
        pygame.draw.line(screen,const.WALL_LINE_COLOR,(x, y + settings.cell_size()), (x + settings.cell_size(), y + settings.cell_size()), const.WALL_LINE_THICKNESS)
    if cell.walls[CellSide.left]:
        pygame.draw.line(screen,const.WALL_LINE_COLOR,(x, y), (x, y + settings.cell_size()), const.WALL_LINE_THICKNESS)
    if cell.walls[CellSide.right]:
        pygame.draw.line(screen,const.WALL_LINE_COLOR,(x + settings.cell_size(), y), (x + settings.cell_size(), y + settings.cell_size()), const.WALL_LINE_THICKNESS)
        
def draw_cells(screen):
    screen.fill(const.WAY_CELL_COLOR)
    for cell in calculation.grid:
        draw_cell(cell, screen)
    pygame.display.flip()
    
    
# def save_image(screen):
#     image_name = f'image_{datetime.now().time()}'.replace(':', '_').replace('.', '_') + '.jpg' 
#     pygame.image.save(screen, image_name)