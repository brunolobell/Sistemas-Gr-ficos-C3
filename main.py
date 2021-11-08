import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

from Transformations import *
from Models.Cube import *
from Models.Hall import *
from Models.Test import *

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
    translate(0, 0, -8)
    #rotate(58, 1, 0, 0)  #58 fica pro meu lado, 61 fica legal tambem
    scale(0.03)
    i = 0
    #orthogonalProjection(1, -1, 1, -1, 100, 0.1)
    #perspective(1, 10, 1, 10, 1, 10)

    while(1):
        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                pygame.quit()
                quit()

        #rotate(1,1,0,0)
        #translate(0,0,1)
        #i+=0.25
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        #object(cube_faces, cube_verts)
        #object(hall_faces, hall_verts)
        object(test_faces, test_verts)

        pygame.display.flip()
        pygame.time.wait(500)

main()

'Funções do OpenGL'
  #glFrustum(1, 10, 1, 10, 1, 10)
  #glFrustum(1, 10, 1, 10, 1, 10)
