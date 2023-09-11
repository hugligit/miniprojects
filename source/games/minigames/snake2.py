import pgzero, pgzrun
import random

GRID_X = 24
GRID_Y = 16
CELL = 15
WIDTH = GRID_X * CELL
HEIGHT = GRID_Y * CELL
TICK = 0.15
SNAKE_SEGMENT_COLOLUR = (165, 255, 81)
SNAKE_HEAD_COLOLUR = (165, 255, 255)
DEAD_SNAKE_COLOUR = (140, 140, 140)
FOOD_COLOUR = (165, 0, 0)

class Game(object): # {{{
    def __init__(self): # {{{
        self.food = {'x': 0, 'y': 0 }
        # }}}
    def place_food(self, snake): # {{{
        possible_food_positions = []

        for x in range(GRID_X):
            for y in range(GRID_Y):
                possible = True
                for segment in snake.segments:
                    if x == segment['x'] and y == segment['y']:
                        possible = False
                if possible:
                    possible_food_positions.append({'x': x, 'y': y})

        self.food = random.choice(possible_food_positions)
        # }}}
    def draw_food(self, size):# {{{
            screen.draw.filled_rect(
                Rect(
                    (self.food['x'] * size), 
                    (self.food['y'] * size), 
                    size, 
                    size),
                color=FOOD_COLOUR
                )
# }}}
    # }}}
class Snake(object): # {{{
    def __init__(self): # {{{
        self.segments = [
            {'x':2, 'y': 0},
            {'x':1, 'y': 0},
            {'x':0, 'y': 0},
        ]

        self.direction_queue = ['right']
        self.can_move = True
# }}}
    def draw(self, size):# {{{
        if self.can_move:
            colour_segment = SNAKE_SEGMENT_COLOLUR
            colour_head = SNAKE_HEAD_COLOLUR
        else:
            colour_segment = colour_head = DEAD_SNAKE_COLOUR
        for segment in self.segments:
            screen.draw.filled_rect(
                Rect(
                    (segment['x'] * size) + 1, 
                    (segment['y'] * size) + 1, 
                    size - 2, 
                    size - 2),
                color=colour_segment
                )

            screen.draw.filled_rect(
                Rect(
                    (self.segments[0]['x'] * size), 
                    (self.segments[0]['y'] * size), 
                    size, 
                    size),
                color=colour_head
                )
# }}}
    def update_position(self): # {{{
        if len(self.direction_queue) > 1: self.direction_queue.pop(0)
        next_x = self.segments[0]['x']
        next_y = self.segments[0]['y']
        direction = self.direction_queue[0]

        if direction == 'right':
            next_x +=1
            if next_x >=  GRID_X:
                next_x = 0

        elif direction == 'left':
            next_x -=1
            if next_x < 0:
                next_x = GRID_X -1

        elif direction == 'up':
            next_y -=1
            if next_y < 0:
                next_y = GRID_Y -1

        elif direction == 'down':
            next_y +=1
            if next_y >=  GRID_Y:
                next_y = 0

        for segment in self.segments[:-1]:
            if next_x == segment['x'] and next_y == segment['y']:
                self.can_move = False


        if self.can_move:
            self.segments.insert(0, {'x': next_x, 'y': next_y})
        # }}}
    def send_key(self, key): # {{{
        last_direction = self.direction_queue[-1]

        if key == keys.A and not (last_direction in ('right', 'left')):
            self.direction_queue.append('left')
        elif key == keys.D and not (last_direction in ('right', 'left')):
            self.direction_queue.append('right')
        elif key == keys.W and not (last_direction in ('up', 'down')):
            self.direction_queue.append('up')
        elif key == keys.S and not (last_direction in ('up', 'down')):
            self.direction_queue.append('down')


    # }}}
    def found_food(self, food): # {{{
        test = self.segments[0]['x'] == food['x'] and self.segments[0]['y'] ==  food['y']
        return test
    # }}}
# }}}
def on_key_down(key): # {{{
    if key in [keys.W, keys.A, keys.S, keys.D]: bob.send_key(key)
    # }}}
def update(dt): # {{{
    global timer, bob, game
    timer += dt

    if bob.can_move:
        if timer >= TICK:
            timer = 0
            bob.update_position()
            if bob.found_food(game.food):
                game.place_food(bob)
            else:
                bob.segments.pop()
    elif timer >= 2:
        reset()
# }}}
def draw(): # {{{
    screen.fill((0, 0, 0))
    bob.draw(CELL)
    game.draw_food(CELL)
# }}}

def reset():
    global timer, bob, game
    bob = Snake()
    game = Game()
    game.place_food(bob)
    timer = 0

reset()
pgzrun.go()
