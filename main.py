import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

from objLoader import *
from Transformations import *
from Models.Cube import *
from Models.Hall import *
from Models.Test import *
from Models.Cone import *
from Models.Cube2 import *

def object(edges, verts):
  glBegin(GL_LINES)
  for i in edges:
    glColor3fv((10, 100, 1))
    for vertex in i:
      glVertex3fv(verts[vertex])
  glEnd()

def main():
    pygame.init()
    display = (1000, 720)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL | RESIZABLE)

    gluPerspective(90, display[0] / display[1], 1, 100) 
    #translate(0, 0, -8)
    #rotate(45, 0, 1, 0)  #58 fica pro meu lado, 61 fica legal tambem
    #scale(0.1)
    i = 0
    #orthogonalProjection(1, -1, 1, -1, 100, 0.1)
    #perspective(1, 10, 1, 10, 1, 10)
    tx, ty = (0,0)
    zpos = 5
    obj = OBJ("Models/C3.obj", swapyz=True)
    translate(tx/20., ty/20., - zpos)
    scale(0.1)
    while(1):
        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                pygame.quit()
                quit()

        #rotate(1,1,0,0)
        #translate(0,0,1)
        #i+=0.25
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        #bresenham(0, 0, 350, 350)
        #object(cube_faces, cube_verts)
        #object(hall_faces, hall_verts)
        #object(cone_faces, cone_verts)
        #object(cube2_faces, cube2_verts)
        rotate(0.5, 1, 0, 0)
        #rotate(1, 0, 1, 0)
        glCallList(obj.gl_list)
        pygame.display.flip()
        pygame.time.wait(500)

main()

'Funções do OpenGL'
  #glFrustum(1, 10, 1, 10, 1, 10)
  #glFrustum(1, 10, 1, 10, 1, 10)
