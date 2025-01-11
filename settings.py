import const

maze_height = 50
maze_width = 50

def y_offset():
    return (const.SCREEN_HEIGHT - screen_height()) / 2

def x_offset():
    return (const.SCREEN_WIDTH - screen_width()) / 2

def cell_size():
    return int(min(const.SCREEN_HEIGHT / maze_height, const.SCREEN_WIDTH / maze_width))

clock_tick = 10

def screen_height():
    return maze_height * cell_size()

def screen_width():
    return maze_width * cell_size()