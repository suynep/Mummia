import pygame

pygame.init()
pygame.display.init()
BASE_W, BASE_H = (800, 900)
SCREEN=pygame.display.set_mode((BASE_W, BASE_H), pygame.RESIZABLE)
COLORS={
    "ui_bg": pygame.Color(36, 36, 36),
    "ui_fg": pygame.Color(99, 99, 99),
    "text": pygame.Color(255, 255, 255)
}
pygame.display.set_caption("Mummia - An Image Viewer")