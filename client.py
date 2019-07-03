import pygame
from network import Network
width = 500
height = 500

win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Client")

clientNumber = 0


class player():
    """Represents the player in the online game"""

    def __init__(self, x, y, width, height, color):
        self.y = y
        self.x = x
        self.width = width
        self.height = height
        self.color = color
        self.rect = (x, y, width, height)
        self.velocity = 3

    def draw(self, win):
        """Draws self on given window"""
        pygame.draw.rect(win, self.color, self.rect)

    def move(self):
        """Move according to arrow keys"""
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.x -= self.velocity
        if keys[pygame.K_RIGHT]:
            self.x += self.velocity
        if keys[pygame.K_UP]:
            self.y -= self.velocity
        if keys[pygame.K_DOWN]:
            self.y += self.velocity
        self.update()

    def update(self):
        """Update the self.rect according to self's dimensions"""
        self.rect = (self.x, self.y, self.width, self.height)


def read_pos(str):
    """Convert string to a position tuple"""
    str = str.split(",")
    return int(str[0]), int(str[1])


def make_pos(tup):
    """Converts tuple to a string as 'x,y' """
    return str(tup[0]) + "," + str(tup[1])


def redraw_window(win, player, player2):
    win.fill((255, 255, 255))
    player2.draw(win)
    player.draw(win)
    pygame.display.update()


def main():
    # SETUP
    running = True
    clock = pygame.time.Clock()

    n = Network()
    start_pos = read_pos(n.getPos())

    p2 = player(0, 0, 100, 100, (128, 0, 0))
    p = player(start_pos[0], start_pos[1], 100, 100, (0, 128, 0))

    # GAME LOOP
    while running:
        clock.tick(60)

        # Send current position, and receive other player's position
        my_pos = make_pos((p.x, p.y))
        response = n.send(my_pos)
        p2Pos = read_pos(response)
        print(p2Pos)

        # Update other player's position
        p2.x = p2Pos[0]
        p2.y = p2Pos[1]
        p2.update()

        # EVENTS
        for event in pygame.event.get():
            # QUIT Event
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                break

        # Break out before anything else if game is no longer running
        if not running:
            break

        p.move()
        redraw_window(win, p, p2)


main()
