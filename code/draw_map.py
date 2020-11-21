import numpy as np
import random
import settings as s


# RGB colors:
blue = [55, 95, 125]
beach = [238, 214, 175]
green = [34, 139, 34]
snow = [255, 250, 250]
mountain = [70, 60, 60]

# All of this variables indicate the high of the diferent terrain tipes:
interval_blue = -0.4        # From -1 to this number  (wather)
interval_beach = -0.35
interval_green = 0.35
interval_mountain = 0.60    # From this number to 1



# This function colorize the map matrix dependin on the values/ altitude of every point
def add_color(world):
    color_world = []
    for x in range(s.shape[0]):
        color_world.append([])
        for y in range(s.shape[1]):
            color_world[x].append([0,0,0])

    for i in range(s.shape[0]):
        for j in range(s.shape[1]):
            if world[i][j] < interval_blue:
                tono = 15*tonos(-1, world[i][j])
                color_world[i][j] = suma_matrices([0,0,tono], blue)
            elif world[i][j] >= interval_blue and world[i][j] < interval_beach:
                tono = 10*tonos(interval_blue, world[i][j])
                color_world[i][j] = suma_matrices([0,-tono,0], beach)
            elif world[i][j] >= interval_beach and world[i][j] < interval_green:
                tono = 5*tonos(interval_beach, world[i][j])
                color_world[i][j] = suma_matrices([tono,tono,tono], green)
            elif world[i][j] >= interval_green and world[i][j] <  interval_mountain:
                tono = 5*tonos(interval_green, world[i][j])
                color_world[i][j] = suma_matrices([tono,tono,tono], mountain)
            elif world[i][j] >= interval_mountain:
                color_world[i][j] = snow
    return color_world

def tonos(a,b):
    ton = 0
    while b > a:
        ton = ton + 1
        b = b - 0.05
    return ton

def suma_matrices(a,b):
    matriz = [0,0,0]
    for y in range(3):
            matriz[y] = a[y] + b[y]
    return matriz
