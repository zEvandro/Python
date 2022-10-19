# Desafio 021

"""
faça um programa em Python que abra e reproduza um arquivo MP3
"""

# CODIGO:

import pygame
pygame.init()
pygame.mixer.music.load('ex022.mp3')
pygame.mixer.music.play()
pygame.event.wait()
