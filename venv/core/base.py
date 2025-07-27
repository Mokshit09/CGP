import pygame 
import sys 
from core.input import Input


class Base(object):
    def __init__(self, screenSize=[512, 512]):
        # initialize all pygame modules
        pygame.init()
        # indicate rendering details
        displayFlags = pygame.DOUBLEBUF | pygame.OPENGL
        # initialize buffers to perform antialiasing
        pygame.display.gl_set_attribute(pygame.GL_MULTISAMPLEBUFFERS, 1)
        pygame.display.gl_set_attribute(pygame.GL_MULTISAMPLESAMPLES, 4)
        # use a core OpenGL profile for cross-platform compatibility
        pygame.display.gl_set_attribute(
        pygame.GL_CONTEXT_PROFILE_MASK,
        pygame.GL_CONTEXT_PROFILE_CORE)
        # create and display the window
        self.screen = pygame.display.set_mode(screenSize, displayFlags )
                # set the text that appears in the title bar of the window
        pygame.display.set_caption("Graphics Window")
        # determine if main loop is active
        self.running = True
        # manage time-related data and operations
        self.clock = pygame.time.Clock()
        self.input = Input()

        # number of seconds application has been running 
        self.time = 0
        # seconds since iteration of run loop 
        self.deltaTime = self.clock.get_time() / 1000
        
        # increment time application has been running 
        self.time += self.deltaTime
    
    def initialize(self):
        pass

    def update(self):
        pass

    def run(self):
        self.initialize()
        ## main loop ##
        while self.running:
            ## calculate deltaTime ##
            self.deltaTime = self.clock.tick(60) / 1000  # Convert milliseconds to seconds
            # print("Delta Time:", self.deltaTime)  # Debugging: check if it's updating

            ## process input ##
            self.input.update()
            if self.input.quit:
                self.running = False 

            ## update ##
            self.update()

            ## render ##
            pygame.display.flip()  # Display image on screen

        pygame.quit()
        sys.exit()

    
    
    # def run(self):
    #     self.initialize()
    #     ## main loop ##
    #     while self.running:
    #         ## process input ##
    #         self.input.update() 
    #         if self.input.quit:
    #             self.running = False 
    #         ## update ##
    #         self.update()
    #         ## render ##
    #         # display image on screen
    #         pygame.display.flip()
    #         # pause if necessary to achieve 60 FPS
    #         self.clock.tick(60)
    #     pygame.quit()
    #     sys.exit()
