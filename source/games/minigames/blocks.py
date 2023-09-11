import pgzrun
import random

GAME_X = 10
GAME_Y = 18
TILE_WIDTH = 20
TICK = 0.5
HUD = 4
WIDTH = GAME_X * TILE_WIDTH
HEIGHT = (GAME_Y + HUD) * TILE_WIDTH

class Game(object): # {{{
    class Piece(object): # {{{
        def __init__(self, parent): # {{{
            self.parent = parent
            self.x = GAME_X // 2 - 2
            self.y = 0
            self.rotation = 0
            self.type = parent.sequence.pop()
            if len(parent.sequence) == 0: 
                self.parent.sequence = self.parent.new_sequence()
            # }}}
        def draw(self): # {{{
            for y in range(4):
                for x in range(4):
                    block = self.parent.PIECES[self.type][self.rotation][y][x]
                    if block > 0: self.parent.draw_block(block, x + self.x, y + self.y + HUD)
        # }}}
        def move(self, direction): # {{{
            test_offset = self.x + direction
            if self.can_move(test_x=test_offset):
                self.x = test_offset
        # }}}
        def rotate(self, direction): # {{{
            test_rotation = self.rotation
            test_rotation = (test_rotation + direction) % len(self.parent.PIECES[self.type])
            if self.can_move(test_x=self.x, test_y=self.y, test_r=self.rotation):
                self.rotation = test_rotation

        # }}}
        def drop(self): # {{{
            while self.can_move(self.x, self.y+1, self.rotation):
                self.y += 1
                self.parent.timer = TICK
        # }}}
        def can_move(self, test_x=None, test_y=None, test_r=None): # {{{
            if not test_x: test_x = self.x
            if not test_y: test_y = self.y
            if not test_r: test_r = self.rotation

            for y in range(4):
                for x in range(4):
                    if (
                            self.parent.PIECES[self.type][self.rotation][y][x] != 0
                            and
                            (
                                ((test_x + x) not in range(GAME_X))
                                or
                                test_y + y >= GAME_Y
                                or
                                self.parent.area[test_y + y][test_x + x] != 0
                                )
                            ): return False
            return True
        # }}}
        # }}}
    def __init__(self): # {{{
        self.COLOURS = { # {{{
            0: (0xaa, 0xaa, 0xaa),
            1: (120, 195, 239),
            2: (236, 231, 108),
            3: (124, 218, 193),
            4: (234, 177, 121),
            5: (211, 136, 236),
            6: (248, 147, 196),
            7: (169, 221, 118),
            }
        #  }}}
        # self.COLOURS = { # {{{
        #     0: (0xaa, 0xaa, 0xaa),
        #     1: (255, 0, 0),
        #     2: (0, 255, 0),
        #     3: (0, 0, 255),
        #     4: (255, 255, 0),
        #     5: (0, 255, 255),
        #     6: (255, 0, 255),
        #     7: (255, 128, 0),
        #     }
        # #  }}}
        self.PIECES = [] # {{{
        self.PIECES.append([ # {{{ I
            [ [0, 0, 0, 0],
              [1, 1, 1, 1],
              [0, 0, 0, 0],
              [0, 0, 0, 0] ],

            [ [0, 1, 0, 0],
              [0, 1, 0, 0],
              [0, 1, 0, 0],
              [0, 1, 0, 0] ]
            ]) # }}}
        self.PIECES.append([ # {{{ O
            [ [0, 0, 0, 0],
              [0, 2, 2, 0],
              [0, 2, 2, 0],
              [0, 0, 0, 0] ]
            ]) # }}}
        self.PIECES.append([ # {{{ J
            [ [0, 0, 0, 0],
              [3, 3, 3, 0],
              [0, 0, 3, 0],
              [0, 0, 0, 0] ],

            [ [0, 3, 0, 0],
              [0, 3, 0, 0],
              [3, 3, 0, 0],
              [0, 0, 0, 0] ],

            [ [3, 0, 0, 0],
              [3, 3, 3, 0],
              [0, 0, 0, 0],
              [0, 0, 0, 0] ],

            [ [0, 3, 3, 0],
              [0, 3, 0, 0],
              [0, 3, 0, 0],
              [0, 0, 0, 0] ],
            ]) # }}}
        self.PIECES.append([ # {{{ L
            [ [0, 0, 0, 0],
              [4, 4, 4, 0],
              [4, 0, 0, 0],
              [0, 0, 0, 0] ],

            [ [0, 4, 0, 0],
              [0, 4, 0, 0],
              [0, 4, 4, 0],
              [0, 0, 0, 0] ],

            [ [0, 0, 4, 0],
              [4, 4, 4, 0],
              [0, 0, 0, 0],
              [0, 0, 0, 0] ],

            [ [4, 4, 0, 0],
              [0, 4, 0, 0],
              [0, 4, 0, 0],
              [0, 0, 0, 0] ],
            ]) # }}}
        self.PIECES.append([ # {{{ T
            [ [0, 0, 0, 0],
              [5, 5, 5, 0],
              [0, 5, 0, 0],
              [0, 0, 0, 0] ],

            [ [0, 5, 0, 0],
              [0, 5, 5, 0],
              [0, 5, 0, 0],
              [0, 0, 0, 0] ],

            [ [0, 5, 0, 0],
              [5, 5, 5, 0],
              [0, 0, 0, 0],
              [0, 0, 0, 0] ],

            [ [0, 5, 0, 0],
              [5, 5, 0, 0],
              [0, 5, 0, 0],
              [0, 0, 0, 0] ],
            ]) # }}}
        self.PIECES.append([ # {{{ S
            [ [0, 0, 0, 0],
              [0, 6, 6, 0],
              [6, 6, 0, 0],
              [0, 0, 0, 0] ],

            [ [0, 6, 0, 0],
              [0, 6, 6, 0],
              [0, 0, 6, 0],
              [0, 0, 0, 0] ],
            ]) # }}}
        self.PIECES.append([ # {{{ Z
            [ [0, 0, 0, 0],
              [7, 7, 0, 0],
              [0, 7, 7, 0],
              [0, 0, 0, 0] ],

            [ [0, 0, 7, 0],
              [0, 7, 7, 0],
              [0, 7, 0, 0],
              [0, 0, 0, 0] ],
            ]) # }}}
        # }}}
        self.reset()
    # }}}
    def reset(self): # {{{
        self.timer = 0
        self.score = 0
        self.area = []
        for y in range(GAME_Y):
            self.area.append([0 for x in range(GAME_X)])
        self.sequence = self.new_sequence()
        self.piece = self.Piece(self)
    # }}}
    def update(self, dt): # {{{
        self.timer += dt

        if self.timer > TICK:
            self.timer = 0

            test_offset_y = self.piece.y + 1
            if self.piece.can_move(test_y=test_offset_y): 
                self.piece.y = test_offset_y
            else:
                for y in range(4):
                    for x in range(4):
                        block = self.PIECES[self.piece.type][self.piece.rotation][y][x]
                        if block != 0:
                            self.area[self.piece.y + y][self.piece.x + x] = block

                completes = []
                for y in range(GAME_Y):
                    if 0 not in self.area[y]:
                        completes.append(y)

                for i in completes:
                    self.area.pop(i)
                    self.area.insert(0, [0 for i in range(GAME_X)])
                    self.score += 1


                self.piece = self.Piece(self)
                if not self.piece.can_move(self.piece.x, self.piece.y, self.piece.rotation): self.reset()
    # }}}
    def draw(self): # {{{
        screen.fill((0, 0, 0))

        for y in range(GAME_Y):
            for x in range(GAME_X):
                block = self.area[y][x]
                self.draw_block(block, x, y+HUD)

        self.piece.draw()

        for y in range(4):
            for x in range(4):
                block = self.PIECES[self.sequence[-1]][0][y][x]
                if block > 0: self.draw_block(block, x + 3, y + 0) 

        screen.draw.text('%d' % self.score, (5,5))
    # }}}
    def new_sequence(self): # {{{
        sequence = list(range(7))
        # random.shuffle(sequence)
        return sequence
    # }}}
    def draw_block(self, block, x, y): # {{{
        colour = self.COLOURS[block]
        r = Rect(
                x * TILE_WIDTH,
                y * TILE_WIDTH,
                TILE_WIDTH-1,
                TILE_WIDTH-1
                )
        screen.draw.filled_rect(r, color=colour)
        # }}}
# }}}
def on_key_down(key): # {{{
    if   key == keys.A: game.piece.move(-1)
    elif key == keys.D: game.piece.move(1)
    elif key == keys.S: game.piece.rotate(-1)
    elif key == keys.W: game.piece.rotate(1)
    elif key == keys.SPACE: game.piece.drop()
# }}}
def update(dt): game.update(dt)
def draw(): game.draw()
game = Game()
pgzrun.go()
