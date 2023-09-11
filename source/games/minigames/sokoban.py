import os
os.environ['SDL_video_window_pos'] = '%d,%d' % (20, 100)
import pgzrun
import copy

# {{{
#   @  Player
#   +  PlayerPlayer on storage
#   $  Box
#   *  BoxBox on storage
#   .  Storage
#   #  StorageWall


#"""
#  ###
#  #.#
#  # ####
####$ $.#
##. $@###
#####$#
#   #.#
#   ###
#"""
# }}}


import copy





player = '@'
player_on_storage = '+'
box = '$'
box_on_storage = '*'
storage = '.'
wall = '#'
empty = ' '
current_level = 0

LEVELS = [ # {{{
    [
        [' ', ' ', '#', '#', '#'],
        [' ', ' ', '#', '.', '#'],
        [' ', ' ', '#', ' ', '#', '#', '#', '#'],
        ['#', '#', '#', '$', ' ', '$', '.', '#'],
        ['#', '.', ' ', '$', '@', '#', '#', '#'],
        ['#', '#', '#', '#', '$', '#'],
        [' ', ' ', ' ', '#', '.', '#'],
        [' ', ' ', ' ', '#', '#', '#'],
    ],
    [
        ['#', '#', '#', '#', '#'],
        ['#', ' ', ' ', ' ', '#'],
        ['#', '@', '$', '$', '#', ' ', '#', '#', '#'],
        ['#', ' ', '$', ' ', '#', ' ', '#', '.', '#'],
        ['#', '#', '#', ' ', '#', '#', '#', '.', '#'],
        [' ', '#', '#', ' ', ' ', ' ', ' ', '.', '#'],
        [' ', '#', ' ', ' ', ' ', '#', ' ', ' ', '#'],
        [' ', '#', ' ', ' ', ' ', '#', '#', '#', '#'],
        [' ', '#', '#', '#', '#', '#'],
    ],
    [
        [' ', '#', '#', '#', '#', '#', '#', '#'],
        [' ', '#', ' ', ' ', ' ', ' ', ' ', '#', '#', '#'],
        ['#', '#', '$', '#', '#', '#', ' ', ' ', ' ', '#'],
        ['#', ' ', '@', ' ', '$', ' ', ' ', '$', ' ', '#'],
        ['#', ' ', '.', '.', '#', ' ', '$', ' ', '#', '#'],
        ['#', '#', '.', '.', '#', ' ', ' ', ' ', '#'],
        [' ', '#', '#', '#', '#', '#', '#', '#', '#'],
    ],
] # }}}
C_EMPTY   = ((255 , 255 , 230))
C_STORAGE = ((230 , 220 , 170))
C_WALL    = ((33  , 33  , 33 ))
C_BOX     = ((60  , 115 , 20 ))
C_PERSON  = ((190 , 30   ,65 ))
C_BG = { # {{{
    ' ': C_EMPTY,
    '@': C_EMPTY,
    '$': C_EMPTY,
    '.': C_STORAGE,
    '+': C_STORAGE,
    '*': C_STORAGE,
    '#': C_WALL,
} # }}}
C_FG = { # {{{
        '$': C_BOX,
        '*': C_BOX,
        '@': C_PERSON,
        '+': C_PERSON,
} # }}}
CELL_SIZE = 30
GAP = 8



def draw(): # {{{
    screen.fill(C_EMPTY)

    for y, row in enumerate(level):
        for x, cell in enumerate(row):
            screen.draw.filled_rect(
                Rect ( (x*CELL_SIZE, y*CELL_SIZE), (CELL_SIZE, CELL_SIZE)),
                color = C_BG[cell]
                )
            if cell in ('@', '+', '$', '*'):
                if cell in ('$', '*'):
                    screen.draw.filled_rect(
                        Rect ( 
                            (x*CELL_SIZE + GAP, y*CELL_SIZE + GAP), 
                            (CELL_SIZE - 2*GAP, CELL_SIZE - 2*GAP)),
                        color = C_FG[cell]
                        )
                else:
                    screen.draw.filled_circle(
                            ((x+0.5)*CELL_SIZE, (y+0.5)*CELL_SIZE), 
                            (CELL_SIZE - 2*GAP)/2,
                        color = C_FG[cell]
                        )

# }}}
def on_key_down(key): # {{{
    global current_level
    if key in (keys.W, keys.A, keys.S, keys.D):
        for test_y, row in enumerate(level):
            for test_x, cell in enumerate(row):
                if cell in (player, player_on_storage):
                    player_x = test_x
                    player_y = test_y
        dx = 0
        dy = 0

        if   key == keys.A: dx = -1
        elif key == keys.D: dx = 1
        elif key == keys.W: dy = -1
        elif key == keys.S: dy = 1



        current = level[player_y][player_x]
        adjacent = level[player_y + dy][player_x + dx]

        beyond = ''
        if (
                0 <= player_y + dy + dy < len(level)
                and
                0 <= player_x + dx + dx < len(level[player_y + dy + dy])
                ):
            beyond = level[player_y + dy + dy][player_x + dx + dx]

        next_adjacent = {
                empty: player,
                storage: player_on_storage,
                }

        next_current = {
                player: empty,
                player_on_storage: storage,
                }

        next_beyond = {
                empty: box,
                storage: box_on_storage,
                }

        next_adjacent_push = {
                box: player,
                box_on_storage: player_on_storage,
                }

        if adjacent in next_adjacent:
            level[player_y][player_x] = next_current[current]
            level[player_y + dy][player_x + dx] = next_adjacent[adjacent]
        elif beyond in next_beyond and adjacent in next_adjacent_push:
            level[player_y][player_x] = next_current[current]
            level[player_y + dy][player_x + dx] = next_adjacent_push[adjacent]
            level[player_y + dy + dy][player_x + dx + dx] = next_beyond[beyond]

        complete = True
        for y, row in enumerate(level):
            for x, cell in enumerate(row):
                if cell == box:
                    complete = False

        if complete: 
            current_level += 1
            load_level()

    
    elif key == keys.R:
        load_level()
    elif key == keys.N: 
        current_level += 1
        load_level()
    elif key == keys.P: 
        current_level -= 1
        load_level()


# }}}
def load_level(): # {{{
    global current_level
    global level
    current_level = current_level  % len(LEVELS)
    level = copy.deepcopy(LEVELS[current_level])
    # }}}





load_level()
pgzrun.go()
