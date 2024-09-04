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
new_center = (center[0], center[1]+100)

l1 = 1
l2 = 1

coor1 = (center[0], center[1]+l1*100)
coor2 = (center[0],center[1]+l2*200)


omega0 = 0
theta_01 = 0
theta_02 = 0
dt = (10/625)*1000


def deriv(t,funcin):
    theta1, omega1, theta2, omega2 = funcin

    delta_theta = theta1 - theta2
    denom1 = (2 - np.cos(2 * delta_theta))
    denom2 = (l2 / l1) * denom1
    
    dtheta1 = omega1
    dtheta2 = omega2
    
    domega1 = (-9.81 * (2 * np.sin(theta1) + np.sin(theta1 - 2 * theta2)) - 2 * np.sin(delta_theta) * (omega2**2 * l2 + omega1**2 * l1 * np.cos(delta_theta))) / (l1 * denom1)
    domega2 = (2 * np.sin(delta_theta) * (omega1**2 * l1 * np.cos(delta_theta) + 9.81 * np.cos(theta1) + omega2**2 * l2 * np.cos(delta_theta))) / (l2 * denom2)

    return [dtheta1,domega1,dtheta2,domega2]

def motion(theta_01,theta_02, l1, l2, omega0):
    y0 = [float(theta_01), omega0,float(theta_02), omega0]
    t_eval = np.linspace(0, 10,625)
    t_span = (0,10)
    sol = solve_ivp(deriv, t_span, y0, t_eval=t_eval)
    x1 = (l1*np.sin(sol.y[0])).tolist()
    y1 = (l1*np.cos(sol.y[0])).tolist()
    x2 = (l2*np.sin(sol.y[2])).tolist()
    y2 = (l2*np.cos(sol.y[2])).tolist()
    return [x1,y1,x2,y2]

x1 = motion(theta_01,theta_02, l1, l2, omega0)[0]
y1 = motion(theta_01,theta_02, l1, l2, omega0)[1]
x2 = motion(theta_01,theta_02, l1, l2, omega0)[2]
y2 = motion(theta_01,theta_02, l1, l2, omega0)[3]
index = 0

old_x1 = x1[index]
old_y1 = y1[index]

while running:

    screen.fill("white")

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    mouse_state = pygame.mouse.get_pressed(num_buttons=3)
    
    if mouse_state[0] == True:
        coor1 = pygame.mouse.get_pos()
        coor2 = (coor1[0],coor1[1] + l2*100)
        index = 0
        l1 = np.sqrt((coor1[0]/100-center[0]/100)**2 + (coor1[1]/100-center[1]/100)**2)
        if coor1[0]<center[0]:
            theta_01 = -np.arccos(coor1[1]/(l1*100))
        else:
            theta_01 = np.arccos(coor1[1]/(l1*100))
        x1 = motion(theta_01,theta_02, l1, l2, omega0)[0]
        y1 = motion(theta_01,theta_02, l1, l2, omega0)[1]
        x2 = motion(theta_01,theta_02, l1, l2, omega0)[2]
        y2 = motion(theta_01,theta_02, l1, l2, omega0)[3]

    if mouse_state[2] == True:
        coor2 = pygame.mouse.get_pos()
        coor1 = new_center
        index = 0
        l2 = np.sqrt((coor2[0]/100-new_center[0]/100)**2 + (coor2[1]/100-new_center[1]/100)**2)
        if coor2[0]<new_center[0]:
            theta_02 = -np.arccos((coor2[1]-coor1[1])/(l2*100))
        else:
            theta_02 = np.arccos((coor2[1]-coor1[1])/(l2*100))
        x1 = motion(theta_01,theta_02, l1, l2, omega0)[0]
        y1 = motion(theta_01,theta_02, l1, l2, omega0)[1]
        x2 = motion(theta_01,theta_02, l1, l2, omega0)[2]
        y2 = motion(theta_01,theta_02, l1, l2, omega0)[3]

    pygame.draw.line(screen,"black",center,(coor1[0],coor1[1]))
    pygame.draw.circle(screen, "red", (coor1[0],coor1[1]), 24)
    pygame.draw.line(screen,"black",(coor1[0],coor1[1]),(coor2[0],coor2[1]))
    pygame.draw.circle(screen, "red", (coor2[0],coor2[1]), 24)
    if mouse_state[2] == True:
        coor2 = pygame.mouse.get_pos()

    if not mouse_state[0]:
        old_x1 = x1[index]
        old_y1 = y1[index]
        theta_01 = theta_01
        screen.fill("white")
        new_center = (x1[index]*100+center[0],y1[index]*100+center[1])
        pygame.draw.line(screen,"black",center,(x1[index]*100+center[0],y1[index]*100+center[1]))
        pygame.draw.circle(screen, "red", (x1[index]*100+center[0],y1[index]*100+center[1]), 24)
        pygame.draw.line(screen,"black",(x1[index]*100+center[0],y1[index]*100+center[1]),(x2[index]*100+new_center[0],y2[index]*100+new_center[1]))
        pygame.draw.circle(screen, "red", (x2[index]*100+new_center[0],y2[index]*100+new_center[1]), 24)

    font = pygame.font.Font(None, 36)
    time = "Time = "
    time_num = 0 + index*dt/1000
    text_surface1 = font.render(str(time), True, (0, 0, 0))
    text_rect1 = text_surface1.get_rect(center=(320, 240))
    text_surface2 = font.render(str(time_num), True, (0, 0, 0))
    text_rect2 = text_surface2.get_rect(center=(410, 240))
    screen.blit(text_surface1, text_rect1) 
    screen.blit(text_surface2, text_rect2) 

    if index < len(x1)-1:
        index = index + 1
        pygame.time.delay(int(dt))
    else:
        index = 0
    pygame.display.flip()
    clock.tick(60)  # limits FPS to 60

pygame.quit()
