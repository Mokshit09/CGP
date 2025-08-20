from core.base import Base
from core.renderer import Renderer
from core.camera import Camera
from core.scene import Scene
from core.mesh import Mesh
from core.geometry.sphereGeometry import SphereGeometry
from core.material.material import Material
from core.extras.axesHelper import AxesHelper
from core.extras.gridHelper import GridHelper
from math import pi

###render a basic scence

class Test(Base):

    def initialize(self):
        print("Initializing program ...")

        self.renderer = Renderer()
        self.scene = Scene()
        self.camera = Camera(aspectRatio=800/600)
        self.camera.setPosition([0.5,1,5])

        ##axes and  grid
        axes = AxesHelper(axisLength=2)
        self.scene.add(axes)

        grid = GridHelper(size=30, gridColor= [1,1,1], centerColor=[1,1,0])
        grid.rotateX(-pi/2)
        self.scene.add(grid)

        #change the mesh and material after this

        # geometry = SphereGeometry(radius = 3, radiusSegments=128, heightSegments=64)
        # vsCode = """ 
        #     uniform mat4 modelMatrix; 
        #     uniform mat4 viewMatrix; 
        #     uniform mat4 projectionMatrix; 
        #     in vec3 vertexPosition; 
        #     in vec3 vertexColor; 
        #     out vec3 color; 
        #     uniform float time; 
        #     void main() 
        #     {
        #         float offset = 0.2 * sin(8.0 * vertexPosition.x + time); 
        #         vec3 pos = vertexPosition + vec3(0.0, offset, 0.0);
        #         gl_Position = projectionMatrix* viewMatrix* modelMatrix* vec4(pos, 1);
        #         color = vertexColor;
        #     }
        # """ 

        # fsCode = """ 
        # in vec3 color; 
        # uniform float time; 
        # out vec4 fragColor; 
        # void main() 
        #     {
        #     float r = abs(sin(time));
        #     vec4 c = vec4(r, -0.5*r, -0.5*r, 0.0);
        #     fragColor = vec4(color, 1.0) + c; 
        #     } 
        # """


        # material = Material(vsCode, fsCode)
        # material.addUniform("float", "time", 0)
        # material.locateUniform()

        # #time variable
        # self.time = 0


        # self.mesh = Mesh(geometry, material)
        # self.scene.add(self.mesh)

    def update(self):
        # self.mesh.rotateY(0.0514)
        # self.mesh.rotateX(0.0337)
        # self.time += 1/60
        # self.mesh.material.uniforms["time"].data = self.time
        self.renderer.render(self.scene, self.camera)


Test(screenSize=[800,600]).run()
