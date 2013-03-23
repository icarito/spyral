try:
    import _path
except NameError:
    pass
import spyral
import sys
import math

SIZE = (640, 480)
BG_COLOR = (0, 0, 0)

class Game(spyral.Scene):
    def __init__(self, color):
        spyral.Scene.__init__(self, SIZE)
        bg = spyral.Image(size=SIZE)
        bg.fill(color)
        k =spyral.Rect(160,120,640-320,480-240)
        bg.draw_rect( (0, 100, 0), k.topleft, k.size)
        self.set_background(bg)
        
        s = spyral.Sprite(self)
        s.image = spyral.Image(size=(20,20)).draw_circle((255, 255, 255), (10,10), 10)
        s.pos = 300, 200
        
        a1 = spyral.Animation('pos', spyral.animator.LinearTuple(start = (0,0), finish= SIZE),
                                           duration = 3,
                                           loop = False)
        a2 = spyral.Animation('pos', spyral.animator.LinearTuple(start = (0, SIZE[1]), finish= (SIZE[0], 0)),
                                           duration = 3,
                                           loop = False)
        a3 = a1 + a2
        a3.loop = True
        s.animate(a3)
        s.anchor = 'center'
        
        v = spyral.ViewPort(self)
        v.crop = k
        v.add(s)
        
        self.register("system.quit", sys.exit)


        
if __name__ == "__main__":
    spyral.director.init(SIZE) # the director is the manager for your scenes
    spyral.director.run(scene=Game((100, 100, 100))) # This will run your game. It will not return.