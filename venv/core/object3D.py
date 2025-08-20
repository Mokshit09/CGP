from core.matrix import Matrix

class Object3D:
    def __init__(self):
        self.transform = Matrix.makeIdentity()
        self.parent = None
        self.children = []

    def add(self, child):
        self.children.append(child)
        child.parent = self

    def remove(self, child):
        self.children.remove(child)
        child.parent = None

    #calculate transform relative to root
    def getWorldMatrix(self):
        if self.parent == None:
            return self.transform
        else:
            return self.parent.getWorldMatrix() @ self.transform
        
    def getDescendantList(self):
        descendants = []

        nodesToProcess = [self]
        while len(nodesToProcess)> 0 :
            node = nodesToProcess.pop(0)
            descendants.append(node)
            nodesToProcess = node.children + nodesToProcess
        return descendants
    
    # apply geometric transformations 
    def applyMatrix(self, matrix, localCoord=True):
        if localCoord:
            self.transform = self.transform @ matrix
        else:
            self.transform = matrix @ self.transform 
    def translate(self, x,y,z, localCoord=True):
        m = Matrix.makeTranslation(x,y,z)
        self.applyMatrix(m, localCoord) 
    def rotateX(self, angle, localCoord=True):
        m = Matrix.makeRotationX(angle)
        self.applyMatrix(m, localCoord) 
    def rotateY(self, angle, localCoord=True):
        m = Matrix.makeRotationY(angle)
        self.applyMatrix(m, localCoord) 
    def rotateZ(self, angle, localCoord=True):
        m = Matrix.makeRotationZ(angle)
        self.applyMatrix(m, localCoord) 
    def scale(self, s, localCoord=True):
        m = Matrix.makeScale(s)
        self.applyMatrix(m, localCoord)

    def getPosition(self):
        return [self.transform.item((0,3)), 
                self.transform.item((1,3)),
                self.transform.item((2,3)) ]
    
    def getWorldPosition(self):
        worldTranform = self.getWorldMatrix()
        return [worldTranform.item((0,3)),
                worldTranform.item((1,3)),
                worldTranform.item((2,3))]
    
    def setPosition(self, position):
        self.transform[0, 3] = position[0]
        self.transform[1, 3] = position[1]
        self.transform[2, 3] = position[2]

    


