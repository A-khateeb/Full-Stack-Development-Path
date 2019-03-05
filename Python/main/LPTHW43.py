'''
Death: This is when the player dies
Central Corridor: The starting point and where the player should defeat the Gothons (Aliens)
Lazer weapon Armory: A neutron bomb to blow the ship up before escaping the pod.
-->It has a keypad that the hero needs to guess the number
The bridge: Another battle scene where the hero places the bomb
Escape pod: Where the hero escapes but only after guessing the number

*Map
 _next_scene
 _opening_scene
*Engine
 _play

*Scene
    _enter
   * Death
   *Central Corridor
   * Lazer weapon armory
   * The bridge
   * Escape pod
 '''


class Scene(object):
    def enter(self):
        pass

class Death(object):
    def enter(self):
        pass

class CentralCorridor(object):
    def enter(self):
        pass

class LazerWeponArmory(object):
    def enter(self):
        pass

class EscapePod(object):
    def enter(self):
        pass

class Engine(object):
    def __init__(self,scene_map):
        pass
    def play(self):
        pass
class Map(object):
    def __init__(self, start_scene):
        pass
    def next_scene(self, scene_name):
        pass
    def opening_scene(self):
        pass
a_map = Map("central_corridor")
a_engine = Engine(a_map)
a_game.play()
