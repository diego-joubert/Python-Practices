import pygame
import sys

# Inicializar Pygame
pygame.init()

# Configuraciones de la ventana
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Juego de Mundo Abierto en 2D")

# Colores
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Cargar mapa (puedes reemplazarlo con tu propio mapa)
map_width, map_height = 2000, 2000
map_image = pygame.Surface((map_width, map_height))  # Mapa grande
map_image.fill(GREEN) 

# Clase del jugador
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill(BLUE)  # Color del jugador
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH // 2, HEIGHT // 2)
        self.speed = 5

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed
        if keys[pygame.K_UP]:
            self.rect.y -= self.speed
        if keys[pygame.K_DOWN]:
            self.rect.y += self.speed

# Crear el jugador
player = Player()
all_sprites = pygame.sprite.Group()
all_sprites.add(player)

# Bucle principal del juego
clock = pygame.time.Clock()
camera_x, camera_y = 0, 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Actualizar el jugador
    all_sprites.update()

    # Mover la cámara según la posición del jugador
    camera_x = player.rect.centerx - WIDTH // 2
    camera_y = player.rect.centery - HEIGHT // 2

    # Limitar la cámara a los bordes del mapa
    camera_x = max(0, min(camera_x, map_width - WIDTH))
    camera_y = max(0, min(camera_y, map_height - HEIGHT))

    # Dibujar todo
    screen.fill(WHITE)  # Limpiar la pantalla con blanco
    screen.blit(map_image, (-camera_x, -camera_y))  # Dibujar el mapa desplazado por la cámara
    all_sprites.draw(screen)  # Dibujar al jugador

    # Actualizar la pantalla
    pygame.display.flip()
    clock.tick(60)  # Limitar a 60 FPS