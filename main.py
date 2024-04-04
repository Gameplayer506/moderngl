import pygame as pg
import moderngl as mgl
import sys
from cube import *
from camera import Camera
from light import Light

class GraphicsEngine:
    def __init__(self, win_size=(1280, 720)):
        #set up pygame 
        pg.init()
        self.WIN_SIZE = win_size
        pg.display.gl_set_attribute(pg.GL_CONTEXT_MAJOR_VERSION, 3)
        pg.display.gl_set_attribute(pg.GL_CONTEXT_MINOR_VERSION, 3)
        pg.display.gl_set_attribute(pg.GL_CONTEXT_PROFILE_MASK  , pg.GL_CONTEXT_PROFILE_CORE)
        pg.display.set_mode(self.WIN_SIZE, flags=pg.OPENGL | pg.DOUBLEBUF)
        self.ctx = mgl.create_context()
        pg.event.set_grab(True)
        pg.mouse.set_visible(False)

        #view internal walls with self.ctx.front_face = "cw"

        self.ctx.enable(flags=mgl.DEPTH_TEST | mgl.CULL_FACE)
        self.clock = pg.time.Clock()
        self.time = 0
        self.delta_time = 0

        #bring in from imports
        self.light = Light()
        self.camera = Camera(self)
        self.scene = Cube(self)

    def check_events(self):
        #check for closing window or esc pressed
        for event in pg.event.get():
            if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                self.scene.destroy()
                pg.quit()
                sys.exit()

    def render(self):
        #clear frame then render and send to display
        self.ctx.clear(color=(0.1, 0.2, 0.3))
        self.scene.render()
        pg.display.flip()

    def get_time(self):
        self.time = pg.time.get_ticks() * 0.001

    def run(self):
        while True:
            self.get_time()
            self.check_events()
            self.camera.update()
            self.render()
            self.delta_time = self.clock.tick(60)


if __name__ == "__main__":
    app = GraphicsEngine()
    app.run()