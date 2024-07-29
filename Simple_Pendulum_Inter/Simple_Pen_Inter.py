import numpy as np
from scipy.integrate import solve_ivp
import pygame
import os
import matplotlib.pyplot as plt

os. chdir("D:\GitHubRepos\Double Pendulum\Simple_Pendulum_Inter")

pygame.init()
screen = pygame.display.set_mode((1500, 720))
clock = pygame.time.Clock()
running = True

center = pygame.Vector2(screen.get_width() / 2,0)
coor = (center[0], center[1]+100)

l = 1
omega0 = 0

def deriv(t, y): 
    theta, omega = y
    dtheta_dt = omega
    domega_dt = -9.81/ l * np.sin(theta)
    return [dtheta_dt, domega_dt]

def motion(theta_0, l, omega0):
    y0 = [float(theta_0), omega0]
    t_eval = np.linspace(0, 10, 250)
    t_span = (0,10)
    sol = solve_ivp(deriv, t_span, y0, t_eval=t_eval)
    x = (l*np.sin(sol.y[0])).tolist()
    y = (l*np.cos(sol.y[0])).tolist()
    return [x,y]

speed = 2
frame_count = 0
index = 0

while running:

    screen.fill("white")

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    mouse_state = pygame.mouse.get_pressed(num_buttons=3)
    
    if mouse_state[0] == True:
        coor = pygame.mouse.get_pos()

    l = np.sqrt((coor[0]/100-center[0]/100)**2 + (coor[1]/100-center[1]/100)**2)

    #if coor[0]<center[0]:
    theta_0 = np.arccos(coor[1]/(l*100))
    #else:
     #   theta_0 = -np.arccos(coor[1]/(l*100))
    pygame.draw.line(screen,"black",center,(coor[0],coor[1]))
    pygame.draw.circle(screen, "red", (coor[0],coor[1]), 24)
    

    if not mouse_state[0]:
        screen.fill("white")
        x = motion(theta_0, l, omega0)[0]
        y = motion(theta_0, l, omega0)[1]
        pygame.draw.line(screen,"black",center,(x[index]*100+center[0],y[index]*100+center[1]))
        pygame.draw.circle(screen, "red", (x[index]*100+center[0],y[index]*100+center[1]), 24)

        frame_count += 1
        if frame_count >= speed:
            frame_count = 0
            index += 1
            if index >= len(x):
                index = 0
        
       
    pygame.display.flip()
    clock.tick(60)  # limits FPS to 60
pygame.quit()
