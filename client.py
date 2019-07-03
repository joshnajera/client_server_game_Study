import pygame
from network import Network
from player import player

width = 500
height = 500

win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Client")


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
    p = n.get_player()

    # GAME LOOP
    while running:
        clock.tick(60)

        # Send current position, and receive other player's position
        p2 = n.send(p)

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
