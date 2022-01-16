import pygame

class MenuButton:
	def __init__(self, type, rect, surfaces=None, text=None, centered=None, task=None):
		self.rect = rect
		self.type = type
		self.pressed = False
		self.on_press = task
		if not surfaces: 
			self.button_surfaces = [pygame.Surface((10, 10), pygame.SRCALPHA) for i in range(2)]
		else:
			self.button_surfaces = [pygame.Surface.copy(surface) for surface in surfaces]
		self.button_surfaces[0] = pygame.transform.scale(self.button_surfaces[0], (self.rect[2], self.rect[3]))
		self.button_surfaces[1] = pygame.transform.scale(self.button_surfaces[1], (self.rect[2], self.rect[3]))
		if text:
			t_rect = text.get_rect()
			if t_rect.width >= self.rect.width-20:
				num = int(t_rect.width/(t_rect.width/(self.rect.width-20)))
				text = pygame.transform.scale(text, (num, t_rect.h))
			center = text.get_rect(center=(self.rect[2]/2, self.rect[3]/2))
			self.button_surfaces[0].blit(text, center)
			self.button_surfaces[1].blit(text, center)
		if centered: self.rect.center = centered
		self.surface = self.button_surfaces[0]


	def logic(self, mouse, mouse_btn):
		if not mouse_btn[0] and self.pressed:
			self.pressed = False
			if self.on_press:
				self.on_press()
		if self.rect.collidepoint(mouse) and mouse_btn[0]:
			self.pressed = True

	def draw(self, screen):
		if self.pressed:
			screen.blit(self.button_surfaces[1], self.rect)
		else:
			screen.blit(self.button_surfaces[0], self.rect)
		
