import pygame
import os


os. chdir("D:\GitHubRepos\Double Pendulum")


pygame.init()
screen = pygame.display.set_mode((1500, 720))
clock = pygame.time.Clock()
running = True

center = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

coor = (center[0], center[1]+100)
coor2 = (center[0],center[1]+200)
while running:

    screen.fill("white")

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    mouse_state = pygame.mouse.get_pressed(num_buttons=3)
    
    if mouse_state[0] == True:
        coor = pygame.mouse.get_pos()

    if mouse_state[2] == True:
        coor2 = pygame.mouse.get_pos()

    pygame.draw.line(screen,"black",center,(coor[0],coor[1]))
    pygame.draw.circle(screen, "red", (coor[0],coor[1]), 24)
    pygame.draw.line(screen,"black",(coor[0],coor[1]),(coor2[0],coor2[1]))
    pygame.draw.circle(screen, "red", (coor2[0],coor2[1]), 24)

    pygame.display.flip()
    clock.tick(60)  # limits FPS to 60

pygame.quit()
