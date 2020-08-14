import pygame, sys
pygame.init()

#Definir colores
BLACK   = (0,0,0)
WHITE   = (255,255,255)
GREEN   = (0,255,0)
RED   = (255,0,0)
BLUE   = (0,0,255)

size = (800, 500)

#crear ventana
screen = pygame.display.set_mode(size)

#Controlar FPS
clock = pygame.time.Clock() 

# Coordenadas del cuadrado
cord_x = 400
cord_y = 200

# Velocidad a la que se movera mi cuadrado
speed_x = 3
speed_y = 3

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    
    ### ---- LOGICA DEL JUEGO
    if (cord_x > 720 or cord_x < 0):
        speed_x *= -1
    if (cord_y > 420 or cord_y < 0):
        speed_y *= -1

    cord_x += speed_x
    cord_y += speed_y
    ### ---- LOGICA DEL JUEGO

    #Color de Pantalla
    screen.fill(WHITE)

    ### ZONA DE DIBUJO
    pygame.draw.rect(screen, RED, (cord_x, cord_y, 80, 80))
    
    
    ### ZONA DE DIBUJO

    #Actualizar ventana
    pygame.display.flip()
    clock.tick(60)