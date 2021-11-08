import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

from Transformations import *
from Models.Cube import *
from Models.Hall import *

def object(edges, verts):
  glBegin(GL_LINES)
  for i in edges:
    for vertex in i:
      glVertex3fv(verts[vertex])
  glEnd()

def main():
    pygame.init()
    display = (1000, 720)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL | RESIZABLE)

    gluPerspective(40, display[0] / display[1], 1, 10)
    translate(0, 0, -5)
    #rotate(45, 0, 1, 0)
    #scale(.5)
    i = 0
    #glOrtho(1, -1, 1, -1, 100, 0.1)
    #orthogonalProjection(1, -1, 1, -1, 100, 0.1)
    #glFrustum(1, 10, 1, 10, 1, 10)
    perspective(1, 10, 1, 10, 1, 10)
    while(1):
        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                pygame.quit()
                quit()
        #rotate(1,0,0,1, verts)
        #translate(0,0,1)
        #i+=0.25
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        object(cube_faces, cube_verts)
        #object(hall_edges, hall_verts)
        pygame.display.flip()
        pygame.time.wait(500)

main()