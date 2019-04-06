'''
Gothons from Planet Percal #25
\Death
Central Corridor
Laser Wepon Armory
Escape Pod
\
NOUNS
Alien
Player
Ship
Maze
Room
Scene
Gothon
Escape Pod
Planet
Map
Engine
Death
Central Corridor
Lazer Wepon Armory
The Bridge

The classes
Map
   -next_scene
   -opening_scene
Engine
   -play
Scene
    -enter
    Death
    Central Corridor
    Lazer Wepon Armory
    Escape Pod
'''

class Scene(object):
    def enter(self):
        pass

class Engine(object):
    def __init__(self, scene_map):
        pass
    def play(self):
        pass

class Death(Scene):
    def enter(self):
        pass

class CentralCorridor(Scene):
    def enter(self):
        pass

class LazerWeponArmory(Scene):
    def enter(self):
        pass

class EscapePod(Scene):
    def enter(self):
        pass

class Map(object):
    def __init__(self, start_scene):
        pass
    def next_scene(self, scene_name):
        pass

    def opening_scen(self):
        pass

a_map = Map("central_corridor")
a_game = Engine(a_map)
a_game.play()
