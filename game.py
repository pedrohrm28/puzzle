from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys
import math
from quadro import quadro
from peca import peca
import random
import time

def init():
    glClearColor(0.0, 0.0, 0.0, 1.0)
    gluOrtho2D(-2.0, 2.0, -2.0, 2.0)

ciano_positions = [(random.uniform(-1,1), random.uniform(-1,1)), (random.uniform(-1,1), random.uniform(-1,1)), (random.uniform(-1,1), random.uniform(-1,1)), (random.uniform(-1,1), random.uniform(-1,1))]
selected_piece = -1  # Índice da peça selecionada (-1 = nenhuma selecionada)
mouse_x, mouse_y = 0, 0
mouse_pressed = False
rotation_angle_ciano = [0.0, 0.0, 0.0, 0.0]  # Angulos de rotação para cada peça

def desenha():
    glClearColor(1.0, 1.0, 1.0, 1.0)
    glClear(GL_COLOR_BUFFER_BIT)
    
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    
    glPushMatrix()
    glTranslatef(0.25, 0.25, 0.0)
    quadro()
    glPopMatrix()
    
    for i, (x, y) in enumerate(ciano_positions):
        peca(x, y, i, rotation_angle_ciano[i])
    
    glutSwapBuffers()

encaixadas = [False] * len(ciano_positions)

def verificarEncaixe():
    global ciano_positions, encaixadas
    
    for i, (px, py) in enumerate(ciano_positions):
        # Verifica se a peça está encaixada
        if 0 <= px <= 0.5 and 0 <= py <= 0.5:
            encaixadas[i] = True
        else:
            encaixadas[i] = False
            

def todasPecasEncaixadas():
    global encaixadas
    print(encaixadas)
    return all(encaixadas)


def encaixeAutomatico():
    global ciano_positions, selected_piece, rotation_angle_ciano, encaixadas
    
    # Coordenadas do centro do quadro
    quadro_x, quadro_y = 0.0, 0.0
    
    # Tamanho do quadro
    quadro_largura, quadro_altura = 1.0, 1.0
    
    # Tamanho dos quadrados da grade
    quadrado_lado = quadro_largura / 2.0
    
    if selected_piece != -1:
        px, py = ciano_positions[selected_piece]
        # Verifica qual quadrado da grade a peça está cobrindo
        for j in range(4):
            gx = quadro_x + (j % 2) * quadrado_lado
            gy = quadro_y + (j // 2) * quadrado_lado
            
            # Calcula as coordenadas da peça na grade rotacionada
            rotated_px = (px - quadro_x) * math.cos(math.radians(rotation_angle_ciano[selected_piece])) - (py - quadro_y) * math.sin(math.radians(rotation_angle_ciano[selected_piece])) + quadro_x
            rotated_py = (px - quadro_x) * math.sin(math.radians(rotation_angle_ciano[selected_piece])) + (py - quadro_y) * math.cos(math.radians(rotation_angle_ciano[selected_piece])) + quadro_y
            
            # Verifica se a peça cobre pelo menos metade do quadrado
            if (gx - quadrado_lado / 2) <= rotated_px <= (gx + quadrado_lado / 2) and (gy - quadrado_lado / 2) <= rotated_py <= (gy + quadrado_lado / 2):
                # Ajusta a posição da peça para ficar no centro do quadrado da grade
                ciano_positions[selected_piece] = (gx, gy)
                return


def reiniciar():
    global ciano_positions, encaixadas

    for i, (px, py) in enumerate(ciano_positions):      
        ciano_positions[i] = (random.uniform(-1,1),random.uniform(-1,1))  # Ajusta a posição
            

def mousePressed(button, state, x, y):
    global mouse_x, mouse_y, mouse_pressed, ciano_positions, selected_piece, rotation_angle_ciano
    
    if button == GLUT_LEFT_BUTTON: 
        if state == GLUT_DOWN: # pressionar o botao esquerdo do mouse
            for i, (px, py) in enumerate(ciano_positions):
                if px - 0.25 <= mouse_x <= px + 0.25 and py - 0.25 <= mouse_y <= py + 0.25:
                    if selected_piece == i:
                        selected_piece = -1  # Desseleciona a peça se já estiver selecionada
                    else:
                        selected_piece = i  # Seleciona a peça clicada
                        mouse_pressed = True
        elif state == GLUT_UP: # soltar o botao esquerdo do mouse
            if selected_piece != -1:
                encaixeAutomatico()  # Encaixa a peça quando soltar o botão do mouse
                verificarEncaixe()  # Verifique se a peça se encaixou corretamente na grade
                if todasPecasEncaixadas():  # Verifique se o quebra-cabeça foi resolvido
                    print("Jogo finalizado / Pressione o scroll do mouse para reiniciar")                 
            mouse_pressed = False
    elif button == GLUT_RIGHT_BUTTON and state == GLUT_DOWN and selected_piece != -1: # pressionar botao direito do mouse para rotacionar a peça
        rotation_angle_ciano[selected_piece] += 45.0
    elif button == GLUT_MIDDLE_BUTTON and state == GLUT_DOWN: # pressionar o (scroll) do mouse
        reiniciar()

def mouseMotion(x, y): # movimentação do mouse
    global mouse_x, mouse_y
    
    mouse_x, mouse_y = (x - 250) / 250, (250 - y) / 250
    
    if mouse_pressed and selected_piece != -1:
        ciano_positions[selected_piece] = (mouse_x, mouse_y)
    
    glutPostRedisplay()
   

def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
    glutInitWindowSize(500, 500)
    glutInitWindowPosition(50, 50)
    glutCreateWindow("Puzzle")
    glutDisplayFunc(desenha)
    glutMouseFunc(mousePressed)
    glutMotionFunc(mouseMotion)
    init()
    glutMainLoop()

main()