import pygame
from Controller import *
class MainMenu:
    def __init__(self):
        pygame.init()
        # Window display
        self.x_cam = 0
        self.y_cam = 0
        self.move_cam = 0
        self.main_menu_window = pygame.display.set_mode((800,600))
        # Boss Icons
        self.knife_boss_icon = pygame.image.load("Menu//Knife_Boss_Icon.png")
        self.menu_background = pygame.image.load("Menu//Background.png")
        self.running = False
        self.running_start = False
        self.start_dare = pygame.mixer.Sound("Menu//Start_Dare.wav")
        self.music = pygame.mixer.Sound("Menu//Main_Menu_Song.wav")

    def run(self):
        self.running_start = True
        pygame.display.set_caption("Sick Up")
        i = 0
        self.music.play(loops=-1)
        self.music.set_volume(0.1)
        while self.running_start:

            i -= 1
            rel_x = i % 800
            self.main_menu_window.blit(self.menu_background, (rel_x - 800, 0))
            if rel_x < 800:
                self.main_menu_window.blit(self.menu_background, (rel_x, 0))
            for event in pygame.event.get():
                ControllerMain.basic_keys(self, event)
                pressed = pygame.mouse.get_pressed()
                mouse_pos_x = pygame.mouse.get_pos()[0]
                mouse_pos_y = pygame.mouse.get_pos()[1]
            self.click(mouse_pos_x, mouse_pos_y, pressed)
            self.run_text(mouse_pos_x, mouse_pos_y)
            pygame.display.flip()

    def run_text(self, mouse_pos_x, mouse_pos_y):
        ControllerMain.text(self, "Stick Up", 180, (10,100), (255,255,255), self.main_menu_window)
        if mouse_pos_x > 25 and mouse_pos_y > 450 and mouse_pos_x < 225 and mouse_pos_y < 525:
            ControllerMain.text(self, "Start", 60, (40,450), (0,255,255), self.main_menu_window)
        else:
            ControllerMain.text(self, "Start", 60, (40,450), (255,255,255), self.main_menu_window)
        if mouse_pos_x > 250 and mouse_pos_y > 450 and mouse_pos_x < 530 and mouse_pos_y < 525:
            ControllerMain.text(self, "Settings", 60, (265,450), (0,255,255), self.main_menu_window)
        else:
            ControllerMain.text(self, "Settings", 60, (265,450), (255,255,255), self.main_menu_window)
        if mouse_pos_x > 575 and mouse_pos_y > 450 and mouse_pos_x < 710 and mouse_pos_y < 525:
            ControllerMain.text(self, "Quit", 60, (590,450), (0,255,255), self.main_menu_window)
        else:
            ControllerMain.text(self, "Quit", 60, (590,450), (255,255,255), self.main_menu_window)

    def click(self, mouse_pos_x, mouse_pos_y, pressed):
        if pressed[0] == 1 and mouse_pos_x > 25 and mouse_pos_y > 450 and mouse_pos_x < 225 and mouse_pos_y < 525:
            ControllerMain.scene = 1




    def run_scene2(self):
        self.running = True
        pygame.display.set_caption("Choose a boss")
        while self.running:
            for event in pygame.event.get():
                ControllerMain.basic_keys(self, event)
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_w:
                        self.move_cam = 1
                    if event.key == pygame.K_s:
                        self.move_cam = 2
                    if event.key == pygame.K_d:
                        self.move_cam = 3
                    if event.key == pygame.K_a:
                        self.move_cam = 4
                    if event.key == pygame.K_UP:
                        self.move_cam = 1
                    if event.key == pygame.K_DOWN:
                        self.move_cam = 2
                    if event.key == pygame.K_RIGHT:
                        self.move_cam = 3
                    if event.key == pygame.K_LEFT:
                        self.move_cam = 4
            if self.move_cam == 1:
                self.y_cam -= 5
            if self.move_cam == 2:
                self.y_cam += 5
            if self.move_cam == 3:
                self.x_cam += 5
            if self.move_cam == 4:
                self.x_cam -= 5
        self.main_menu_window.blit(self.knife_boss_icon, (0 - self.x_cam,0 - self.y_cam))
        pygame.display.flip()
