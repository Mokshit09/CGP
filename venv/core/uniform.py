from OpenGL.GL import * 

class Uniform:
    def __init__(self, dataType, data): 
        # Type of data: int | bool | float | vec2 | vec3 | vec4
        self.dataType = dataType
        # Data to be sent to uniform variable
        self.data = data
        # Reference for variable location in program
        self.variableRef = None

    # Get and store reference for program variable with the given name
    def locateVariable(self, programRef, variableName):
        self.variableRef = glGetUniformLocation(programRef, variableName)

    # Store data in uniform variable previously located
    def uploadData(self):
        # If the program does not reference the variable, then exit
        if self.variableRef == -1:
            return 
        


        if self.dataType == "int":
            glUniform1i(self.variableRef, self.data)
        elif self.dataType == "bool":
            glUniform1i(self.variableRef, self.data)
        elif self.dataType == "float":
            glUniform1f(self.variableRef, self.data)
        elif self.dataType == "vec2":
            glUniform2f(self.variableRef, self.data[0], self.data[1])
        elif self.dataType == "vec3":
            glUniform3f(self.variableRef, self.data[0], self.data[1], self.data[2])
        elif self.dataType == "vec4":
            glUniform4f(self.variableRef, self.data[0], self.data[1], self.data[2], self.data[3])
        elif self.dataType == "mat4":
            glUniformMatrix4fv(self.variableRef, 1, GL_TRUE, self.data)
            
