import pygame, random

SCREEN_WIDTH = 720
SCREEN_HEIGHT = 720
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

class Meteor(pygame.sprite.Sprite):
	def __init__(self):
		super().__init__()
		self.image = pygame.image.load("meteor.png").convert()
		self.image.set_colorkey(BLACK)
		self.rect = self.image.get_rect() #Posicionar sprite

	def update(self):
		self.rect.y += 1

		if self.rect.y > SCREEN_HEIGHT:
			self.rect.y = -10
			self.rect.x = random.randrange(SCREEN_WIDTH)


class Player(pygame.sprite.Sprite):
	def __init__(self):
		super().__init__()
		self.image = pygame.image.load("player.png").convert()
		self.image.set_colorkey(BLACK)
		self.rect = self.image.get_rect() #Posicionar sprite
		self.speed_x = 0
		self.speed_y = 0

	def changespeed(self, x): #Mover personaje con el teclado
		self.speed_x += x

	def update(self):  #Mover personaje con el teclado
		self.rect.x += self.speed_x
		self.rect.y = 510

    #def update(self): #Mover personaje con el mouse
		#mouse_pos = pygame.mouse.get_pos()
		#player.rect.x = mouse_pos[0]
		#player.rect.y = mouse_pos[1]

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





class Game(object):
	def __init__(self):
		self.game_over = False
		self.background = pygame.image.load("background.png").convert()
		self.player = pygame.image.load("player.png").convert()
		pygame.mouse.set_visible(0)
		self.sound = pygame.mixer.Sound("laser5.ogg")

		self.score = 0

		self.meteor_list = pygame.sprite.Group()
		self.laser_list = pygame.sprite.Group()
		self.all_sprite_list = pygame.sprite.Group()

		for i in range(50):
			self.meteor = Meteor()  #Se crea el objeto meteoro 50 veces
			self.meteor.rect.x = random.randrange(SCREEN_WIDTH)
			self.meteor.rect.y = random.randrange(SCREEN_HEIGHT)

			self.meteor_list.add(self.meteor)
			self.all_sprite_list.add(self.meteor)

		self.player = Player()  #Se crea el objeto jugador
		self.laser = Laser()    #Se crea el objeto laser
		self.all_sprite_list.add(self.player)

	def process_events(self):
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return True

			if event.type == pygame.MOUSEBUTTONDOWN: #Si termina el juego
				if self.game_over:
					self.__init__() #Volvemos a correr el juego(reinicio)

			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_LEFT:
					self.player.changespeed(-3)
				if event.key == pygame.K_RIGHT:
					self.player.changespeed(3)
				if event.key == pygame.K_SPACE:
					self.laser = Laser()
					self.laser.rect.x = self.player.rect.x + 45
					self.laser.rect.y = self.player.rect.y - 20
					self.all_sprite_list.add(self.laser)
					self.laser_list.add(self.laser)
					self.sound.play()
        
			if event.type == pygame.KEYUP:
				if event.key == pygame.K_LEFT:
					self.player.changespeed(3)
				if event.key == pygame.K_RIGHT:
					self.player.changespeed(-3)
            
            
		return False


	def run_logic(self):
		if not self.game_over:
			self.all_sprite_list.update()
			# True detecta colision y elimina el objeto, False detecta pero no elimina
			meteor_hit_list = pygame.sprite.spritecollide(self.player, self.meteor_list, True)

			for self.meteor in meteor_hit_list:
				self.score += 1
				print(self.score)
			for self.laser in self.laser_list:
				meteor_hit_list = pygame.sprite.spritecollide(self.laser, self.meteor_list, True)
			for self.meteor in meteor_hit_list:
				self.all_sprite_list.remove(self.laser)
				self.laser_list.remove(self.laser)
				self.score += 1
				print(self.score)
			if self.laser.rect.y < -10:
				self.all_sprite_list.remove(self.laser)
				self.laser_list.remove(self.laser)
            
			if len(self.meteor_list) == 0:  #Si se acaban los meteoritos sale del juego
				self.game_over = True


	def display_frame(self, screen):
		screen.blit(self.background, [0, 0])

		if self.game_over:
			font = pygame.font.SysFont("serif", 25)
			text = font.render("Game Over, Click To Continue", True, BLACK)
			center_x = (SCREEN_WIDTH // 2) - (text.get_width() // 2)
			center_y = (SCREEN_HEIGHT // 2) - (text.get_height() // 2)
			screen.blit(text, [center_x, center_y])

		if not self.game_over:
			self.all_sprite_list.draw(screen)

		pygame.display.flip()

def main(): #Clase principal
	pygame.init()
	screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
	done = False
	clock = pygame.time.Clock()
	game = Game() #Reiniciar juego

	while not done:
		done = game.process_events()
		game.run_logic()
		game.display_frame(screen)
		clock.tick(60)
	pygame.quit()

if __name__ == "__main__":
	main()








		


	
	




