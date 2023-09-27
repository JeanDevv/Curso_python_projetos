import pygame
pygame.mixer.init()
pygame.init()
pygame.mixer.music.load('mine.mp3')
pygame.mixer.music.play()
pygame.event.wait()