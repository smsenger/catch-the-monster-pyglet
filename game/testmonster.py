from datetime import datetime, timedelta 
import pyglet
from pyglet.window import key
from . import physicalobject, resources

from random import randint

class Monster(physicalobject.PhysicalObject):
    """Physical object that responds to user input"""

    def __init__(self, *args, **kwargs):
        super().__init__(img=resources.monster_image, *args, **kwargs)

        self.counter = 0
        self.change_at = randint(50,100)
        self.randomize()
        self.health = 10
        self.didgethit = False
        self.lasthit = None
        self.nexthit = None
        

    def update(self, dt):
        # Do all the normal physics stuff
        super().update(dt)
        # self.velocity_x = 0
        # self.velocity_y = 0
        self.counter += 1
        if self.counter >= self.change_at:
            self.counter = 0

            # The randomize() function alters
            # the current velocity of the monster.
            self.randomize()

    def randomize(self):
        self.velocity_x = randint(20, 130)
        self.velocity_y = randint(20, 130)
        
        # This expression means: there is a 50%
        # chance we will change our horizontal direction.
        if randint(0, 100) > 20:
            self.velocity_x *= -1
            
        # This expression means: there is a 50%
        # chance we will change our vertical direction.
        if randint(0, 100) > 20:
            self.velocity_y *= -1        

    def delete(self):
        # We have a child sprite which must be deleted when this object
        # is deleted from batches, etc.
        super().delete()

    def handle_collision_with(self, other_object):
        self.dead = True
        current_time = datetime.now()
        print(current_time)
        print(self.nexthit)
        print(not self.lasthit)
        if not self.lasthit or current_time > self.nexthit:
            print(current_time > self.nexthit)
            self.nexthit = current_time + timedelta(seconds=5)
            self.lasthit = current_time
            self.didgethit = True
            self.health -= 1
            if self.health == 0:
                self.dead = True
                print('hello hello')






#mostly original Monster class code
import pyglet
from pyglet.window import key
from . import physicalobject, resources

from random import randint

class Monster(physicalobject.PhysicalObject):
    """Physical object that responds to user input"""

    def __init__(self, *args, **kwargs):
        super().__init__(img=resources.monster_image, *args, **kwargs)

        self.counter = 0
        self.change_at = randint(50,100)
        self.randomize()

    def update(self, dt):
        # Do all the normal physics stuff
        super().update(dt)
        # self.velocity_x = 0
        # self.velocity_y = 0
        self.counter += 1
        if self.counter >= self.change_at:
            self.counter = 0

            # The randomize() function alters
            # the current velocity of the monster.
            self.randomize()

    def randomize(self):
        self.velocity_x = randint(50, 150)
        self.velocity_y = randint(50, 150)
        
        # This expression means: there is a 50%
        # chance we will change our horizontal direction.
        if randint(0, 100) > 20:
            self.velocity_x *= -1
            
        # This expression means: there is a 50%
        # chance we will change our vertical direction.
        if randint(0, 100) > 20:
            self.velocity_y *= -1        

    def delete(self):
        # We have a child sprite which must be deleted when this object
        # is deleted from batches, etc.
        super().delete()

    def handle_collision_with(self, other_object):
        self.dead = True
