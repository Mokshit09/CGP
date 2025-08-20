from core.openGLUtils import OpenGLUtils
from core.uniform import Uniform
from OpenGL.GL import *

class Material(object):

    def __init__(self, vertexShaderCode, fragmentShaderCore):
        self.programRef = OpenGLUtils.initializeProgram(vertexShaderCode,fragmentShaderCore)

        #store uniform objects, indexed by name of associated variable

        self.uniforms = {}

        self.uniforms["modelMatrix"] = Uniform("mat4", None)
        self.uniforms["viewMatrix" ]= Uniform("mat4", None)
        self.uniforms["projectionMatrix"] = Uniform("mat4", None)

        #store OpenGL render Settings, indexed by variable name
        self.settings = {}
        self.settings["drawStyle"] = GL_TRIANGLES

    def addUniform(self, dataType, variableName, data):
        self.uniforms[variableName] = Uniform(dataType, data)

    #initiable all uniform variable refernce 
    def locateUniform(self):
        for variableName, uniformObject in self.uniforms.items():
            uniformObject.locateVariable(self.programRef, variableName)

    #OpenGL with render setting
    def updateRenderSettings(self):
        pass

    #convenience method for setting multiple material

    def setProperties(self, properties):
        for name,data in properties.items():
            if name in self.uniforms.keys():
                self.uniforms[name].data = data
            elif name in self.settings.keys():
                self.settings[name] = data
            else:
                raise Exception("Material has no proprty named:" + name)
            
    