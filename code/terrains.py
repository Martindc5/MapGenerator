import numpy as np
import noise
import settings as s
import noise_function as nf
import draw_map as dm

# Values for the noise function of biomes()
scale = 1000.0
octaves = 6
persistence = 0.5
lacunarity = 2.0

def mountainous():
    lin = np.linspace(0, 8, s.shape[0], endpoint=False)
    x, y = np.meshgrid(lin, lin)
    return nf.perlin(x, y, seed= s.seed)

def plain():
    lin = np.linspace(0, 3, s.shape[0], endpoint=False)
    x, y = np.meshgrid(lin, lin)
    return nf.perlin(x, y, seed= s.seed)

def low_mountainous():
    lin = np.linspace(0, 5, s.shape[0], endpoint=False)
    x, y = np.meshgrid(lin, lin)
    return nf.perlin(x, y, seed= s.seed)

def biomes(map, world):
    forest = np.zeros(s.shape)
    for i in range(s.shape[0]):
        for j in range(s.shape[1]):
            forest[i][j] = noise.pnoise2(i/scale,
                                        j/scale,
                                        octaves= octaves,
                                        persistence= persistence,
                                        lacunarity= lacunarity,
                                        repeatx= s.shape[0],
                                        repeaty= s.shape[1],
                                        base=0)
    for i in range(s.shape[0]):
        for j in range(s.shape[1]):
            if forest[i][j] > 0.1 and map[i][j] <= dm.interval_green and map[i][j] > dm.interval_beach:
                world[i][j] = [0,100,0]

