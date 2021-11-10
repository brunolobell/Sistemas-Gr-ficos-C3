import numpy as np
from OpenGL.GL import *
from OpenGL.GLU import *

def rotate(angle, x, y, z):
    if z == 1:
        R = [[np.cos(angle), -np.sin(angle), 0, 0], [np.sin(angle), np.cos(angle), 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]]
    if x == 1:
        R = [[1, 0, 0, 0], [0, np.cos(angle), -np.sin(angle), 0], [0, np.sin(angle), np.cos(angle), 0], [0, 0, 0, 1]]
    if y == 1:
        R = [[np.cos(angle), 0, np.sin(angle), 0], [0, 1, 0, 0], [-np.sin(angle), 0, np.cos(angle), 0], [0, 0, 0, 1]]
    glMultMatrixf(R)

def scale(newScale):
    if (newScale > 0):
        S = [[newScale, 0, 0, 0], [0, newScale, 0, 0], [0, 0 , newScale, 0], [0, 0, 0, 1]]
        glMultMatrixf(np.transpose(S))
    else:
        print("Scale must be bigger than 0")

def translate(x, y, z):
    T = [[1,0,0,x],[0,1,0,y],[0,0,1,z],[0,0,0,1]]
    glMultMatrixf(np.transpose(T))

def orthogonalProjection(left, right, bottom, top, near, far):
    p1 = 2.0 / (right - left)
    p2 = 2.0 / (top - bottom)
    p3 = -2.0 / (far - near)
    p4 = -(right + left) / (right - left)
    p5 = -(top + bottom) / (top - bottom)
    p6 = -(far + near) / (far - near)
    P = [[p1, 0, 0, 0], [0, p2, 0, 0], [0, 0, p3, 0], [p4, p5, p6, 1]]
    glMultMatrixf(P)

def perspective(left, right, bottom, top, near, far):
    P = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
  
    P[0][0] = 2 * near / (right - left); 
    P[1][1] = 2 * near / (top - bottom); 
    P[2][0] = (right + left) / (right - left); 
    P[2][1] = (top + bottom) / (top - bottom); 
    P[2][2] = -(far + near) / (far - near); 
    P[2][3] = -1; 
    P[3][2] = -2 * far * near / (far - near); 
    glMultMatrixf(P)

def setPixel(x, y):
    glBegin(GL_POINTS)
    print((x,y))
    glVertex2i(int(x), int(y))
    glEnd()

def DDA(x0, y0, x1, y1):
    dx = x1 - x0;
    dy = y1 - y0;

    if abs(dx) > abs(dy):
        steps = abs(dx)
    else:
        steps = abs(dy)
 
    Xinc = dx / steps
    Yinc = dy / steps
 
    X = x0;
    Y = y0;
    for i in range(steps + 1):
        setPixel(X, Y)
        X += Xinc
        Y += Yinc
