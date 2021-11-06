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
