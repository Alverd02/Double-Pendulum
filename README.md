# Pendulums

I will assume that you already have python, fortran and gnuplot(optional) properly installed.

## -Physic behind the program

The system(s) consist of a pendulum(s) with mass $m$ with length $l$ using $g=9.81$.
The equations used were obtained using lagrangian mechanics taking into account the information above.
In the simple pendulum case, I use:

$$\ddot{\theta} = \frac{-g}{l}sin(\theta)$$

The double pendulum case:

$$2\ddot{\theta}_1 + \sin{(\theta_1-\theta_2)}\dot{\theta}_2 + \cos{(\theta_1-\theta_2)}\ddot{\theta}_2 + \frac{2g}{l}\sin{\theta_1} = 0$$

$$ \ddot{\theta}_2 - \sin{(\theta_1-\theta_2)}\dot{\theta}_1 + \cos{(\theta_1-\theta_2)\ddot{\theta}_1} + \frac{g}{l}\sin{\theta_2} = 0 $$

## -How this programs work

I use fortran to compute the numerical solutions for each system and then using python(pygame) I make the simulation.

![python_na2kb2hl0Q](https://github.com/Alverd02/Double-Pendulum/assets/118913394/efeb7794-48db-49f6-8e36-1883fd7cfbbe)


![python_mdV9DQJ4na](https://github.com/Alverd02/Double-Pendulum/assets/118913394/4f530ea3-6d42-47b2-a34a-4b18fd6116f5)


## -How to use it

In each fortran file you can change the initial conditions to make your own numerical solutions, nothing more has to be changed, then run the python code and magic will be done :).
Note that the only parameter that can change the system is the length $l$, the equations used are the ones deriven from equal masses so you can't simulate pendulums of differents masses.
## -More

There is a little gnuplot script to see the x,y graph. You can also change it to make your own plots or just run it.



  ![Simple Graphic](https://github.com/Alverd02/Double-Pendulum/assets/118913394/8049efec-9812-48c4-9789-3fd072a21d1b)


  ![Double Graphic](https://github.com/Alverd02/Double-Pendulum/assets/118913394/31ef7529-7e89-45e4-a6e2-e9de889193b6)

Also, I did a script wit the angles and its velocity with time


![Simple Graphic Time](https://github.com/Alverd02/Double-Pendulum/assets/118913394/6896d05d-50d5-4308-9812-3159f7c4ac84)

![Simple Graphic Time](https://github.com/Alverd02/Double-Pendulum/assets/118913394/3dff4b10-7a89-4359-86f2-547302dec596)

