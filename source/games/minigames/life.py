import pgzrun, pygame
import math

GAME_X = 70
GAME_Y = 50
CELL_SIZE = 10
BORDER = 1

HUD = 2 * CELL_SIZE
CELL_DRAW_SIZE = CELL_SIZE - BORDER
WIDTH = GAME_X * CELL_SIZE
HEIGHT = GAME_Y * CELL_SIZE + HUD


def reset() : # {{{
    global grid

    grid = []

    for y in range(GAME_Y):
        grid.append([False for x in range(GAME_X)])
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
    screen.fill((255, 255, 255))
    screen.draw.filled_rect(
        Rect(0, 0, WIDTH, HUD), color="black")

    for y in range(GAME_Y):
        for x in range(GAME_X):
            # colour = (0, 255, 255) if x == selected_x and y == selected_y else (220, 220, 220)
            if x == selected_x and y == selected_y:
                colour = (0, 255, 255)
            elif grid[y][x]:
                colour = (255, 0, 255)
            else:
                colour = (220, 220, 220)

            screen.draw.filled_rect(
                    Rect(
                        (x*CELL_SIZE, y*CELL_SIZE + HUD), 
                        (CELL_DRAW_SIZE, CELL_DRAW_SIZE)),
                    color=colour
                    )
    screen.draw.text(
        "X: %d, Y:%d" % (selected_x, selected_y),
        (3, 3),
        color="orange"
        )
# }}}
def on_mouse_down(pos, button): # {{{
    if button == mouse.LEFT:
        grid[selected_y][selected_x] = not grid[selected_y][selected_x] 
    if button == mouse.RIGHT:
        neighbour_count = 0
        print("Finding neighbours of grid %d:%d:" % (selected_y, selected_x))

        for dy in range(-1, 2):
            for dx in range(-1, 2):
                if (
                        not (dy == 0 and dx ==0)
                        and 0 <= (selected_y + dy) < GAME_Y
                        and 0 <= (selected_x + dx) < GAME_X
                        and grid[selected_y + dy][selected_x + dx]
                        ):
                    neighbour_count +=1

        print("Total neighbours: %d\n%s" % (neighbour_count, 30*"_"))
# }}}
def on_key_down(): # {{{
    global grid
    next_grid = []

    for y in range(GAME_Y):
        next_grid.append([])
        for x in range(GAME_X):
            # next_grid.append([True for x in range(GAME_X)])
            
            neighbour_count = 0
            # print("Finding neighbours of grid %d:%d:" % (selected_y, selected_x))

            for dy in range(-1, 2):
                for dx in range(-1, 2):
                    if (
                            not (dy == 0 and dx ==0)
                            and 0 <= (y + dy) < GAME_Y
                            and 0 <= (x + dx) < GAME_X
                            and grid[y + dy][x + dx]
                            ):
                        neighbour_count +=1
                    
            next_grid[y].append(
                    neighbour_count == 3 or (grid[y][x] and neighbour_count == 2)
                    )

    grid = next_grid
# }}}
def clamp(val, minv, maxv): return minv if val < minv else maxv if val > maxv else val

reset()
pgzrun.go()
