import pgzrun
import random
import os

PATH = 'D:\\Documents\\Marcel\\Projects\\pgzero\\ghoulash\\images\\blackjack\\'

SUITS = ('spade', 'heart', 'diamond', 'club',)


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

    # output = ['Player hand:']
    for i, card in enumerate(player_hand):
        suit = card['suit']
        rank = card['rank']
        # output.append('suit:%s, rank:%s' % (suit, rank))
        screen.blit('%s%s_%s.png' % (PATH, suit, rank), (i*card_spacing + margin_x, margin_y + 130))
    # output.append('Total: %s' % get_total(player_hand))

    # output.append('')
    # output.append('Dealer hand:')
    for i, card in enumerate(dealer_hand):
        suit = card['suit']
        rank = card['rank']
        # if not round_over and i == 0:
        #     output.append('(Card hidden)')
        # else:
        #     output.append('suit:%s, rank:%s' % (suit, rank))
    if round_over:
        # output.append('Total: %s' % get_total(dealer_hand))
        screen.draw.text('Total: %d' % get_total(dealer_hand), (margin_x, 10))
    else:
        # output.append('Total: ?')
        screen.draw.text('Total: %s' % '?', (margin_x, 10))

    screen.draw.text('Total: %d' % get_total(player_hand), (margin_x, 230))

    if round_over:
    #     output.append('')

    #     if hand_has_won(player_hand, dealer_hand):
    #         output.append('Player wins')
    #     elif hand_has_won(dealer_hand, player_hand):
    #         output.append('Dealer wins')
    #     else:
    #         output.append('Draw')


        if hand_has_won(player_hand, dealer_hand):
            message = 'Player wins'
        elif hand_has_won(dealer_hand, player_hand):
            message = 'Dealer wins'
        else:
            message = 'Draw'



        screen.draw.text(message, (margin_x, 268))
        # result = 0 if player_score > dealer_score else 1 if dealer_score > player_score else 2
        # results = [
        #         'Player wins',
        #         'Dealer wins',
        #         'Draw',
        #         ]
        # output.append(results[result])

    # screen.draw.text('\n'.join(output), (300, 15))
    # }}}



reset()
pgzrun.go()

# BCP {{{
mydir = os.path.dirname('__file__')
# mydir = os.getcwd()
mydir = (os.path.dirname(os.path.realpath('__file__')))
mydir = os.path.join(mydir, 'images', 'tinted', 'clouds_1.png')
# }}}
