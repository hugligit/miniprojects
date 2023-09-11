import pgzrun, pygame
import random



GAME_Y = 14
GAME_X = 19
CELL_SIZE = 18
HUD = 36
NUMBER_OF_FLOWERS = 40
WIDTH = GAME_X * CELL_SIZE
HEIGHT = GAME_Y * CELL_SIZE + HUD


def get_surrounding_flower_count(x, y): # {{{
    surrounding_flower_count = 0

    for dy in range(-1, 2):
        for dx in range(-1, 2):
            if (
                    not (dy == 0 and dx == 0)
                    and 0 <= (y+dy) < len(grid)
                    and 0 <= (x+dx) < len(grid[y+dy])
                    and grid[y+dy][x+dx]['flower']
                    ): 
                surrounding_flower_count +=1
    return surrounding_flower_count
# }}}

def update(): # {{{
    global selected_x, selected_y

    mouse_x, mouse_y = pygame.mouse.get_pos()
    selected_x = mouse_x // CELL_SIZE
    selected_y = (mouse_y - HUD) // CELL_SIZE
    selected_x = clamp(selected_x, 0, GAME_X-1)
    selected_y = clamp(selected_y, 0, GAME_Y-1)

    # }}}
def draw(): # {{{
    screen.fill((0, 0, 0))
    for y in range(GAME_Y):
        for x in range(GAME_X):
            if grid[y][x]['state'] == 'uncovered':
                draw_cell('uncovered', x, y)
            else:
                if x == selected_x and y == selected_y and not game_over:
                    if pygame.mouse.get_pressed()[0] == 1:
                        if grid[y][x]['state'] == 'flag':
                            image = 'covered'
                        else:
                            image = 'uncovered'
                    else:
                        image = 'covered_highlighted'
                else:
                    image = 'covered'
                draw_cell(image, x, y)

            surrounding_flower_count = get_surrounding_flower_count(x, y)


            if grid[y][x]['flower'] and game_over:
                draw_cell('flower', x, y)
            elif surrounding_flower_count > 0 and grid[y][x]['state'] == 'uncovered':
                draw_cell('%s' % surrounding_flower_count, x, y)


            if grid[y][x]['state'] == 'flag':
                draw_cell('flag', x, y)
            if grid[y][x]['state'] == 'question':
                draw_cell('question', x, y)

    screen.draw.text("x: %d, y: %d" % (selected_x, selected_y), (2, 2), color='orange')
    # }}}
def on_mouse_up(button): # {{{
    global game_over
    global first_click
    
    if not game_over:
        if button == mouse.LEFT and grid[selected_y][selected_x]['state'] != 'flag':
            if first_click: first_click = False
            if grid[selected_y][selected_x]['flower']:
                grid[selected_y][selected_x]['state'] = 'uncovered'
                game_over = True
            else:
                stack = [{
                 'x': selected_x,
                 'y': selected_y,
                 }]

                while len(stack) > 0:
                    current = stack.pop()
                    x = current['x']
                    y = current['y']
                    grid[y][x]['state'] = 'uncovered'

                    if get_surrounding_flower_count(x, y) == 0:
                        for dy in range(-1, 2):
                            for dx in range(-1, 2):
                                if (
                                        not (dy == 0 and dx == 0)
                                        and 0 <= (y + dy) < GAME_Y
                                        and 0 <= (x + dx) < GAME_X
                                        and grid[y+dy][x+dx]['state'] in ('covered', 'question')
                                        ):
                                    stack.append({
                                        'x': x + dx,
                                        'y': y + dy,
                                        })
                complete = True

                for y in range(GAME_Y):
                    for x in range(GAME_X):
                        if grid[y][x]['state'] != 'uncovered' and not grid[y][x]['flower']:
                            complete = False

                if complete: game_over = True
    else:
        reset()

    if button == mouse.RIGHT:
        # flower_state = grid[selected_y][selected_x]['flower']
        # grid[selected_y][selected_x]['flower'] = not flower_state

        if grid[selected_y][selected_x]['state'] == 'covered':
            grid[selected_y][selected_x]['state']  = 'flag'

        elif grid[selected_y][selected_x]['state'] == 'flag':
            grid[selected_y][selected_x]['state']  = 'question'

        elif grid[selected_y][selected_x]['state'] == 'question':
            grid[selected_y][selected_x]['state']  = 'covered'


        # }}}
def reset(): #{{{
    global grid
    global game_over
    global first_click

    first_click = True
    game_over = False
    grid = []
    possible_flower_positions = []

    for y in range(GAME_Y):
        grid.append([])
        for x in range(GAME_X):
            grid[y].append({
                'flower': False,
                'state': 'covered',
                })


    for y in range(GAME_Y):
        for x in range(GAME_X):
            # if not (x == selected_x and y == selected_y):
            possible_flower_positions.append({'x': x, 'y': y})


    for i in range(NUMBER_OF_FLOWERS):
        position = possible_flower_positions.pop(random.randrange(len(possible_flower_positions)))
        grid[position['y']][position['x']]['flower'] = True
        # }}}
def clamp(val, minv, maxv): return minv if val < minv else maxv if val > maxv else val
def draw_cell(image, x, y): screen.blit(image, (x*CELL_SIZE, y*CELL_SIZE+HUD))
def on_key_down(key): reset()

reset()
pgzrun.go()
