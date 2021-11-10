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

def main():
    # Iniciação do pygame
    pygame.init()
    # Setar variáveis para o display
    display = (1000, 720)
    # DOUBLEBUF -> recomendado para o uso do Opengl
    # OPENGL -> Cria um display renderizado pelo OPENGL
    # RESIZABLE -> 
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL | RESIZABLE)

    gluPerspective(90, display[0] / display[1], 1, 100) 
    glLightfv(GL_LIGHT0, GL_POSITION,  (-40, 200, 100, 0.0))
    glLightfv(GL_LIGHT0, GL_AMBIENT, (0.2, 0.2, 0.2, 1.0))
    glLightfv(GL_LIGHT0, GL_DIFFUSE, (0.5, 0.5, 0.5, 1.0))
    glLightfv(GL_LIGHT0, GL_SPECULAR, (0.7, 0.7, 0.7, 1.0))
    glEnable(GL_LIGHT0)
    glEnable(GL_LIGHTING)
    glEnable(GL_DEPTH_TEST)
    glEnable(GL_COLOR_MATERIAL)
    glShadeModel(GL_SMOOTH)  

    obj = OBJ("teste.obj", swapyz=True)
    translate(0, 0, -5)
    scale(0.1)
    s = 0.1
    while(1):
      for ev in pygame.event.get():
        if ev.type == pygame.QUIT:
          pygame.quit()
          quit()
        elif ev.type == pygame.constants.KEYDOWN and ev.key == pygame.constants.K_1:
          rotate(1,1,0,0)
        elif ev.type == pygame.constants.KEYDOWN and ev.key == pygame.constants.K_2:
          rotate(1,0,1,0)
        elif ev.type == pygame.constants.KEYDOWN and ev.key == pygame.constants.K_3:
          rotate(1,0,0,1)
        elif ev.type == pygame.constants.KEYDOWN and ev.key == pygame.constants.K_KP1:
          translate(1,0,0)
        elif ev.type == pygame.constants.KEYDOWN and ev.key == pygame.constants.K_KP2:
          translate(0,1,0)
        elif ev.type == pygame.constants.KEYDOWN and ev.key == pygame.constants.K_KP3:
          translate(0,0,1)
        elif ev.type == pygame.constants.KEYDOWN and ev.key == pygame.constants.K_KP4:
          translate(-1,0,0)
        elif ev.type == pygame.constants.KEYDOWN and ev.key == pygame.constants.K_KP5:
          translate(0,-1,0)
        elif ev.type == pygame.constants.KEYDOWN and ev.key == pygame.constants.K_KP6:
          translate(0,0,-1)
        elif ev.type == pygame.constants.KEYDOWN and ev.key == pygame.constants.K_UP:
          s += 1
          scale(s)
        elif ev.type == pygame.constants.KEYDOWN and ev.key == pygame.constants.K_DOWN:
          s -= 1
          scale(s)
        elif ev.type == pygame.constants.KEYDOWN and ev.key == pygame.constants.K_o:
          orthogonalProjection(1, 2, 5, 4, 5, 10)
        elif ev.type == pygame.constants.KEYDOWN and ev.key == pygame.constants.K_p:
          perspective(1, 2, 4, 5, 0.1, 100)

      glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
      glCallList(obj.gl_list)
      pygame.display.flip()
      #pygame.time.wait(200)

main()