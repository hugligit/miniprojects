import pgzero, pgzrun
import random


# SETTINGS {{{
def move_food():# {{{
    global food_position
    possible_food_positions = []

    for food_x in range(grid_x_count):
        for food_y in range(grid_y_count):
            possible = True

            for segment in snake_segments:
                if food_x == segment['x'] and food_y == segment['y']:
                    possible == False

                if possible:
                    possible_food_positions.append({'x': food_x, 'y': food_y})

    food_position = random.choice(possible_food_positions)

    


    # }}}
def reset():# {{{
    global timer
    global direction_queue
    global snake_segments
    global snake_alive

    snake_alive =  True

    timer = 0

    snake_segments = [
            {'x': 2, 'y':1},
            {'x': 1, 'y':1},
            {'x': 0, 'y':1},
            ]

    direction_queue = ['right']
    move_food()
    # }}}

grid_x_count = 24
grid_y_count = 16
cell_size = 15

WIDTH = grid_x_count * cell_size
HEIGHT = grid_y_count * cell_size
reset()
# }}}
# DRAW {{{
def draw():

    def draw_cell(x, y, color): # {{{
        screen.draw.filled_rect(
                Rect (
                    x * cell_size,
                    y * cell_size,
                    cell_size -1,
                    cell_size -1,
                    ),
                color=color
                ) # }}}

    screen.fill((0, 0, 0))
    screen.draw.filled_rect(
            Rect (0, 0, grid_x_count * cell_size, grid_y_count * cell_size),
            color=(70, 70, 70)
            )

    draw_cell(food_position['x'], food_position['y'], color=(255, 76, 76))
    color=(165, 255, 81)
    if not snake_alive: color=(140, 140, 140)
    for segment in snake_segments: draw_cell(segment['x'], segment['y'], color)
    draw_cell(snake_segments[0]['x'], snake_segments[0]['y'], color=(165, 255, 220))

    for index, direction in enumerate(direction_queue):
        screen.draw.text(
                '%d: %s' % (index, direction), 
                (cell_size, WIDTH - (cell_size + cell_size * index))
                )
# }}}
# UPDATE {{{
def update(dt):
    global timer
    global food_position
    global snake_alive

    timer += dt

    if snake_alive:
        if timer >= 0.15: 
            timer = 0
            # print("tick")
            if len (direction_queue) > 1: direction_queue.pop(0)

            next_x_position = snake_segments[0]['x']
            next_y_position = snake_segments[0]['y']

            direction = direction_queue[0]
            if direction == 'right': 
                next_x_position += 1
                if next_x_position >= grid_x_count:
                    next_x_position = 0

            elif direction == 'left': 
                next_x_position -= 1
                if next_x_position < 0:
                    next_x_position = grid_x_count

            elif direction == 'down': 
                next_y_position += 1
                if next_y_position >= grid_y_count:
                    next_y_position = 0

            elif direction == 'up': 
                next_y_position -= 1
                if next_y_position < 0:
                    next_y_position = grid_y_count -1


            can_move = True

            for segment in snake_segments[:-1]:
                if next_x_position == segment['x'] and next_y_position == segment['y']:
                    can_move = False

            if can_move:
                snake_segments.insert(0, {'x': next_x_position, 'y': next_y_position})


                test = snake_segments[0]['x'] == food_position['x'] and snake_segments[0]['y'] ==  food_position['y']
                if test:
                    move_food()
                else:
                    snake_segments.pop()
            else:
                snake_alive = False
    elif timer >= 2:
        reset()

# }}}
# EVENT HOOKS {{{
def on_key_down(key): # {{{
    global direction
    last_direction = direction_queue[-1]

    if key == keys.A and not (last_direction in ('right', 'left')):
        direction_queue.append('left')
    elif key == keys.D and not (last_direction in ('right', 'left')):
        direction_queue.append('right')
    elif key == keys.W and not (last_direction in ('up', 'down')):
        direction_queue.append('up')
    elif key == keys.S and not (last_direction in ('up', 'down')):
        direction_queue.append('down')
    # }}}
# }}}

pgzrun.go()
