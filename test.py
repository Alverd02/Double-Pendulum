import pygame
# Inicializar Pygame
pygame.init()

# Configuración de la ventana
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Animación de un círculo")

# Colores
black = (0, 0, 0)
white = (255, 255, 255)

# Lista de posiciones (puedes personalizar estas listas con tus valores)
positions_x = [100, 150, 200, 250, 300, 350, 400, 450, 500, 550, 600, 650, 700, 750, 800]
positions_y = [100, 120, 140, 160, 180, 200, 220, 240, 260, 280, 300, 320, 340, 360, 380]

# Índice de la posición actual
pos_index = 0

# Velocidad de la animación (cuántos cuadros esperar antes de cambiar de posición)
animation_speed = 10  # Ajusta este valor para cambiar la velocidad de la animación
frame_count = 0

# Reloj para controlar la tasa de cuadros por segundo (FPS)
clock = pygame.time.Clock()
fps = 60  # Tasa de cuadros por segundo

# Bucle principal del programa
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Limpiar la pantalla
    screen.fill(black)

    # Dibujar el círculo en la posición actual
    pygame.draw.circle(screen, white, (positions_x[pos_index], positions_y[pos_index]), 20)

    # Actualizar la pantalla
    pygame.display.flip()

    # Control de la velocidad de la animación
    frame_count += 1
    if frame_count >= animation_speed:
        frame_count = 0
        pos_index += 1
        if pos_index >= len(positions_x):
            pos_index = 0

    # Controlar la tasa de cuadros por segundo (FPS)
    clock.tick(fps)

# Salir de Pygame
pygame.quit()

