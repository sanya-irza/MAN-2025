import os
import pygame
from const import *
from customtkinter import *
from tkinter import *
from calculation import prepare_maze
import settings

set_appearance_mode('dark')
set_default_color_theme('dark-blue')

root = Tk()
root.title('Labirynth Generator')
root.resizable(False, False)

generate_frame = Frame(
    root, 
    width = SCREEN_WIDTH, 
    height = SCREEN_HEIGHT
)
generate_frame.pack(side=LEFT)

gui_frame = CTkFrame(
    root, 
    height = SCREEN_HEIGHT,
    corner_radius=0
)
gui_frame.pack(side=RIGHT, fill=Y)

widgets_font = CTkFont(family='Cascadia Code', size=20)

os.environ['SDL_WINDOWID'] = str(generate_frame.winfo_id())
os.environ['SDL_VIDEODRIVER'] = 'windib'

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.init()

settings_frame = CTkFrame(gui_frame)
settings_frame.pack(side=TOP, fill=X, pady=10, padx=10)

settings_label = CTkLabel(
    settings_frame,
    text='Settings',
    font=widgets_font
)
settings_label.pack(side = TOP)


height_frame = CTkFrame(gui_frame)
height_frame.pack(side=TOP, fill=X, pady=5, padx=10)

height_label = CTkLabel(
    height_frame,
    text='Maze height: ',
    font=widgets_font
)
height_label.pack(side=TOP)

def get_height(value):
    height_label.configure(text=f'Maze height: {int(value)}')

height_scale = CTkSlider(
    height_frame,
    from_=5,
    to=100, 
    height=20,
    command=get_height,
    orientation=HORIZONTAL
)
height_scale.pack(side=TOP)

width_frame = CTkFrame(gui_frame)
width_frame.pack(side=TOP, fill=X, pady=5, padx=10)

width_label = CTkLabel(
    width_frame, 
    text='Maze width: ', 
    font=widgets_font
)
width_label.pack(side=TOP)

def get_width(value):
    width_label.configure(text=f'Maze width: {int(value)}')

width_scale = CTkSlider(
    width_frame,
    from_=5, 
    to=100, 
    height=20,
    command=get_width,
    orientation=HORIZONTAL
)
width_scale.pack(side=TOP)

speed_frame = CTkFrame(gui_frame)

speed_label = CTkLabel(
    speed_frame, 
    text='Generating Speed: ', 
    font=widgets_font
)
speed_label.pack(side=TOP)

def get_speed(value):
    speed_label.configure(text=f'Generating Speed: {int(value)}')
    
speed_scale = CTkSlider(
    speed_frame,
    from_=1, 
    to=100, 
    height=20,
    command=get_speed,
    orientation=HORIZONTAL
)
speed_scale.pack(side=TOP)

def stack(able):
    if able:
        speed_frame.pack_forget()
    else:
        speed_frame.pack(side=TOP, fill=X, pady=5, padx=10)
    
check_button = CTkCheckBox(
    gui_frame, 
    text='Instant appearance?', 
    offvalue=False, 
    onvalue=True,
    command=lambda:stack(check_button.get()),
    font=widgets_font
)

check_button.pack(side=TOP, pady=5, padx=10)
check_button.select()

copyright_frame = CTkFrame(
    gui_frame,
    fg_color='#212121'
)
copyright_frame.pack(side=BOTTOM, fill=X, padx=10)

copyright_label = CTkLabel(
    copyright_frame,
    text='© 2025 O. Irza. All rights reserved.',
    font= CTkFont(size=10)
)
copyright_label.pack(side=RIGHT)

def generate_click():
    root.title('Processing...')
    settings.maze_height = int(height_scale.get())
    settings.maze_width = int(width_scale.get())
    settings.clock_tick = int(speed_scale.get())
    prepare_maze(screen, check_button.get())
    root.title('Done!')
    root.update

generate_button = CTkButton(
    gui_frame,
    text='Generate!',
    command = generate_click,
    font=widgets_font
)
generate_button.pack(side=BOTTOM, fill=X, padx=10, pady=20)

root.mainloop()
