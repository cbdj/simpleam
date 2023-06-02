import pygame
import simpleam
pygame.init()

screen = pygame.display.set_mode((1280, 720), pygame.SCALED | pygame.FULLSCREEN)
clock = pygame.time.Clock()
from ui import MenuButton
font = pygame.font.SysFont("Bold", 80)
simpleam.simpleam_init()
global banner, inter, rewarded
banner = simpleam.Banner(simpleam.TEST_BANNER_ID, "BOTTOM", "BANNER")
banner.load_ad()
inter = simpleam.Interstitial()
rewarded = simpleam.Rewarded()

def turn_banner():
	global banner
	banner.set_visibility(not banner.get_visibility())


def turn_interstitial():
	global inter
	inter.load_ad()
	while inter.is_loading():
		print('waiting for ad to load')
		# Absolutely not recommended to do like this. This is used ONLY for example showcase!
		pygame.time.delay(600)
	inter.show()

def turn_rewarded():
	global rewarded
	rewarded.load_ad()
	while rewarded.is_loading():
		print('waiting for ad to load')
		# Absolutely not recommended to do like this. This is used ONLY for example showcase! x2
		pygame.time.delay(600)
	rewarded.show()

ui = []
btn_surf = pygame.Surface((300, 140)).convert()
btn_surf.fill((40, 40, 40))
btn_surf2 = pygame.Surface.copy(btn_surf)
btn_surf2.fill((30, 30, 30))
ui.append(MenuButton(type="banner_btn", rect=pygame.Rect(0, 0, 300, 160), surfaces=[btn_surf, btn_surf2],
		 text=font.render("Turn on/off banner", 1, (255, 255, 255)), centered=(800, 720//2), task=turn_banner))
ui.append(MenuButton(type="inter_btn", rect=pygame.Rect(0, 0, 300, 160), surfaces=[btn_surf, btn_surf2],
		 text=font.render("Show interstitial", 1, (255, 255, 255)), centered=(480, 720//2), task=turn_interstitial))
ui.append(MenuButton(type="rewarded_btn", rect=pygame.Rect(0, 0, 300, 160), surfaces=[btn_surf, btn_surf2],
		 text=font.render("Show rewarded", 1, (255, 255, 255)), centered=(1280//2, 550), task=turn_rewarded))
while 1:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			raise SystemExit

	# logic
	m_pos = pygame.mouse.get_pos()
	m_btn = pygame.mouse.get_pressed()
	for ui_element in ui:
		ui_element.logic(mouse=m_pos, mouse_btn=m_btn)

	# redrawing the screen
	screen.fill((0, 0, 0))
	for ui_element in ui:
		ui_element.draw(screen)

	pygame.display.update()
	clock.tick(60)
