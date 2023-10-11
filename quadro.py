from OpenGL.GL import *

def quadro():
    glColor3f(1.0, 0.0, 0.0)
    
    glPushMatrix()
    glLineWidth(2.0)
    
    # Linhas horizontais
    glBegin(GL_LINES)
    glVertex2f(-0.5, 0.0)
    glVertex2f(0.5, 0.0)
    glVertex2f(-0.5, -0.5)
    glVertex2f(0.5, -0.5)
    glVertex2f(-0.5, 0.5)
    glVertex2f(0.5, 0.5)
    glEnd()
    
    
    # Linhas verticais
    glBegin(GL_LINES)
    glVertex2f(0.0, 0.5)
    glVertex2f(0.0, -0.5)
    glVertex2f(-0.5, 0.5)
    glVertex2f(-0.5, -0.5)
    glVertex2f(0.5, 0.5)
    glVertex2f(0.5, -0.5)
    glEnd()
    
    glPopMatrix()
