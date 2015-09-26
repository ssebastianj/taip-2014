# -*- coding: utf-8 -*-

import itertools


def calc_gallantry_count(players):
    turns_yielded = turns_count = len(players) // 2
    turns_combinations = itertools.combinations_with_replacement([0, 1], 3)
    players = sorted(players)

    for turns in turns_combinations:
        players_list = players[:]
        german = giannina = 0

        for turn in turns:
            max_player = players_list.pop()

            if turn:
                giannina += max_player
            else:
                german += max_player

        giannina += sum(players_list)
        turns_yielded -= 1 if german > giannina else 0

    return -1 if (turns_yielded == turns_count) else turns_yielded
