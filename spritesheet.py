import pygame as pg

class SpriteSheet():
    def __init__(self, spr):
        self.sheet = spr

    def get_image(self, frame, w, h, scale):
        spr = pg.Surface((w, h), pg.SRCALPHA).convert_alpha()
        spr.blit(self.sheet, (0, 0), (0, (frame*h), w, h))
        spr = pg.transform.scale(spr, (w * scale, h * scale))

        return spr