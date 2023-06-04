import pygame
import simpleam
pygame.init()

screen = pygame.display.set_mode((1280, 720), pygame.SCALED | pygame.FULLSCREEN)
clock = pygame.time.Clock()
from ui import MenuButton
font = pygame.font.SysFont("Bold", 80)
simpleam.simpleam_init()
global banner, inter, rewarded, inter_asked, rewarded_asked
banner = simpleam.Banner(simpleam.TEST_BANNER_ID, "BOTTOM", "BANNER")
banner.load_ad()
inter = simpleam.Interstitial()
rewarded = simpleam.Rewarded()
inter_asked = False
rewarded_asked = False


def turn_banner():
    global banner
    print('toggling banner')
    banner.set_visibility(not banner.get_visibility())


def turn_interstitial():
    global inter, inter_asked, rewarded_asked
    if inter_asked or rewarded_asked:
        print('not that fast !')
        return
    print('loading interstitial')
    inter.load_ad()
    inter_asked = True

def turn_rewarded():
    global rewarded, inter_asked, rewarded_asked
    if inter_asked or rewarded_asked:
        print('not that fast !')
        return
    print('loading rewarded')
    rewarded.load_ad()
    rewarded_asked = True

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
         
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            raise SystemExit

    # logic
    m_pos = pygame.mouse.get_pos()
    m_btn = pygame.mouse.get_pressed()
    for ui_element in ui:
        ui_element.logic(mouse=m_pos, mouse_btn=m_btn)

    if inter_asked and inter.is_loaded():
        print('showing interstitial')
        inter.show()
        inter_asked= False
    elif rewarded_asked and rewarded.is_loaded():
        print('showing rewarded')
        rewarded.show()
        rewarded_asked= False
        
    # redrawing the screen
    screen.fill((0, 0, 0))
    for ui_element in ui:
        ui_element.draw(screen)
    pygame.display.update()
    clock.tick(60)
