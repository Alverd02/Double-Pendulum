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
theta_0 = 0
dt = (10/625)*1000

def deriv(t, y): 
    theta, omega = y
    dtheta_dt = omega
    domega_dt = -9.81/ l * np.sin(theta)
    return [dtheta_dt, domega_dt]

def motion(theta_0, l, omega0):
    y0 = [float(theta_0), omega0]
    t_eval = np.linspace(0, 10,625)
    t_span = (0,10)
    sol = solve_ivp(deriv, t_span, y0, t_eval=t_eval)
    x = (l*np.sin(sol.y[0])).tolist()
    y = (l*np.cos(sol.y[0])).tolist()
    return [x,y]

x = motion(theta_0, l, omega0)[0]
y = motion(theta_0, l, omega0)[1]
index = 0

while running:

    screen.fill("white")

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    mouse_state = pygame.mouse.get_pressed(num_buttons=3)
    
    if mouse_state[0]:
        coor = pygame.mouse.get_pos()
        index  = 0
        l = np.sqrt((coor[0]/100-center[0]/100)**2 + (coor[1]/100-center[1]/100)**2)
        if coor[0]<center[0]:
            theta_0 = -np.arccos(coor[1]/(l*100))
        else:
            theta_0 = np.arccos(coor[1]/(l*100))
        x = motion(theta_0, l, omega0)[0]
        y = motion(theta_0, l, omega0)[1]
        
    pygame.draw.line(screen,"black",center,(coor[0],coor[1]))
    pygame.draw.circle(screen, "red", (coor[0],coor[1]), 24)
    

    if not mouse_state[0]:

        screen.fill("white")
        pygame.draw.line(screen,"black",center,(x[index]*100+center[0],y[index]*100+center[1]))
        pygame.draw.circle(screen, "red", (x[index]*100+center[0],y[index]*100+center[1]), 24)

    font = pygame.font.Font(None, 36)
    time = f"Time = {0 + index*dt/1000}"
    text_surface = font.render(str(time), True, (0, 0, 0))
    text_rect = text_surface.get_rect(center=(320, 240))
    screen.blit(text_surface, text_rect) 

    if index < len(x)-1:
        index = index + 1
        pygame.time.delay(int(dt))
    else:
        index = 0
    pygame.display.flip()
    clock.tick(60)  # limits FPS to 60
pygame.quit()