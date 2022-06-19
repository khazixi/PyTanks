import pygame as pg

import entities.player


class Game:
    def __init__(self):
        pg.init()
        pg.mixer.init()
        self.screen = pg.display.set_mode((800, 600))  # NEEDS ARG
        pg.display.set_caption("Game Window")  # NEEDS ARG
        self.clock = pg.time.Clock()
        self.running = True

    def new(self):
        player = entities.player.Player()
        self.all_sprites = pg.sprite.Group()
        self.all_sprites.add(player)
        self.run()

    def run(self):
        self.playing = True
        while self.playing:
            self.clock.tick(60)  # NEEDS ARG
            self.events()
            self.update()
            self.draw()
            pg.display.flip()

    def update(self):
        self.all_sprites.update()

    def events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                if self.playing:
                    self.playing = False
                self.running = False
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    if self.playing:
                        self.playing = False
                    self.running = False

    def draw(self):
        self.screen.fill((128, 0, 128))  # NEEDS ARG
        self.all_sprites.draw(self.screen)

    def draw_text(self, text, size, color, x, y):
        font = pg.font.Font('Skia', size)  # NEEDS ARG
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect()
        text_rect.midtop = (x, y)
        self.screen.blit(text_surface, text_rect)


if __name__ == "__main__":
    g = Game()
    g.new()
