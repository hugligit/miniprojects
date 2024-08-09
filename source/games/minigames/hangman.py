#!/usr/bin/env python2

from random import *

player_score = 0
computer_score = 0


def hangedman(hangman): # {{{
    graphic = [ # {{{
            # 0 {{{
            """
            +-------+
            |        
            |              
            |              
            |              
            |              
         ===============
            """,
            # }}}
            # 1 {{{
            """
            +-------+
            |       |
            |              
            |              
            |              
            |              
         ===============
            """,
            # }}}
            # 2 {{{
            """
            +-------+
            |       |
            |       O      
            |              
            |              
            |              
         ===============
            """,
            # }}}
            # 3 {{{
            """
            +-------+
            |       |
            |       O      
            |       |      
            |              
            |              
         ===============
            """,
            # }}}
            # 4 {{{
            """
            +-------+
            |       |
            |       O      
            |       |-     
            |              
            |              
         ===============
            """,
            # }}}
            # 5 {{{
            """
            +-------+
            |       |
            |       O      
            |      -|-     
            |              
            |              
         ===============
            """,
            # }}}
            # 6 {{{
            """
            +-------+
            |       |
            |       O      
            |      -|-     
            |      /       
            |              
         ===============
            """,
            # }}}
            # 7 {{{
            """
            +-------+
            |       |
            |       O      
            |      -|-     
            |      / \     
            |              
         ===============
            """,
            # }}}


            ] # }}}
    print graphic[hangman]
# }}}
def start(): # {{{
    print "Let's play a game of Hangman"
    while game():
        pass
    scores()
# }}}
def game(): # {{{
    # SETUP {{{
    dictionary = [ # {{{
            "gnu",
            "kernel",
            "linux",
            "penguin",
            "ubuntu",
            ] # }}}
    word = choice(dictionary)
    word_length = len(word)
    clue = word_length * ["_"]
    tries = 6
    letters_tried = ""
    guesses = 0
    letters_right = 0
    letters_wrong = 0
    global computer_score, player_score

    # }}}
    # ROUND {{{
    while (letters_wrong != tries) and ("".join(clue) != word):
        letter = guess_letter()
        print 16*"-"
        print letters_tried
        print letter
        print 16*"-"
        if len(letter)==1 and letter.isalpha():
            if letters_tried.find(letter) != -1:
                print "You've already picked", letter
            else:
                letters_tried += letter
                first_index = word.find(letter)
                if first_index == -1:
                    letters_wrong += 1
                    print "Sorry,", letter, "isn't what we're looking"
                else:
                    print "Congratulation", letter, "is correct"
                    for i in range(word_length):
                        if letter == word[i]:
                            clue[i] = letter
        else:
            print "Choose another."

        # ROUND_RESULTS {{{
        hangedman(letters_wrong)
        print " ".join(clue)
        print "Guesses: ", letters_tried

        if letters_wrong == tries:
            print "Game Over"
            print "The word was", word
            computer_score += 1
            break
        if "".join(clue) == word:
            print "You win"
            print "The word was", word
            player_score += 1
            break
        # }}}
    # }}}
    return play_again()
# }}}
def guess_letter(): # {{{
    print
    letter = raw_input("Take a guess at our mystery word >>> ")
    letter.strip()
    letter.lower()
    print
    return letter
# }}}
def play_again(): # {{{
    answer = raw_input("Would you like to play again? y/n >>>  ")
    if answer in ("y", "Y"):
        return True
    else:
        print "Thank you very much for playing our game. See you next time!"
# }}}
def scores(): # {{{
    global player_score, computer_score
    print "HIGH SCORES"
    print "Player: ", player_score
    print "Computer: ", computer_score
# }}}

if __name__ == '__main__':
    start()

