import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

from objLoader import *
from Transformations import *

def main():
    # Iniciação do pygame
    pygame.init()
    # Setar variáveis para o display
    display = (1000, 720)
    # DOUBLEBUF -> recomendado para o uso do Opengl
    # OPENGL -> Cria um display renderizado pelo OPENGL
    # RESIZABLE -> 
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL | RESIZABLE)

    gluPerspective(120, display[0] / display[1], 1, 100) 
    glLightfv(GL_LIGHT0, GL_POSITION,  (-40, 200, 100, 0.0))
    glLightfv(GL_LIGHT0, GL_AMBIENT, (0.2, 0.2, 0.2, 1.0))
    glLightfv(GL_LIGHT0, GL_DIFFUSE, (0.5, 0.5, 0.5, 1.0))
    glLightfv(GL_LIGHT0, GL_SPECULAR, (0.7, 0.7, 0.7, 1.0))
    glEnable(GL_LIGHT0)
    glEnable(GL_LIGHTING)
    glEnable(GL_DEPTH_TEST)
    glEnable(GL_COLOR_MATERIAL)
    glShadeModel(GL_SMOOTH) 

    # Objetos criação
    obj1 = OBJ("Models/chao.obj")
    obj2 = OBJ("Models/AtrasC3.obj")
    obj3 = OBJ("Models/Cupula.obj")
    obj4 = OBJ("Models/FrenteC3.obj")
    # obj = OBJ("Models/Cubo2.obj")

    # Definições iniciais para apresentar o projeto
    translate(0, 0, -5)
    scale(0.1)
    s = 0.1

    while(1):
      # Eventos do pygame
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
          perspective(10,20,25,30,40,35)
      
      # Limpar a tela
      glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
  
      # Apresenta na tela uma lista
      # glCallList(obj1.gl_list)
      # glCallList(obj2.gl_list)
      # glCallList(obj3.gl_list)
      # glCallList(obj4.gl_list)

      # DDD Algoritmo
      # C
      DDA(1, 5, 5, 5)
      DDA(1, 5, -1, 3)
      DDA(1, 1, -1, 3)
      DDA(1, 1, 5, 1)
      # 3
      DDA(8, 5, 12, 5)
      DDA(12, 5, 14, 3)
      DDA(14, 3, 10, 3)
      DDA(14, 3, 10, 3)
      DDA(14, 3, 8, 0)

      pygame.display.flip()
    
main()