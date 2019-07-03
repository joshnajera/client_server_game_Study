import pygame

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
