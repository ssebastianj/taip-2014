# -*- coding: utf-8 -*-

def calc_minimum_travels(east_stations):
    cant_stations = len(east_stations)
    paralelas_arriba = set()
    paralelas_abajo = set()
    rectas = set()

    for west_station in range(cant_stations - 1):
        e_station_1 = east_stations[west_station]
        e_station_2 = east_stations[west_station + 1]

        if e_station_1 < e_station_2:
            if e_station_1 > (west_station + 1):
                paralelas_abajo.update((e_station_1, e_station_2))
            elif e_station_1 < (west_station + 1):
                paralelas_arriba.update((e_station_1, e_station_2))
            else:
                rectas.update((e_station_1, e_station_2))

    travels = 1 if paralelas_arriba else 0
    travels += 1 if paralelas_abajo else 0
    travels += 1 if rectas else 0
    travels += cant_stations - len(paralelas_arriba) - len(paralelas_abajo) - len(rectas)

    return travels
