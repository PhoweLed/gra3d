key_switch_camera = 'c' 
key_switch_mode = 'z' 
key_forward = 'w'  
key_back = 's'      
key_left = 'a'      
key_right = 'd'     
key_up = 'e'      
key_down = 'q'    

key_turn_left = 'n' 
key_turn_right = 'm'
class Hero():
    def __init__(self,pos,land):
        self.land = land
        self.mode = True
        self.hero = loader.loadModel("steve.glb")
        self.hero.setScale(0.1)
        self.hero.setPos(pos)
        self.hero.reparentTo(render)
        self.hero.setHpr(0,90,0)
        self.hero.reparentTo(render)
        self.cameraBind()

    def cameraBind(self):
        base.disableMouse()
        base.camera.setHpr(90,90,90)
        base.camera.reparentTo(self.hero)
        base.camera.setPos(5,8,15)
        
