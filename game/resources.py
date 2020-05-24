import pyglet


def center_image(image):
    """Sets an image's anchor point to its center"""
    image.anchor_x = image.width / 2
    image.anchor_y = image.height / 2


# Tell pyglet where to find the resources
pyglet.resource.path = ['./resources']
pyglet.resource.reindex()

# Load the three main resources and get them to draw centered
player_image = pyglet.resource.image("alienBlue_jump.png")
center_image(player_image)

monster_image = pyglet.resource.image("spider_walk1.png")
center_image(monster_image)

worm_image = pyglet.resource.image('worm_walk.png')
center_image(worm_image)

background = pyglet.resource.image('future.jpg')

# bullet_image = pyglet.resource.image("bullet.png")
# center_image(bullet_image)

# asteroid_image = pyglet.resource.image("asteroid.png")
# center_image(asteroid_image)

# The engine flame should not be centered on the ship. Rather, it should be shown 
# behind it. To achieve this effect, we just set the anchor point outside the
# # image bounds.
# engine_image = pyglet.resource.image("engine_flame.png")
# engine_image.anchor_x = engine_image.width * 1.5
# engine_image.anchor_y = engine_image.height / 2
