from functions import get_full_file_name
from Cell import Cell
from TerrainObject import TerrainObject
import random
from Group import Group


class Location:
    def __init__(self, filename, objects_group, type, start_pos_x, start_pos_y, sheet=None):
        self.objects_group = objects_group
        self.type = type
        self.start_pos_x = start_pos_x
        self.start_pos_y = start_pos_y
        self.sheet = sheet

        self.filename = get_full_file_name(filename)
        self.map = []
        with open(self.filename, 'r') as mapfile:
            while True:
                firstline = mapfile.readline()
                if firstline == '':
                    break
                secondline = mapfile.readline()
                row = []
                for i in range(0, len(firstline) - 1, 2):
                    row.append(firstline[i] + firstline[i + 1] + secondline[i] + secondline[i + 1])
                self.map.append(row)
            mapfile.close()

    def location_creating(self):
        x = self.start_pos_x
        y = self.start_pos_y
        location_object = None

        for i in range(len(self.map)):
            row_of_location = Group()
            for j in range(len(self.map[i])):
                if self.type == 'surface':
                    if self.map[i][j] == 'ffff':
                        location_object = Cell(self.objects_group, 'field', x, y)
                    elif self.map[i][j] == 'pppp':
                        location_object = Cell(self.objects_group, 'pebbles', x, y)
                    elif self.map[i][j] == 'psps':
                        location_object = Cell(self.objects_group, 'paving stones', x, y)
                    elif self.map[i][j] == 'pswg':
                        location_object = Cell(self.objects_group, 'paving stones with grass', x, y)
                    elif self.map[i][j] == 'tttt':
                        location_object = Cell(self.objects_group, 'trail', x, y)

                    location_object.moving_rect[0] = x
                    location_object.moving_rect[1] = y
                elif self.type == 'terrain':
                    if self.map[i][j] == '....':
                        x += Cell.width
                        continue
                    elif self.map[i][j] == 'ssss':
                        location_object = self.spawn_spruce(x, y)

                    row_of_location.add(location_object)

                x += Cell.width

            if self.type == 'terrain' and len(row_of_location.get_sprites()) > 1:
                self.setup_row_of_location(row_of_location)
            x = self.start_pos_x
            y += Cell.height

    def spawn_spruce(self, cell_x, cell_y):
        image = TerrainObject.object_images['spruce']
        spruce_width = int(image.get_width() / 2.5)
        spruce_height = int(image.get_height() / 2.5)
        stem_width = int(image.get_width() / 3.5)
        spawn_x = random.randint(cell_x - int((spruce_width - stem_width) / 2), cell_x + Cell.width - stem_width)
        spawn_y = random.randint(cell_y - spruce_height, cell_y + Cell.height - spruce_height)
        spruce = TerrainObject(self.objects_group, 'spruce', spawn_x, spawn_y,
                               spruce_width, spruce_height)

        spruce.moving_rect[0] = spawn_x
        spruce.moving_rect[1] = spawn_y

        return spruce

    def setup_row_of_location(self, row):
        row = Group(sorted(row.get_sprites(), key=lambda sprite: sprite.rect.y))
        for i in range(len(row.get_sprites())):
            self.objects_group.remove(-1 - i)
            self.objects_group.add(row.get_sprites()[i])