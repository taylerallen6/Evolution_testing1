import pygame
import numpy as np


class Organism(pygame.sprite.Sprite):
	def __init__(self, pos, size, color, health_damage, foods_group):
		super().__init__()
		self.life_iters = 0
		
		self.health_damage = health_damage
		self.speed = 3
		self.color = color
		self.size = size
		self.pos = pos

		self.health = 100
		self.foods_group = foods_group

		self.rect = pygame.Rect(self.pos, self.size)

		self.screen = pygame.display.get_surface()
		pygame.draw.rect(self.screen, self.color, self.rect)

	def move_up(self):
		self.pos[1] -= self.speed
	def move_down(self):
		self.pos[1] += self.speed
	def move_left(self):
		self.pos[0] -= self.speed
	def move_right(self):
		self.pos[0] += self.speed

	def automate(self, moves):
		if moves[0]:
			self.move_up()
		if moves[1]:
			self.move_down()
		if moves[2]:
			self.move_left()
		if moves[3]:
			self.move_right()

	def update(self):
		self.life_iters += 1

		self.health -= self.health_damage
		if self.health <= 0:
			self.kill()
			# print("DEAD")
			# print("ORGANISM LIFE ITERS: ", self.life_iters)

		for food in pygame.sprite.spritecollide(self, self.foods_group, 1):
			self.health += food.health_increase
			# print("FOOD")
			# print("ORGANISM HEALTH INCREASED: ", self.health)

		self.rect = pygame.Rect(self.pos, self.size)
		pygame.draw.rect(self.screen, self.color, self.rect)



class Food(pygame.sprite.Sprite):
	def __init__(self, pos, size, color, health_increase):
		super().__init__()
		self.health_increase = health_increase
		self.color = color
		self.size = size
		self.pos = pos

		self.rect = pygame.Rect(self.pos, self.size)

		self.screen = pygame.display.get_surface()
		pygame.draw.rect(self.screen, self.color, self.rect)

	def update(self):
		self.rect = pygame.Rect(self.pos, self.size)
		pygame.draw.rect(self.screen, self.color, self.rect)

