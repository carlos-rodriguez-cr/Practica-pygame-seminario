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


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    
    #Pantalla de color blanco
    screen.fill(WHITE)

    ### ZONA DE DIBUJO

    #pygame.draw.line(screen, GREEN, [0,100], [200,300], 5)
    pygame.draw.rect(screen, BLUE, (50,300, 200, 80))
    pygame.draw.rect(screen, BLUE, (50,100, 80, 200))
    pygame.draw.circle(screen, BLUE, (390,260), 120, 70)
    pygame.draw.rect(screen, BLUE, (530,300, 200, 80))
    pygame.draw.rect(screen, BLUE, (530,100, 80, 200))

    ### ZONA DE DIBUJO



    #Actualizar ventana
    pygame.display.flip()

