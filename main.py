import pygame
import os
import sys
from pprint import pprint
from base import BASE_H, BASE_W, SCREEN, COLORS


class Button:
    def __init__(self, position, label):
        self.position = position
        self.color = COLORS["ui_fg"]
        self.label = label
        self.font = pygame.font.SysFont("Hack", 15)
        self.size = (len(self.label) * 10, 30)

    def draw(self):
        pygame.draw.rect(SCREEN, self.color, (*self.position, *self.size))
        text = self.font.render(self.label, True, COLORS["text"])
        SCREEN.blit(text, self.position) # --> adjust the position later on to center the text in the rectangle

class Image:
    def __init__(self, path, canvas): # --> canvas is a RectVal
        self.path = path
        self.img_surf = None
        try:
            self.img_surf = pygame.image.load(self.path)

        except:
            print("Error: Couldn't find/open the given file")

        self.display_img_surf = None
        self.canvas = canvas
        self.chop_coords = [0, 0]
    
    def draw_chopped(self):
        self.display_img_surf = pygame.transform.chop(self.img_surf, (*self.chop_coords, *self.canvas[2:]))
        SCREEN.blit(self.display_img_surf, self.canvas)

    def draw_scaled(self):
        self.display_img_surf = pygame.transform.scale(self.img_surf, self.canvas[2:])
        SCREEN.blit(self.display_img_surf, self.canvas)



class MainApplication:
    def __init__(self):
        self.running = True
        self.menu_buttons = {
            "open_img": Button((BASE_W / 5, 10),  "Open Img"), 
            "open_folder": Button((2 * BASE_W / 5, 10),  "Open Folder"), 
            "help": Button((3 * BASE_W / 5, 10),  "Help"), 
            "about": Button((4 * BASE_W / 5, 10),  "About")
            }
        self.display_canvas = (40, 40, BASE_W - 40 * 2, BASE_H - 40 * 2)
        self.display_img = None


    def run(self):
        while self.running:

            # Check if the user wants to QUIT :( and other events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    print("Thank you for using Mummia! Please leave any feedback you may have at \n\tsuy.nepal@gmail.com")
                    pygame.quit()
                    sys.exit(0)

                if event.type == pygame.MOUSEBUTTONDOWN:
                    click_pos = event.pos
                    for btn in self.menu_buttons.keys():
                        ref_btn = self.menu_buttons[btn]
                        if click_pos[0] > ref_btn.position[0] and click_pos[0] < ref_btn.position[0] + ref_btn.size[0] and click_pos[1] > ref_btn.position[1] and click_pos[1] < ref_btn.position[1] + ref_btn.size[1]:
                            if btn == "open_img":
                                self.display_img = Image(self.open_file_prompt(), self.display_canvas)
                
                if event.type == pygame.MOUSEWHEEL:
                    if self.display_img != None:
                        if self.display_img.chop_coords[0] >= 0:
                            self.display_img.chop_coords[0] -= event.x * 10
                        else:
                            self.display_img.chop_coords[0] = 0

                        if self.display_img.chop_coords[1] >= 0:
                            self.display_img.chop_coords[1] -= event.x * 10
                        else:
                            self.display_img.chop_coords[1] = 0
            

            SCREEN.fill(COLORS["ui_bg"])

            for btn in self.menu_buttons.keys():
                self.menu_buttons[btn].draw()
            
            if self.display_img != None:
                self.display_img.draw_chopped()

            pygame.display.flip()

    def open_file_prompt(self):
        file_path = input("enter the file path: ")
        sys.stdout.flush()
        return file_path

if __name__ == "__main__":
    MainApplication().run()