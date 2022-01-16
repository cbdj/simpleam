import pygame
pygame.init()

screen = pygame.display.set_mode((1280, 720), pygame.SCALED | pygame.FULLSCREEN)
clock = pygame.time.Clock()
from ui import MenuButton # Ignore this file. It's for simplicity, and it has nothing to do with simpleam module
font = pygame.font.SysFont("Bold", 80)

ANDROID = True
try: 
	import simpleam
except: 
	ANDROID = False

class Callbacks(simpleam.RewardedCallbacks):
	def __init__(self):
		pass

	def on_rewarded_loaded(self):
		print("SIMPLEAM: Ad is loaded!")

	def on_rewarded_opened(self):
		print("SIMPLEAM: Ad is opened!")

	def on_rewarded_started(self):
		print("SIMPLEAM: Ad is started!")

	def on_rewarded_closed(self):
		print("SIMPLEAM: Ad closed!")

	def on_rewarded_success(self, reward):
		print(f"SIMPLEAM: Ad succesfully ended!")

	def on_rewarded_left(self):
		print("SIMPLEAM: Ad left application!")

	def on_rewarded_load_fail(self, num):
		print(f"SIMPLEAM: Ad failed to load: {num}")
	
if ANDROID:
	simpleam.simpleam_init(None)
	global banner, inter, rewarded
	banner = simpleam.Banner(position="BOTTOM", size="SMART_BANNER")
	inter = simpleam.Interstitial("ca-app-pub-3940256099942544/8691691433")
	rewarded = simpleam.Rewarded()
	rewarded.set_listener(Callbacks())

def turn_banner():
	global banner
	if not banner.visible:
		print("Turning on banner")
		banner.load_ad()
		banner.set_visibility(True)
	else:
		print("Turning off banner")
		banner.set_visibility(False)


def turn_interstitial():
	global inter, banner
	if inter:
		inter.load_ad()
		while not inter.is_loaded():
			# Absolutely not recommended to do like this. This is used ONLY for example showcase!
			pygame.time.delay(600)
		inter.show()

def turn_rewarded():
	global rewarded
	if rewarded:
		rewarded.load_ad()
		while not rewarded.is_loaded():
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