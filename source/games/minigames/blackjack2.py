import pgzrun
import pygame
import random
import os

PATH = 'D:\\Documents\\Marcel\\Projects\\pgzero\\ghoulash\\images\\blackjack\\'

SUITS = ('spade', 'heart', 'diamond', 'club',)

BUTTON_Y = 250
BUTTON_H = 25
TEXT_OFFSET_Y = 6

button_hit = { # {{{
        'x': 10,
        'y': BUTTON_Y,
        'width': 53,
        'height': 25,
        'text': 'Hit!',
        'text_offset_x': 13,
        'text_offset_y': TEXT_OFFSET_Y,
        } # }}}
button_stand = { # {{{
        'x': 70,
        'y': BUTTON_Y,
        'width': 53,
        'height': 25,
        'text': 'Stand',
        'text_offset_x': 4,
        'text_offset_y': TEXT_OFFSET_Y,
        } # }}}
button_play_again = { # {{{
        'x': 10,
        'y': BUTTON_Y,
        'width': 113,
        'height': 25,
        'text': 'Play again',
        'text_offset_x': 17,
        'text_offset_y': TEXT_OFFSET_Y,
        } # }}}

def update(): # {{{
    pass
# }}}
def reset(): # {{{
    global deck
    global player_hand, dealer_hand
    global round_over


    deck = []


    for suit in SUITS:
        for rank in range(1, 14):
            deck.append({ 'suit': suit, 'rank': rank, })

    round_over = False

    player_hand = []
    take_card(player_hand)
    take_card(player_hand)


    dealer_hand = []
    take_card(dealer_hand)
    take_card(dealer_hand)

# }}}
def take_card(hand): # {{{
    hand.append(deck.pop(random.randrange(len(deck))))
    # }}}
def on_key_down(key): # {{{
    global  round_over

    if not round_over:
        if key == keys.H:
            take_card(player_hand)
            if get_total(player_hand) >= 21:
                round_over = True
        elif key == keys.S:
            round_over = True

        if round_over:
            while get_total(dealer_hand) < 17:
                take_card(dealer_hand)
    else: reset()
        # }}}
def get_total(hand): # {{{
    all_cards = [min(i['rank'], 10) for i in hand]
    total = sum(all_cards)
    if 1 in all_cards and total <= 11: total += 10
    return total
# }}}
def hand_has_won(this_hand, other_hand): # {{{
    this_score = get_total(this_hand)
    other_score = get_total(other_hand)
    return (
            this_score <= 21 
            and (other_score > 21 or this_score > other_score)
            )
# }}}
def is_mouse_in_button(button): # {{{
    x = button['x']
    w = button['width']
    y = button['y']
    h = button['height']
    mouse_x, mouse_y = pygame.mouse.get_pos()
    return (
        x <= mouse_x < x + w
        and
        y <= mouse_y < y + h
    )
# }}}
def on_mouse_up(): # {{{
    global round_over

    if not round_over:
        if is_mouse_in_button(button_hit):
            take_card(player_hand)
            if get_total(player_hand) >= 21:
                round_over = True
        elif is_mouse_in_button(button_stand):
            round_over = True

    if round_over:
        while get_total(dealer_hand) < 17:
            take_card(dealer_hand)
    elif is_mouse_in_button(button_play_again):
        reset()

    # }}}
def draw_button(button): # {{{
    x = button['x']
    w = button['width']
    y = button['y']
    h = button['height']
    t = button['text']
    text_offset_x = button['text_offset_x']
    text_offset_y = button['text_offset_y']

    if is_mouse_in_button(button):
        color=(255, 202, 75)
    else:
        color=(255, 127, 57)

    screen.draw.filled_rect(
            Rect(x, y, w, h),
            color=color
            )
    screen.draw.text(t, (x + text_offset_x, y + text_offset_y))
# }}}
def draw(): # {{{
    global  round_over
    card_spacing = 60
    margin_x = 10
    margin_y = 10
    screen.fill('#005500')


    for i, card in enumerate(dealer_hand):
        suit = card['suit']
        rank = card['rank']
        image = '%s_%s' % (suit, rank)
        if not round_over and i == 0:
            image = 'card_face_down'
        screen.blit('%s%s.png' % (PATH, image), (i*card_spacing + margin_x, margin_y + 20))

    for i, card in enumerate(player_hand):
        suit = card['suit']
        rank = card['rank']
        screen.blit('%s%s_%s.png' % (PATH, suit, rank), (i*card_spacing + margin_x, margin_y + 130))

    for i, card in enumerate(dealer_hand):
        suit = card['suit']
        rank = card['rank']
    if round_over:
        screen.draw.text('Total: %d' % get_total(dealer_hand), (margin_x, 10))
    else:
        screen.draw.text('Total: %s' % '?', (margin_x, 10))

    screen.draw.text('Total: %d' % get_total(player_hand), (margin_x, 230))

    if round_over:
        if hand_has_won(player_hand, dealer_hand):
            message = 'Player wins'
        elif hand_has_won(dealer_hand, player_hand):
            message = 'Dealer wins'
        else:
            message = 'Draw'



        screen.draw.text(message, (margin_x, 268))

    if not round_over:
        draw_button(button_hit)
        draw_button(button_stand)
    else:
        draw_button(button_play_again)

    # screen.draw.filled_rect(Rect(10, 250, 53, 25), color=(255, 127, 57))
    # screen.draw.text('Hit!', (23, 256))
    # screen.draw.filled_rect(Rect(70, 250, 53, 25), color=(255, 127, 57))
    # screen.draw.text('Stand', (73, 256))

    # screen.draw.filled_rect(Rect(10, 250, 113, 25), color=(255, 127, 57))
    # screen.draw.text('Play again', (27, 256))

    # }}}



reset()
pgzrun.go()

# BCP {{{
mydir = os.path.dirname('__file__')
# mydir = os.getcwd()
mydir = (os.path.dirname(os.path.realpath('__file__')))
mydir = os.path.join(mydir, 'images', 'tinted', 'clouds_1.png')
# }}}
