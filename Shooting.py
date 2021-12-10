import pygame
import random
import os
import math

H = 655
W = 1300
pygame.init()
GameWindow = pygame.display.set_mode((W, H))
pygame.display.set_caption("Shooting")
pygame.display.update()
Gun = pygame.image.load("Components\gun.png").convert_alpha()
gun = pygame.transform.rotozoom(Gun, 0, 0.6)
pygame.display.set_icon(gun)
bullet = pygame.transform.rotozoom(
pygame.image.load("Components\\bullet.png"), 0, 0.15)
white = (255, 255, 255)
red = (255, 0, 0)
black = (0, 0, 0)
c = (0, 255, 0)
d = (0, 0, 255)
e = (123, 3, 32)

pygame.mixer.music.load("Sounds\music.wav")
win = pygame.mixer.Sound("Sounds\win.wav")
lose = pygame.mixer.Sound("Sounds\lose.wav")
lost = pygame.mixer.Sound("Sounds\snake.wav")

bgimg = pygame.image.load("Components\gungame.jpg").convert_alpha()
bgimg = pygame.transform.scale(bgimg, (W, H)).convert_alpha()
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, int(H/10))


def text_screen(text, color, x, y):
    screen_text = font.render(text, True, color)
    GameWindow.blit(screen_text, [x, y])


def game():
    pygame.mixer.music.play(-1)
    gameexit = False
    gameover = False
    bx = 110
    sy = H/2
    by = sy
    ay = H/2
    vx = 50
    balls = 5
    avy = 5
    score = 0
    start = False
    ch1 = 1
    ch2 = 1
    ttt = 1
    while not gameexit:

        if(balls):
            if score == 50 and ch1:
                avy += 5
                ch1 = 0
            if score == 100 and ch2:
                avy += 10
                ch2 = 0
            for event in pygame.event.get():

                if (event.type == pygame.QUIT):
                    gameexit = True
                if (event.type == pygame.KEYDOWN):

                    if (event.key == pygame.K_SPACE):
                        start = True
                    if (event.key == pygame.K_w):
                        sy -= 30
                    if event.key == pygame.K_s:
                        sy += 30
                    if event.key == pygame.K_f:
                        avy += 5
                    if event.key == pygame.K_k:
                        avy -= 5

            keys = pygame.key.get_pressed()
            if(keys[pygame.K_DOWN]):
                sy += 10
            if(keys[pygame.K_UP]):
                sy -= 10
            if(bx == 110):
                by = sy
            ay = (ay+avy) % (H)
            if(start):
                bx += vx

            GameWindow.blit(bgimg, (0, 0))

            GameWindow.blit(gun, (-5, sy-15))

            GameWindow.blit(bullet, (bx+5, by-5))

            pygame.draw.rect(GameWindow, (255, 0, 0), [W-50, ay, 25, 50])
            pygame.draw.rect(GameWindow, (0, 0, 125), [W-50, ay, 10, 50])
            w = score
            if(bx >= int(W*99/100)) and (sy+10 >= ay and sy+10 <= ay+50):
                score += 10
                pygame.mixer.Sound.play(win)
            if(bx > W):
                bx = 110

                start = False
                if(w-score == 0):
                    balls -= 1
                    pygame.mixer.Sound.play(lose)
            text_screen("Score: " + str(score), red, 5, 5)
            text_screen("Life: " + str(balls), red, 300, 5)
        else:

            pygame.mixer.music.pause()
            GameWindow.blit(bgimg, (0, 0))
            if(ttt):
                pygame.mixer.Sound.play(lost)
                ttt = 0
            text_screen(f"SCORE = {score}", red, W/10, H/2)
            text_screen("Game Over! Press Enter To Continue",
                        red, W/40, H/2 + H/15)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameexit = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        welcome()
        pygame.display.update()
        clock.tick(30)
    pygame.quit()
    quit()


def welcome():
    gameexit = False

    while not gameexit:

        GameWindow.blit(bgimg, (0, 0))
        text_screen("Welcome to Shooting", black, W/3, H/2)
        text_screen("Press Space Bar To Play", black, W/3, H/2 + H/15)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameexit = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:

                    game()
        pygame.display.update()
        clock.tick(60)


welcome()
