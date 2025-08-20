from core.base import Base
from core.renderer import Renderer
from core.camera import Camera
from core.scene import Scene
from core.mesh import Mesh
from core.geometry.boxGeometry import BoxGeometry
from core.material.surfaceMaterial import SurfaceMaterial

###render a basic scence

class Test(Base):

    def initialize(self):
        print("Initializing program ...")

        self.renderer = Renderer()
        self.scene = Scene()
        self.camera = Camera(aspectRatio=800/600)
        self.camera.setPosition([0,0,3])

        geometry = BoxGeometry()
        material = SurfaceMaterial({"useVertexColors": True})
        self.mesh = Mesh(geometry, material)
        self.scene.add(self.mesh)

    def update(self):
        self.mesh.rotateY(0.0514)
        self.mesh.rotateX(0.0337)
        self.renderer.render(self.scene, self.camera)


Test(screenSize=[800,600]).run()
