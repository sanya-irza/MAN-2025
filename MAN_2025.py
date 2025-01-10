import os
import pygame
from const import *
from customtkinter import *
from tkinter import *
from calculation import prepare_maze

set_appearance_mode('dark')
set_default_color_theme('dark-blue')

root = CTk()

generate_frame = CTkFrame(
    root, 
    width = screen_width, 
    height = screen_height
)
generate_frame.pack(side = LEFT)

gui_frame = CTkFrame(
    root, 
    height = screen_height
)
gui_frame.pack(side=RIGHT,fill=Y)

widgets_font = CTkFont(family='Cascadia Code', size=20)

os.environ['SDL_WINDOWID'] = str(generate_frame.winfo_id())
os.environ['SDL_VIDEODRIVER'] = 'windib'

pygame.display.init()
screen = pygame.display.set_mode((screen_width, screen_height))
instant_appearance = StringVar()

settings_label = CTkLabel(
    gui_frame, 
    text='Settings',
    font=widgets_font
)
settings_label.pack(side=TOP, fill=X, pady=20, padx=10)

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
    from_=1,
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
    from_=1, 
    to=100, 
    height=20,
    command=get_width,
    orientation=HORIZONTAL
)
width_scale.pack(side=TOP)

check_button = CTkCheckBox(
    gui_frame, 
    text='Instant appearance?', 
    offvalue=False, 
    onvalue=True, 
    variable=instant_appearance,
    font=widgets_font
)
check_button.pack(side=TOP, pady=5, padx=10)

def generate_click():
    root.title('Processing...')
    prepare_maze(screen, instant_appearance.get())
    root.title('Done!')
    root.update

generate_button = CTkButton(
    gui_frame,
    text='Generate!',
    command = generate_click,
    font=widgets_font
)
generate_button.pack(side=TOP, pady=10, padx=10)

root.mainloop()
