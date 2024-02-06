import pygame
import os
import sys


class Car(pygame.sprite.Sprite):
    def __init__(self, size, group):
        super().__init__()
        self.image = load_image("car2.png")
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = size[1] // 15
        self.speed = 1
        self.velocity = self.speed
        self.size = size
        group.add(self)
        self.flipped_im = pygame.transform.flip(self.image, True, False)

    def update(self, *args):
        # Move
        if self.rect.right >= self.size[0]:
            self.direction = -1
        elif self.rect.left <= 0:
            self.direction = 1
        self.rect.x += self.speed * self.direction
        if self.direction == -1:
            self.image = self.flipped_im
        elif self.direction == 1:
            self.image = load_image("car2.png")


def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    if colorkey is not None:
        image = image.convert()
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    else:
        image = image.convert_alpha()
    return image


def main():
    pygame.init()
    size = 600, 95
    screen = pygame.display.set_mode(size)
    screen.fill((0, 0, 0))

    all_sprites = pygame.sprite.Group()
    car = Car(size, all_sprites)

    running = True
    clock = pygame.time.Clock()
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        all_sprites.update()

        screen.fill((255, 255, 255))
        all_sprites.draw(screen)
        pygame.display.flip()

        clock.tick(60)

    pygame.quit()


if __name__ == '__main__':
    main()
