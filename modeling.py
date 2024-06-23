import pygame

pygame.init()
screen = pygame.display.set_mode((1500, 720))
clock = pygame.time.Clock()
running = True
center = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
print(type(center[0]))
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    
    with open("data.dat") as dat:
        for line in dat:
            positions = line.split()
            screen.fill("white")
            pygame.draw.circle(screen, "red", (float(positions[0])*100+center[0],float(positions[1])*100+center[1]), 40)
            pygame.draw.circle(screen, "red", (float(positions[2])*100+center[0],float(positions[3])*100+center[1]), 40)
            pygame.display.update()
    pygame.display.flip()
    clock.tick(60)  # limits FPS to 60

pygame.quit()


