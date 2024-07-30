import numpy as np
from scipy.integrate import solve_ivp
import pygame
import os
import matplotlib.pyplot as plt

os. chdir("D:\GitHubRepos\Double Pendulum\Double_Pendulum_Inter")


pygame.init()
screen = pygame.display.set_mode((1500, 720))
clock = pygame.time.Clock()
running = True

center = pygame.Vector2(screen.get_width() / 2, 0)
coor = (center[0], center[1]+100)
coor2 = (center[0],center[1]+200)

l = 

def deriv(t,funcin):
    theta1, omega1, theta2, omega2 = funcin
    delta_theta = funcin(1) - funcin(3)
    denom = 2.0 - np.cos(delta_theta)**2

    dtheta1 = funcin(2)
    domega1 = (-9.81 * (2.0 * np.sin(funcin(1)) - np.sin(funcin(3)) * np.cos(delta_theta)) - np.sin(delta_theta) * (funcin(4)**2 + 2.0 * funcin(2)**2 * np.cos(delta_theta))) / (l * denom)
    dtheta2 = funcin(4)
    domega2 = (2.0 * np.sin(delta_theta) * (funcin(2)**2 * np.cos(delta_theta) + 9.81 * np.cos(funcin(1))) - 2.0 * 9.81 * np.sin(funcin(3))) / (l * denom)
    return [dtheta1,domega1,dtheta2,domega2]

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
