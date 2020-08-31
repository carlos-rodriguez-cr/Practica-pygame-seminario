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
	def update(self):
		self.rect.y += 1
		if self.rect.y > 720:
			self.rect.y = -10
			self.rect.x = random.randrange(720)

class Laser(pygame.sprite.Sprite):
	def __init__(self):
		super().__init__()
		self.image = pygame.image.load("laser.png").convert()
		self.image.set_colorkey(BLACK)
		self.rect = self.image.get_rect() #Posicionar sprite
	def update(self):
		self.rect.y -= 5
		if self.rect.y > 720:
			self.rect.y = -10
			self.rect.x = random.randrange(720)



class Player(pygame.sprite.Sprite):
	def __init__(self):
		super().__init__()
		self.image = pygame.image.load("player.png").convert()
		self.image.set_colorkey(BLACK)
		self.rect = self.image.get_rect() #Posicionar sprite
		self.speed_x = 0
		self.speed_y = 0

	def changespeed(self, x): #Mover personaje con el mouse
		self.speed_x += x

	#ef update(self): #Mover personaje con el mouse
		#mouse_pos = pygame.mouse.get_pos()
		#player.rect.x = mouse_pos[0]
		#player.rect.y = mouse_pos[1]
	def update(self): #Mover personaje con el mouse
		self.rect.x += self.speed_x
		player.rect.y = 610

screen = pygame.display.set_mode([720, 720])
clock = pygame.time.Clock()
done = False
score = 0

background = pygame.image.load("background.png").convert()
player = pygame.image.load("player.png").convert()
pygame.mouse.set_visible(0)

meteor_list = pygame.sprite.Group()
laser_list = pygame.sprite.Group()
all_sprite_list = pygame.sprite.Group()

for i in range(50):
    meteor = Meteor()
    meteor.rect.x = random.randrange(720)
    meteor.rect.y = random.randrange(720)

    meteor_list.add(meteor)
    all_sprite_list.add(meteor)

player = Player()
all_sprite_list.add(player)
sound = pygame.mixer.Sound("laser5.ogg")

while not done:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done = True

		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_LEFT:
				player.changespeed(-3)
			if event.key == pygame.K_RIGHT:
				player.changespeed(3)
			if event.key == pygame.K_SPACE:
				laser = Laser()
				laser.rect.x = player.rect.x + 45
				laser.rect.y = player.rect.y - 20
				all_sprite_list.add(laser)
				laser_list.add(laser)
				sound.play()

		if event.type == pygame.KEYUP:
			if event.key == pygame.K_LEFT:
				player.changespeed(3)
			if event.key == pygame.K_RIGHT:
				player.changespeed(-3)


	all_sprite_list.update()
	for laser in laser_list:
		meteor_hit_list = pygame.sprite.spritecollide(laser, meteor_list, True)
		for meteor in meteor_hit_list:
			all_sprite_list.remove(laser)
			laser_list.remove(laser)
			score += 1
			print(score)
		if laser.rect.y < -10:
			all_sprite_list.remove(laser)
			laser_list.remove(laser)


	# True detecta colision y elimina el objeto, False detecta pero no elimina
	meteor_hit_list = pygame.sprite.spritecollide(player, meteor_list, True)
	for meteor in meteor_hit_list:
		score += 1
		print(score)

	screen.blit(background, [0, 0])

	all_sprite_list.draw(screen)
	pygame.display.flip()
	clock.tick(60)


pygame.quit()
