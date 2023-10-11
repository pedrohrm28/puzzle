from OpenGL.GL import *

def peca(x, y, index, rotation_angle):
    glColor3f(0.0, 1.0, 1.0)
    
    glPushMatrix()
    glTranslatef(x, y, 0.0)
    glRotatef(rotation_angle, 0.0, 0.0, 1.0)
    glBegin(GL_QUADS)
    glVertex2f(-0.25, -0.25)
    glVertex2f(0.25, -0.25)
    glVertex2f(0.25, 0.25)
    glVertex2f(-0.25, 0.25)
    glEnd()
    glPopMatrix()
