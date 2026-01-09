import pygame
import os

<<<<<<< Updated upstream
os. chdir("C:\GitHubRepos\Double-Pendulum\Double_Pendulum")
=======
>>>>>>> Stashed changes

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
    x1 = []
    y1 = []
    x2 = []
    y2 = []
    with open("double_data.dat") as dat:
        for line in dat:
            positions = line.split()
            x1.append(float(positions[0]))
            y1.append(float(positions[1]))
            x2.append(float(positions[2]))
            y2.append(float(positions[3]))   

    screen.fill("white")

    pygame.draw.line(screen,"black",center,(x1[index]*100+center[0],-y1[index]*100+center[1]))
    pygame.draw.line(screen,"black",(x1[index]*100+center[0],-y1[index]*100+center[1]),(x2[index]*100+center[0],-y2[index]*100+center[1]))
    pygame.draw.circle(screen, "red", (x1[index]*100+center[0],-y1[index]*100+center[1]), 24)
    pygame.draw.circle(screen, "red", (x2[index]*100+center[0],-y2[index]*100+center[1]), 24)

    pygame.display.flip()

    if index < len(x1)-1:
        index = index + 1
        pygame.time.delay(int(dt))
    else:
        index = 0
    clock.tick(60)  # limits FPS to 60

pygame.quit()