import pygame

pygame.init()
pygame.mixer.music.load("exercicios/ex021.mp3")
pygame.mixer.music.play()
input("Tocando música... Pressione Enter para parar.")
pygame.mixer.music.stop()
