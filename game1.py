import pygame
import numpy as np
import time

from sprites1 import Organism, Food


class Game1():

	def __init__(self):
		pygame.init()
		self.game_iters = 0

		self.screen_size = (600,600)
		self.screen = pygame.display.set_mode(self.screen_size)
		self.done = False

		self.clock = pygame.time.Clock()

		self.foods = pygame.sprite.RenderPlain()
		self.organisms = pygame.sprite.RenderPlain()
		self.all_sprites = pygame.sprite.RenderPlain()

		# size = min(self.screen_size)
		# rand_pos = np.random.randint(size-size+50, size-50, size=2)
		# self.player = Organism(rand_pos,
		# 	(30,30),
		# 	(255,0,0),
		# 	health_damage=.5,
		# 	foods_group=self.foods)
		# self.all_sprites.add(self.player)

		self.max_food_count = 20
		self.rand_food_time = 60
		self.rand_food_count = self.rand_food_time
		self.create_foods(10)

		self.create_organisms(5)


	def create_foods(self, n_foods):
		for i in range(n_foods):
			size = min(self.screen_size)
			rand_pos = np.random.randint(size-size+50, size-50, size=2)
			self.foods.add(Food(
				rand_pos,
				(10,10),
				(0,255,0),
				health_increase=20))
		
		self.all_sprites.add(self.foods)

	def create_organisms(self, n_organisms):
		for i in range(n_organisms):
			size = min(self.screen_size)
			rand_pos = np.random.randint(size-size+50, size-50, size=2)
			self.organisms.add(Organism(
				rand_pos,
				(30,30),
				(255,0,0),
				health_damage=.5,
				foods_group=self.foods))
		
		self.all_sprites.add(self.organisms)


	def controls(self):
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				self.done = True

		# pressed = pygame.key.get_pressed()
		# if pressed[pygame.K_UP]: self.player.move_up()
		# if pressed[pygame.K_DOWN]: self.player.move_down()
		# if pressed[pygame.K_LEFT]: self.player.move_left()
		# if pressed[pygame.K_RIGHT]: self.player.move_right()

		for organism in self.organisms:
			organism.automate(np.random.randint(2, size=4))


	def game_logic(self):
		if len(self.foods) < self.max_food_count:
			if self.rand_food_count <= 0:
				self.create_foods(2)
				self.rand_food_count = self.rand_food_time
			self.rand_food_count -= 1

		if len(self.organisms) <= 0:
			self.done = True


	def start(self):
		while not self.done:
			self.game_iters += 1

			self.controls()
			self.game_logic()

			self.screen.fill((0,0,0))
			self.all_sprites.update()
			pygame.display.update()
			self.clock.tick(60)

		print("GAME ITERS: ", self.game_iters)
		pygame.quit()
