import pygame
import sys

# Inicialización de Pygame
pygame.init()

# Configuración de la ventana
WINDOW_WIDTH = 800  # Ancho de la ventana en píxeles
WINDOW_HEIGHT = 600  # Alto de la ventana en píxeles
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Movimiento Preciso en Pygame")

# Colores
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Escalado de los ejes
PIXELS_PER_MM = 10  # Número de píxeles por milímetro

# Posición inicial del objeto (en milímetros)
x_mm = 50
y_mm = 50

# Velocidad del objeto (en milímetros por actualización)
speed_x_mm = 1  # Velocidad en el eje x
speed_y_mm = 1  # Velocidad en el eje y

# Reloj para controlar la tasa de fotogramas
clock = pygame.time.Clock()

# Bucle principal
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Actualizar la posición del objeto
    x_mm += speed_x_mm
    y_mm += speed_y_mm

    # Convertir la posición a píxeles
    x_px = int(x_mm * PIXELS_PER_MM)
    y_px = int(y_mm * PIXELS_PER_MM)

    # Limpiar la pantalla
    screen.fill(WHITE)

    # Dibujar el objeto (un círculo en este caso)
    pygame.draw.circle(screen, RED, (x_px, y_px), 5)

    # Actualizar la pantalla
    pygame.display.flip()

    # Controlar la tasa de fotogramas
    clock.tick(60)

pygame.quit()
sys.exit()