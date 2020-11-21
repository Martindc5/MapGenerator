import matplotlib.pyplot as plt
import settings as s
import terrains
import draw_map as dwm
import noise_function as nf



# Generating the map matrix whit elements between -1 and 1
# It interpolates a plain terrain, a mountainous terrain and a semi montainous terrain
map = nf.lerp(terrains.plain(), terrains.low_mountainous(), terrains.mountainous())

# Colorize the map
world = dwm.add_color(map)

# Add forest and all plants you wont to create
terrains.biomes(map, world)

# Create with the matplotlib the image and
plt.imshow(world, vmin=0, vmax=255)
plt.title('Seed: ' + str(s.seed))
plt.show()
