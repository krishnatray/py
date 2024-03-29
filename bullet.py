import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """A class to manage bullets fired from the ship"""

    def __init__(self, ai_game):
        """Create a bullet object at the ship's current position."""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = (204, 229, 255)
        self.screen_rect = ai_game.screen.get_rect()
        self.image = pygame.image.load('images/bullet.bmp')
        # Create a bullet rect at (0, 0) and then set correct position.
        #self.rect = pygame.Rect(0, 0, self.settings.bullet_width,
        #    self.settings.bullet_height)


        self.rect = self.image.get_rect()

        self.rect.midtop = ai_game.ship.rect.midtop


        # Start each new ship at the bottom center of the screen.
        self.rect.midbottom = self.screen_rect.midbottom

        # Store a decimal value for the ship's horizontal position.
        self.x = float(self.rect.x)


        # Store the bullet's position as a decimal value.
        self.y = float(self.rect.y)

    def update(self):
        """Move the bullet up the screen."""
        # Update the decimal position of the bullet.
        self.y -= self.settings.bullet_speed
        # Update the rect position.
        self.rect.y = self.y

    def draw_bullet(self):
        """Draw the bullet to the screen."""
        pygame.draw.rect(self.screen, self.color, self.rect)
        self.screen.blit(self.image, self.rect)
