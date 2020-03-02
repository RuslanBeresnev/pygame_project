class Group:
    def __init__(self, sprites=None):
        if sprites is None:
            self.sprites = []
        else:
            self.sprites = sprites

    def get_sprites(self):
        return self.sprites

    def add(self, sprite):
        self.sprites.append(sprite)

    def replace(self, position1, position2):
        self.sprites[position1], self.sprites[position2] = self.sprites[position2], self.sprites[position1]

    def remove(self, position):
        self.sprites.pop(position)

    def clear(self):
        self.sprites = []

    def swap_groups(self, group):
        self_copy = self.get_sprites().copy()

        self.clear()
        for sprite in group.get_sprites():
            self.add(sprite)

        group.clear()
        for sprite in self_copy:
            group.add(sprite)

    def update(self):
        for sprite in self.sprites:
            sprite.update()

    def draw(self, surface):
        for sprite in self.sprites:
            surface.blit(sprite.image, (sprite.rect.x, sprite.rect.y))