import pygame, random
pygame.init()

WHITE = (255,255,255)
BLACK = (0,0,0)

class Meteor(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("meteor.png").convert()
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect() #Posicionar sprite

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("player.png").convert()
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect() #Posicionar sprite

screen = pygame.display.set_mode([720, 720])
clock = pygame.time.Clock()
done = False
score = 0

background = pygame.image.load("background.png").convert()
player = pygame.image.load("player.png").convert()
pygame.mouse.set_visible(0)

meteor_list = pygame.sprite.Group()
all_sprite_list = pygame.sprite.Group()

for i in range(50):
    meteor = Meteor()
    meteor.rect.x = random.randrange(720)
    meteor.rect.y = random.randrange(720)

    meteor_list.add(meteor)
    all_sprite_list.add(meteor)

player = Player()
all_sprite_list.add(player)

while not done:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done = True

	mouse_pos = pygame.mouse.get_pos()
	player.rect.x = mouse_pos[0]
	player.rect.y = mouse_pos[1]

	meteor_hit_list = pygame.sprite.spritecollide(player, meteor_list, True) #True detecta colision y elimina el objeto, False detecta pero no elimina
	for meteor in meteor_hit_list:
		score += 1
		print(score)



	screen.blit(background, [0, 0])

	all_sprite_list.draw(screen)
	pygame.display.flip()
	clock.tick(60)
    

pygame.quit()