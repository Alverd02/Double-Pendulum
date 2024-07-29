import pygame
import os

os. chdir("D:\GitHubRepos\Double Pendulum\Simple_Pendulum")

pygame.init()
screen = pygame.display.set_mode((1500, 720))
clock = pygame.time.Clock()
running = True

center = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)


index = 0
dt = (20/800)*1000
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    x = []
    y = []
    with open("simple_data.dat") as dat:
        for line in dat:
            positions = line.split()
            x.append(float(positions[0]))
            y.append(float(positions[1]))  

    screen.fill("white")
    pygame.draw.line(screen,"black",center,(x[index]*100+center[0],-y[index]*100+center[1]))
    pygame.draw.circle(screen, "red", (x[index]*100+center[0],-y[index]*100+center[1]), 24)
    pygame.display.flip()

    if index < len(x)-1:
        index = index + 1
        pygame.time.delay(int(dt))
    else:
        index = 0

    clock.tick(60)  # limits FPS to 60

pygame.quit()


