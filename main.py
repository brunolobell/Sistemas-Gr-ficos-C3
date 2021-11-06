import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

from Transformations import *
from Models.Cube import *

def object(faces, verts):
  glBegin(GL_LINES)
  for i in faces:
    for vertex in i:
      glVertex3iv(verts[vertex])
  glEnd()

def main():
    pygame.init()
    display = (500, 500)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL | RESIZABLE)

    gluPerspective(40, display[0] / display[1], 1, 10)
    #glTranslatef(0.0, 0.0, -5)
    translate(0, 0, -5)
    rotate(45, 0, 1, 0)
    i = 0
    while(1):
        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                pygame.quit()
                quit()
        #rotate(1,0,0,1, verts)
        #translate(0,0,1)
        scale(i)
        i+=0.25
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        object(cube_faces, cube_verts)
        pygame.display.flip()
        pygame.time.wait(500)

main()