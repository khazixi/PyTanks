import math
import pygame as pg


class Player(pg.sprite.Sprite):
    def __init__(self, groups: pg.sprite.AbstractGroup | None = None) -> None:
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface((64, 64))
        self.image.fill((255, 255, 0))
        self.rect = self.image.get_rect()
        self.rect.center = (200, 200)

    def update(self):
        self.dx: float = 0
        self.dy: float = 0
        keystate = pg.key.get_pressed()
        mousepos = pg.mouse.get_pos()
        mousestate = pg.mouse.get_pressed()
        if keystate[pg.K_w]:
            self.dy = -5
        if keystate[pg.K_a]:
            self.dx = -5
        if keystate[pg.K_s]:
            self.dy = 5
        if keystate[pg.K_d]:
            self.dx = 5
        if mousestate[0]:
            if self.groups():
                bullet = Bullet(math.atan2(mousepos[1] - self.rect.y,
                                mousepos[0] - self.rect.x),
                                (self.rect.x + self.rect.width/2,
                                 self.rect.y + self.rect.height/2))
                self.groups()[0].add(bullet)
        if not self.dx or not self.dy:
            self.dx /= 1.414
            self.dy /= 1.414
        self.rect.x += self.dx
        self.rect.y += self.dy


class Bullet(pg.sprite.Sprite):
    def __init__(self, angle: float, position: tuple[int, int], *,
                 groups: pg.sprite.AbstractGroup | None = None) -> None:
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface((32, 32))
        self.image.fill((255, 128, 0))
        self.rect = self.image.get_rect()
        self.rect.center = position
        self.radian = angle

    def update(self):
        self.rect.x += 5 * math.cos(self.radian)
        self.rect.y += 5 * math.sin(self.radian)
        if (self.rect.x < 0 or self.rect.x > 800 or
           self.rect.y < 0 or self.rect.y > 600):
            self.kill()
