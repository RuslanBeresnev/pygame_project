from Cell import Cell
from functions import get_full_file_name


class Location:
    def __init__(self, filename, cells_group, start_pos_x, start_pos_y):
        self.cells_group = cells_group
        self.start_pos_x = start_pos_x
        self.start_pos_y = start_pos_y

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
        cell = None

        for i in range(len(self.map)):
            for j in range(len(self.map[i])):
                if self.map[i][j] == 'ffff':
                    cell = Cell(self.cells_group, 'field', x, y)
                elif self.map[i][j] == 'gggg':
                    cell = Cell(self.cells_group, 'grass', x, y)
                elif self.map[i][j] == 'pppp':
                    cell = Cell(self.cells_group, 'pebbles', x, y)
                elif self.map[i][j] == 'psps':
                    cell = Cell(self.cells_group, 'paving stones', x, y)
                elif self.map[i][j] == 'pswg':
                    cell = Cell(self.cells_group, 'paving stones with grass', x, y)

                cell.moving_rect[0] = x
                cell.moving_rect[1] = y
                x += cell.width
            x = self.start_pos_x
            y += cell.height