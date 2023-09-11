import pgzrun
import random

# SETTINGS {{{
TILE_SIZE = 200
GAME_WIDTH = 4
GAME_HEIGHT = 4
TILE_GAP = 5
BORDER_SIZE = 20
WIDTH = GAME_WIDTH * TILE_SIZE + 2 * BORDER_SIZE + (GAME_WIDTH + 1) * TILE_GAP
HEIGHT = GAME_HEIGHT * TILE_SIZE + 2 * BORDER_SIZE + (GAME_HEIGHT + 1) * TILE_GAP

# }}}
class Game(object): # {{{
    class Board(object): # {{{
        class Tile(object): # {{{
            def __init__(self, value): # {{{
                self.value = value + 1
            # }}}
            def draw(self, order): # {{{
                x = order % GAME_WIDTH
                y = order // GAME_WIDTH
                x = x * TILE_SIZE + BORDER_SIZE + TILE_GAP * (order % GAME_WIDTH) + TILE_GAP
                y = y * TILE_SIZE + BORDER_SIZE + TILE_GAP * (order // GAME_WIDTH) + TILE_GAP

                screen.draw.filled_rect(Rect(x, y, TILE_SIZE, TILE_SIZE), color="#773300")
                screen.draw.text(
                        "%s" % (self.value), 
                        center=(x+TILE_SIZE/2, y+TILE_SIZE/2), 
                        color="#aa9900",
                        fontsize=0.8*TILE_SIZE,
                        owidth=0.4,
                        ocolor="#662200",

                        )
            # }}}
        # }}}
        def __init__(self): # {{{
            self.border = BORDER_SIZE
            self.tiles = [self.Tile(i) for i in range(GAME_WIDTH * GAME_HEIGHT - 1)]
            self.start = [tile.value for tile in self.tiles]
            self.tiles.append(None)
            self.start.append(None)
        # }}}
        def draw(self): # {{{
            border_colour = "#880000"
            if self.is_ordered():
                border_colour = "#662200"
            screen.fill((0, 0, 0))
            dimensions = (
                    ((0, 0), (WIDTH, BORDER_SIZE)),
                    ((0, BORDER_SIZE), (BORDER_SIZE, HEIGHT - 2*BORDER_SIZE)),
                    ((WIDTH-BORDER_SIZE, BORDER_SIZE), (WIDTH, HEIGHT - 2*BORDER_SIZE)),
                    ((0, HEIGHT-BORDER_SIZE), (WIDTH, BORDER_SIZE)),
                    )

            for pos, size in dimensions:
                screen.draw.filled_rect( Rect(pos, size), color=border_colour,)
                screen.draw.rect( Rect(pos, size), color="black",)

            for i, tile in enumerate(self.tiles):
                if tile: tile.draw(i)
        # }}}
        def update(self, dt): # {{{
            pass
        # }}}
        def shuffle(self): # {{{
            directions = [(0, -1), (-1, 0), (0, 1), (1, 0)]
            for i in range(400):
                random_move = directions[random.randint(0, 3)]
                self.move_tiles(random_move)
            # TODO {{{
            # 1. move the empty space to bottom right
            # 2. save the shuffling sequence
            # }}}
        # }}}
        def move_tiles(self,direction): # {{{
            empty_index = self.tiles.index(None)
            empty_x = empty_index % GAME_WIDTH
            empty_y = empty_index // GAME_WIDTH
            swap_x = empty_x + direction[0]
            swap_y = empty_y + direction[1]
            if (
                0 <= swap_x < GAME_WIDTH
                and
                0 <= swap_y < GAME_HEIGHT
                ):
                swap_index = swap_y * GAME_WIDTH + swap_x

                self.tiles[empty_index], self.tiles[swap_index] = self.tiles[swap_index], self.tiles[empty_index]
            
            # }}}
        def is_ordered(self):
            is_ordered = False
            current_state = []
            for tile in self.tiles:
                if tile: current_state.append(tile.value)
                else: current_state.append(None)

            is_ordered = self.start == current_state

            return is_ordered
    # }}}
    def __init__(self): # {{{
        self.board = self.Board()
    # }}}
    def update(self, dt): # {{{
        pass
    # }}}
    def draw(self): # {{{
        self.board.draw()
    # }}}
    def on_key_down(self, key): # {{{
        if key == keys.R:
            self.board.shuffle()
        elif key in [key.W, key.A, key.S, key.D]:
            direction = {
                key.W: (0, -1),
                key.A: (-1, 0),
                key.S: (0, 1),
                key.D: (1, 0),
                }[key]
            self.board.move_tiles(direction)
    # }}}
    def on_mouse_down(self, pos, key): # {{{
        x, y = pos

        x = (x - BORDER_SIZE)//(TILE_SIZE + TILE_GAP)
        y = (y - BORDER_SIZE)//(TILE_SIZE + TILE_GAP)
        i = y*GAME_WIDTH + x
        empty_index = self.board.tiles.index(None)
        empty_x = empty_index % GAME_WIDTH
        empty_y = empty_index // GAME_WIDTH
        are_next = (
                empty_x == x and abs(empty_y - y) == 1 
                or
                empty_y == y and abs(empty_x - x) == 1 
                )

        if are_next:
            self.board.tiles[empty_index], self.board.tiles[i] = self.board.tiles[i], self.board.tiles[empty_index]
        print(self.board.is_ordered())

        # }}}

# }}}
# BOILERPLATE {{{
def update(dt): game.update(dt)
def draw(): game.draw()
def on_key_down(key): game.on_key_down(key)
def on_mouse_down(pos, button): game.on_mouse_down(pos, button)
# }}}

game = Game()
pgzrun.go()



# 王玉
# 飛竜
# 角馬
# 金銀
# 全
# 桂今
# 香仝
# 歩个

# 王将
# 玉将
# 飛車	飛
# 竜王龍 or 竜[b]	ryū	FR
# 角行角	kaku	B
# 竜馬orse	+B	馬	uma	WB
# 金将G	金	kin	WfF
# 銀将S	銀	gin	FfW
# 成銀+S	(全)	—	WfF
# 桂馬N	桂	kei	ffN
# 成桂	+N	(圭or今)	—	WfF
# 香車L	香	kyō	fR
# 成香	+L	(杏 or 仝)	—	WfF
# 歩兵P	歩	fu	fW
# と金	t
