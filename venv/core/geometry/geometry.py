from core.attribute import Attribute

class Geometry(object):
    def __init__(self):
        self.attributes = {}

        self.vertexCount = None

    def addAttribute(self, dataType, variableName, data):
        self.attributes[variableName]= Attribute(dataType, data)

    def countVertices(self):
        attrib = list(self.attributes.values())[0]
        self.vertexCount = len(attrib.data)

    def applyMatrix(self, matrix, variableName="vertexPosition"):
        oldPositionData = self.attributes[variableName].data
        newPositionData = []

        for oldPos in oldPositionData:
            newPos = oldPos.copy()
            #add homogenous fourth coordinate
            newPos.append(1)
            newPos = matrix @ newPos
            #remove the fourth position 
            newPos = list(newPos[0:3])
            newPositionData.append(newPos)

        self.attributes[variableName].data = newPositionData
        self.attributes[variableName].uploadData()

    def merge(self, otherGeometry):
        for variablesName, attributeObject in self.attributes.items():
            attributeObject.data += otherGeometry.attributes[variablesName].data

            attributeObject.uploadData()
        self.countVertices()
        