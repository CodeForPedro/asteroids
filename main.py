import pygame
from constants import SCREEN_WIDTH
from constants import SCREEN_HEIGHT
from logger import log_state
from player import Player


def main():
    print(f"Starting Asteroids with pygame version: {pygame.version.ver} \nScreen width: 1280 \nScreen height: 720")

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    clock = pygame.time.Clock()
    dt = 0 
    
    Player.containers = (updatable, drawable)
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)

    # Game Loop
    while True:
        log_state() # This just lets just logs the state of the game
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        updatable.update(dt)
        for obj in drawable:
            obj.draw(screen)
        pygame.display.flip() # This is what updates the display
        # Below method pauses the game loop until 1/60th of a second has passed, limiting to 60fps.
        dt = clock.tick(60)/1000


if __name__ == "__main__":
    main()