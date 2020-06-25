import random


class Game(object):

    def __init__(self):
        self.hand = []

    def get_user_item(self):
        hand_p = input('''
        Select (r)ock, (p)aper, or (s)cissors:\n
        ''')
        if hand_p not in 'rpsRPS':
            print('Invalid selection. Please try again.')
            self.get_user_item()
        elif hand_p == 'r' or hand_p == 'R':
            hand_p = 'rock'
            return hand_p
        elif hand_p == 'p' or hand_p == 'P':
            hand_p = 'paper'
            return hand_p
        elif hand_p == 's' or hand_p == 'S':
            hand_p = 'scissor'
            return hand_p

    def computer_hand(self):
        hand_c = random.choice(['r', 'p', 's'])
        if hand_c == 'r':
            return 'rock'
        elif hand_c == 'p':
            return 'paper'
        elif hand_c == 's':
            return 'scissor'
