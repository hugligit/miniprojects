import pgzero, pgzrun

bob = Actor('alien')

TILE = max(bob.width, bob.height)
TITLE = "Goulash"
W = 8
H = 5
WIDTH = W * TILE
HEIGHT = H * TILE

print( dir(bob))

def draw():
    P = Rect((0, 0), (TILE, TILE))
    C = [(0, 0, 64), (0, 32, 64)]
    for c in range(W):
        for r in range(H):
            screen.draw.filled_rect(
                Rect((c*TILE, r*TILE), (TILE, TILE)), 
                C[(c+r)%2]
                )

    bob.draw()

# def update():
#     if keyboard.s: bob.y +=  1 # TILE

def on_key_down(key, mod, unicode):
    print("%s, %s, %s" % (key, mod, unicode))
    if key == keys.W: bob.y -= TILE
    if key == keys.A: bob.x -= TILE
    if key == keys.S: bob.y += TILE
    if key == keys.D: bob.x += TILE
    print(bob.pos)


# slimearm = Actor('alien')
# # slimearm.topright = 0, 10
# slimearm.pos = 100, 56

# WIDTH = slimearm.width - 10
# HEIGHT = slimearm.height + 10

# def draw():
#     # screen.clear()
#     screen.fill((16, 16, 28))
#     slimearm.draw()

# def update():
#      slimearm.left += 2
#      if slimearm.left > WIDTH:
#          slimearm.right = 0

# def on_mouse_down(pos):
#      if slimearm.collidepoint(pos):
#          set_alien_hurt()
#      else:
#          print("you missed me!")

# def set_alien_hurt():
#      print("Eek!")
#      # sounds.eep.play()
#      slimearm.image = 'alien_hurt'
#      clock.schedule_unique(set_alien_normal, 1.0)

# def set_alien_normal():
#      slimearm.image = 'alien'


pgzrun.go()
