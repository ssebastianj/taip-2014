# -*- coding: utf-8 -*-


def check_mixing_randomness(cards):
    mix_state = 'B'

    for card1, card2 in zip(cards, cards[1:]):
        if card1[0] == card2[0] or card1[1] == card2[1]:
            mix_state =  'M'
            break
    return mix_state
