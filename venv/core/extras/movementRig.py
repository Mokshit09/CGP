from core.object3D import Object3D

class MovementRig(Object3D):
    def __init__(self, unitsPerSec =1, degreesPerSec = 60):
        super().__init__()

        self.lookAttachment = Object3D()
        self.children = [self.lookAttachment]
        self.lookAttachment.parent = self

        self.unitsPerSecond = unitsPerSec
        self.degreesPerSecond = degreesPerSec
        # customizable key mappings 
        # defaults: WASDRF (move), QE (turn), TG (look) 
        self.KEY_MOVE_FORWARDS = "w" 
        self.KEY_MOVE_BACKWARDS = "s" 
        self.KEY_MOVE_LEFT = "a" 
        self.KEY_MOVE_RIGHT = "d" 
        self.KEY_MOVE_UP = "r"  
        self.KEY_MOVE_DOWN = "f" 
        self.KEY_TURN_LEFT = "q" 
        self.KEY_TURN_RIGHT = "e" 
        self.KEY_LOOK_UP = "t" 
        self.KEY_LOOK_DOWN = "g"
 


    ##adding and removing objects appiles to look attachment
    def add(self, child):
        self.lookAttachment.add(child)

    def remove(self, child):
        self.lookAttachment.remove(child)

    def update(self, inputObject , deltaTime):
        moveAmount = self.unitsPerSecond* deltaTime
        rotateAmount = self.degreesPerSecond *(3.1415926 / 180) *deltaTime
        if inputObject.isKeyPressed(self. KEY_MOVE_FORWARDS):
            self.translate( 0, 0, -moveAmount ) 
        if inputObject.isKeyPressed(self. KEY_MOVE_BACKWARDS):
            self.translate( 0, 0, moveAmount )
        if inputObject.isKeyPressed(self.KEY_MOVE_LEFT):
            self.translate( -moveAmount, 0, 0 )
        if inputObject.isKeyPressed(self.KEY_MOVE_RIGHT):
            self.translate( moveAmount, 0, 0 )
        if inputObject.isKeyPressed(self.KEY_MOVE_UP):
            self.translate( 0, moveAmount, 0 )
        if inputObject.isKeyPressed(self.KEY_MOVE_DOWN):
            self.translate( 0, -moveAmount, 0 )
        if inputObject.isKeyPressed(self.KEY_TURN_RIGHT):
            self.rotateY( -rotateAmount )
        if inputObject.isKeyPressed(self.KEY_TURN_LEFT):
            self.rotateY( rotateAmount )
        if inputObject.isKeyPressed(self.KEY_LOOK_UP):
            self.lookAttachment.rotateX( rotateAmount )
        if inputObject.isKeyPressed(self.KEY_LOOK_DOWN):
            self.lookAttachment.rotateX( -rotateAmount )