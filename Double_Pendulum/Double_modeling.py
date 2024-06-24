import pygame
import os

os. chdir("D:\GitHubRepos\Double Pendulum\Double_Pendulum")

pygame.init()
screen = pygame.display.set_mode((1500, 720))
clock = pygame.time.Clock()
running = True

center = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

speed = 2
frame_count = 0
index = 0

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    x = []
    y = []
    with open("double_data.dat") as dat:
        for line in dat:
            positions = line.split()
            x.append(float(positions[0]))
            y.append(float(positions[1]))  

    screen.fill("white")
    pygame.draw.line(screen,"black",center,(x[index]*100+center[0],-y[index]*100+center[1]))
    pygame.draw.circle(screen, "red", (x[index]*100+center[0],-y[index]*100+center[1]), 24)
    pygame.display.flip()

    frame_count += 1
    if frame_count >= speed:
        frame_count = 0
        index += 1
        if index >= len(x):
            pos_index = 0

    clock.tick(60)  # limits FPS to 60

pygame.quit()