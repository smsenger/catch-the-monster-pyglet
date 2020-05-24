import time
import pyglet
from game import player, monster, worm, resources
from random import randint

from config import WIDTH, HEIGHT

# Set up a window
game_window = pyglet.window.Window(WIDTH, HEIGHT)

# Create the container for our graphics
main_batch = pyglet.graphics.Batch()

# Load the main music
theme_song = pyglet.media.load('./resources/futurebackground.wav')
music = pyglet.media.Player()
music.queue(theme_song)

# Set up the two top labels
score_label = pyglet.text.Label(text="Caught 0", x=15, y=75, bold='True', batch=main_batch)
lives = pyglet.text.Label(text="Lives 3", x=15, y=55, bold='True', batch=main_batch)

# Initialize the player sprite
hero = player.Player(x=400, y=300, batch=main_batch)
goblin = monster.Monster(x=randint(0, WIDTH), y=randint(0,HEIGHT), batch=main_batch)

# Store all objects that update each frame in a list
game_objects = [hero, goblin]

# Add a new monster
worm_monster = worm.Worm(x=randint(0, WIDTH), y=randint(0, HEIGHT), batch=main_batch)
game_objects.append(worm_monster)

# Tell the main window that the player object responds to events
game_window.push_handlers(hero.key_handler)

@game_window.event
def on_draw():
    game_window.clear()
    resources.background.blit(0, 0)
    main_batch.draw()

lives = 3
score = 0
is_drawing = True  # Controls whether to show movement


def game_over():
    global is_drawing

    is_drawing = False
    music.pause()
    winning = pyglet.media.load('./resources/superhero-fanfare.wav')
    winning.play()

def you_lose():
    global is_drawing

    is_drawing = False
    music.pause()
    winning = pyglet.media.load('./resources/boo.wav')
    winning.play()



def update(dt):

    global score
    global lives

    if is_drawing:

        for obj in game_objects:
            obj.update(dt)

        # To avoid handling collisions twice, we employ nested loops of ranges.
        # This method also avoids the problem of colliding an object with itself.
        for i in range(len(game_objects)):
            for j in range(i + 1, len(game_objects)):
                # for k in range(i + 2, len(game_objects)):

                obj_1 = game_objects[i]
                obj_2 = game_objects[j]
                # obj_3 = game_objects[k]

            # Make sure the objects haven't already been killed
                if not obj_1.dead and not obj_2.dead:
                    if obj_1.collides_with(obj_2):
                        obj_1.handle_collision_with(obj_2)
                        obj_2.handle_collision_with(obj_1)
                
                # if not obj_1.dead and not obj_3.dead:
                #     if obj_3.collides_with(obj_1):
                #         lives -= 1
                #         if lives == 0:
                #             print('Booooooo! Go away!')
                #             you_lose()


        #check status of health points
        for opponent in [obj for obj in game_objects if isinstance(obj, monster.Monster) and obj.didgethit]:
            obj.didgethit=False
            score += 10
            print('we increased the score')
            score_label.text = f"Caught {score}"
            if score < 100:
                gotcha_sound_effect = pyglet.media.load('./resources/destruction.wav', streaming=False)
                gotcha_sound_effect.play()

            if score == 100:
                print('You have ended arachnid infestation!!!!!!!!!!!!!!')
                game_over()

            

        # Get rid of dead objects
        for to_remove in [obj for obj in game_objects if obj.dead]:
            # Remove the object from any batches it is a member of
            to_remove.delete()

            # Remove the object from our list
            game_objects.remove(to_remove)



           


if __name__ == "__main__":
    # Update the game 120 times per second
    pyglet.clock.schedule_interval(update, 1 / 120.0)

    music.play()
    # Tell pyglet to do its thing
    pyglet.app.run()