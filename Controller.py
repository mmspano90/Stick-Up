import pygame
class ControllerMain:
    scene = 0
    done = False
    def __init__(self):
        self.running = True
        self.main_menu = MainMenu()
    def run(self):
        while True:
            if ControllerMain.scene == 0:
                self.main_menu.run()
            elif ControllerMain.scene == 1:
                self.main_menu.run_scene2()
            elif ControllerMain.scene == 2:
                self.main_menu.shop()
            elif ControllerMain.scene == 3:
                self.main_menu.settings()
    def basic_keys(self, event):
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        # Keybinds
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                exit()
    def text(self, text, size, pos, color, window):
        myfont = pygame.font.Font("Menu//helsinki.ttf", size)
        textsurface = myfont.render(text, True, color)
        window.blit(textsurface, pos)
from Menu import *
