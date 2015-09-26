# -*- coding: utf-8 -*-

import operator
from collections import OrderedDict

def observar(strings_quantity, seasons):
    garden = OrderedDict(((index, '') for index in range(strings_quantity)))
    observations = []

    for poda_cant, fert_str, obs_pos in seasons:
        for string_index in range(strings_quantity):
            # Get string
            season_string = garden[string_index]
            # Podar el string
            season_string = season_string[:len(season_string) - poda_cant]
            # Fertilizar el string
            season_string += fert_str[string_index]
            # Actualizar string
            garden[string_index] = season_string

        # Ordenar strings
        sorted_garden = OrderedDict(sorted(garden.items(), key=operator.itemgetter(1)))
        # Observar string en posición P
        observations.append(list(sorted_garden.items())[obs_pos - 1][0] + 1)

    return observations
