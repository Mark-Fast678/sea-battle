# Rules:
# 1. Player plays against computer, they do not see each other's battleships
# 2. Computer randomly generates 4 battleships: 1 - 4 pipes, 2 - 3 pipes, 3 - 2 pipes, 4 - 1 pipes
# 3. Battleships are not visible until they are hit, then they become visible
import pygame
import sys
import random
screen_width, screen_height = 800, 600
pipelength = 25
pipehight = 25


def battleship_generator(type):
    if type == "4pipe":
        # Type 1. 1 4 pipe for player
        x = random.randint(1, int(screen_width/2) - 4 * pipelength)
        y = random.randint(1, int(screen_height/2) - pipehight)
        width = 4 * pipelength
    elif type == "3pipe":
        x = random.randint(1, int(screen_width/2) - 3 * pipelength)
        y = random.randint(1, int(screen_height/2) - pipehight)
        width = 3 * pipelength
    return x, y, width



# Initialize Pygame
pygame.init()

# Set up display

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Sea Battle Game")

# Colors
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)

player_ships = []

# Player ship
x, y, width = battleship_generator("4pipe")
player_ship1 = pygame.Rect(x, y, width, pipehight)

for i in range(2):
    x, y, width = battleship_generator("3pipe")
    player_ship = pygame.Rect(x, y, width, pipehight)
    player_ships.append(player_ship)

# Enemy ships (list of rectangles)
#enemy_ships = [pygame.Rect(100, 100, 50, 20), pygame.Rect(300, 150, 50, 20)]

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Player controls
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_ship.x -= 5
    if keys[pygame.K_RIGHT]:
        player_ship.x += 5

    # Draw everything
    screen.fill(WHITE)
    #
    pygame.draw.rect(screen, BLUE, player_ship)
    for ship in player_ships:
        pygame.draw.rect(screen, BLUE, ship)

    #for enemy in enemy_ships:
    #    pygame.draw.rect(screen, BLUE, enemy)

    pygame.display.flip()

