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
    for x in range(100, 700, 100):
        pygame.draw.rect(screen, BLACK, (x, 230, 50, 50))
        pygame.draw.line(screen, GREEN, (x, 0), (x, 100), 5)
    
    
    ### ZONA DE DIBUJO

    #Actualizar ventana
    pygame.display.flip()