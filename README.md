# Pendulums

I will assume that you already have python, fortran and gnuplot(optional) properly installed.

## -Physics behind the program

The system(s) consist of a pendulum(s) with mass $m$ with length $l=1.5(1)m$ using $g=9.81\frac{m}{s^2}$.
The equations used were obtained using lagrangian mechanics taking into account the information above.  
In the simple pendulum case, I use:

$$\ddot{\theta} = \frac{-g}{l}sin(\theta)$$

The double pendulum case:

$$2\ddot{\theta}_1 + \sin{(\theta_1-\theta_2)}\dot{\theta}_2 + \cos{(\theta_1-\theta_2)}\ddot{\theta}_2 + \frac{2g}{l}\sin{\theta_1} = 0$$

$$ \ddot{\theta}_2 - \sin{(\theta_1-\theta_2)}\dot{\theta}_1 + \cos{(\theta_1-\theta_2)\ddot{\theta}_1} + \frac{g}{l}\sin{\theta_2} = 0 $$  

In order to solve this problem I used the Runge-Kutta4 method, with the functions given solving the equation system above:  

$$ \ddot{\theta}_1 = \ddot{\theta}_1(\theta_1,\theta_2,\dot{\theta}_1,\dot{\theta}_2) $$  

$$ \ddot{\theta}_2 = \ddot{\theta}_2(\theta_1,\theta_2,\dot{\theta}_1,\dot{\theta}_2) $$  

In both systems when we obtain the solution of the differential equation we just need to change the variables to $x$ and $y$ and get the coordinates.

## -How this programs work

I use fortran to compute the numerical solutions for each system and then using python(pygame) I make the simulation.

![python_2P9mdJ7yYm](https://github.com/user-attachments/assets/4bc179a5-cab7-47a7-8f1a-660494fce2aa)

![python_Mqj3ajrU87](https://github.com/user-attachments/assets/5ec89c34-38d1-4ec1-9ceb-378ef6cbd26e)


## -How to use it

In each fortran file you can change the initial conditions to make your own numerical solutions, nothing more has to be changed, then run the python code and magic will be done :)  
Note that the only parameter that can change the system is the length $l$, initial angle or angles and angular velocity, the equations used are the ones deriven from equal masses and equal length so you can't simulate pendulums of differents masses and differents lengths.
## -More

There is a little gnuplot script to see the x,y graph. You can also change it to make your own plots or just run it.

  ![Simple Graphic](https://github.com/Alverd02/Double-Pendulum/assets/118913394/8049efec-9812-48c4-9789-3fd072a21d1b)

  ![Screenshot 2024-07-30 001747](https://github.com/user-attachments/assets/efa5ed16-bc4c-423e-8d37-4b812b266115)

Also, I did a script wit the angles and its velocity with time


![Simple Graphic Time](https://github.com/Alverd02/Double-Pendulum/assets/118913394/6896d05d-50d5-4308-9812-3159f7c4ac84)

![Screenshot 2024-07-30 001852](https://github.com/user-attachments/assets/3bedcf87-7831-4bf1-a4fb-b38d86202f76)

## Update

I wanted to do something to make the initial condition changing easier. I made an interactive app in which you can change the angle with the mouse cursor in both systems. The double pendulum has some errors and it's not quite what I wanted but it works somehow.

