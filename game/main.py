import asyncio
import random
import sys
from pygame.font import Font

import pygame

from player import Player
from star import Star


FPS = 25
SCREEN_SIZE = (1200, 800)
PLAYER_SPEED = 30


async def main():
    pygame.init()
    screen: pygame.Surface = pygame.display.set_mode(SCREEN_SIZE)
    clock = pygame.time.Clock()
    font = Font(None, 36)

    all_sprites = pygame.sprite.Group()
    stars = pygame.sprite.Group()
    player = Player()
    all_sprites.add(player)

    score = 0

    while True:
        screen.fill('grey')

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()

        if random.randint(0, 10) == 0:
            star = Star(random.randint(0, SCREEN_SIZE[0]), 0)
            all_sprites.add(star)
            stars.add(star)

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            player.rect.x -= PLAYER_SPEED
        if keys[pygame.K_RIGHT]:
            player.rect.x += PLAYER_SPEED

        all_sprites.update()
        stars_collided = pygame.sprite.spritecollide(player, stars, True)
        for _ in stars_collided:
            score += 1

        all_sprites.draw(screen)
        text = font.render(f'Score: {score}', True, 'black')
        screen.blit(text, (10, 10))
        pygame.display.update()

        clock.tick(FPS)
        await asyncio.sleep(0)


if __name__ == '__main__':
    asyncio.run(main())
