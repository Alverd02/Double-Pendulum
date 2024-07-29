from scipy.integrate import solve_ivp
import numpy as np
import matplotlib.pyplot as plt

# Parámetros del péndulo simple
l = 1.0
g = 9.81

# Ecuaciones diferenciales
def deriv(t, y):
    theta, omega = y
    dtheta_dt = omega
    domega_dt = -g / l * np.sin(theta)
    return [dtheta_dt, domega_dt]

# Condiciones iniciales
theta0 = np.pi / 2
omega0 = 0
y0 = [theta0, omega0]
# Intervalo de tiempo
t_span = (0, 10)
t_eval = np.linspace(0, 10, 250)  # 250 puntos de tiempo para evaluación

# Resolver la ecuación diferencial
sol = solve_ivp(deriv, t_span, y0, t_eval=t_eval)

print(y0,sol.y)
x = (l*np.sin(sol.y[0])).tolist()
y = (-l*np.cos(sol.y[0])).tolist()
# Graficar el resultado
plt.plot(x,y)
plt.xlabel('Tiempo (s)')
plt.ylabel('Ángulo (rad)')
plt.title('Movimiento del Péndulo Simple')
plt.grid(True)
plt.show()
