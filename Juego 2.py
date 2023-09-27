import pygame
import random
import sys

# Inicializar Pygame
pygame.init()

# Configuración de la pantalla
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Esquiva los Objetos")

# Colores
white = (255, 255, 255)
blue = (0, 0, 255)

# Nave espacial
spaceship = pygame.image.load("spaceship.png")
spaceship = pygame.transform.scale(spaceship, (50, 50))
spaceship_x = screen_width // 2 - 25
spaceship_y = screen_height - 70
spaceship_speed = 2

# Obstáculos
obstacles = []
obstacle_speed = 1
obstacle_spawn_rate = 60  # Cada cuántos frames se crea un obstáculo
obstacle_timer = 0

# Puntuación
score = 0

# Fuente de texto
font = pygame.font.Font(None, 36)

# Bucle principal del juego
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Capturar las teclas presionadas
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        spaceship_x -= spaceship_speed
    if keys[pygame.K_RIGHT]:
        spaceship_x += spaceship_speed

    # Limitar la posición de la nave espacial a la pantalla
    spaceship_x = max(0, min(screen_width - 50, spaceship_x))

    # Generar obstáculos
    obstacle_timer += 1
    if obstacle_timer >= obstacle_spawn_rate:
        obstacle_x = random.randint(0, screen_width - 50)
        obstacle_y = -50
        obstacles.append([obstacle_x, obstacle_y])
        obstacle_timer = 0

    # Mover y eliminar obstáculos
    for obstacle in obstacles:
        obstacle[1] += obstacle_speed
        if obstacle[1] > screen_height:
            obstacles.remove(obstacle)

    # Colisiones con obstáculos
    for obstacle in obstacles:
        if (
            spaceship_x < obstacle[0] + 50
            and spaceship_x + 50 > obstacle[0]
            and spaceship_y < obstacle[1] + 50
            and spaceship_y + 50 > obstacle[1]
        ):
            running = False

    # Eliminar obstáculos que han salido de la pantalla
    obstacles = [obstacle for obstacle in obstacles if obstacle[1] < screen_height]

    # Puntuación
    score += 1

    # Llenar la pantalla con color blanco
    screen.fill(white)

    # Dibujar la nave espacial
    screen.blit(spaceship, (spaceship_x, spaceship_y))

    # Dibujar los obstáculos
    for obstacle in obstacles:
        pygame.draw.rect(screen, blue, (obstacle[0], obstacle[1], 50, 50))

    # Mostrar la puntuación en la pantalla
    score_text = font.render(f"Puntuación: {score}", True, blue)
    screen.blit(score_text, (10, 10))

    # Actualizar la pantalla
    pygame.display.update()

# Juego terminado
pygame.quit()
sys.exit()