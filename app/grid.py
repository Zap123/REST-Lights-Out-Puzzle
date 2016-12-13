from app.cell import Cell


class Grid:
    def __init__(self, height, width):
        self.height = height
        self.width = width
        self.level = self.initialize_grid()

    def initialize_grid(self):
        array_grid = []
        for i in range(self.height):
            array_grid.append([])
            for j in range(self.width):
                array_grid[i].append(Cell(0, (i, j), self))
        return array_grid

    def get_cell(self, x, y):
        return self.level[x][y]

    def serialize_level(self):
        array = []
        for i in range(self.height):
            array.append([])
            for j in range(self.width):
                ijl = self.get_cell(i, j)
                array[i].append({'state': ijl.state})
        return array

    @staticmethod
    def import_level(level):
        level_imported = level
        size = len(level_imported[0]), len(level_imported)
        grid = Grid(*size)
        array_grid = []
        for i in range(size[1]):
            array_grid.append([])
            for j in range(size[0]):
                ijstate = level_imported[i][j]['state']
                array_grid[i].append(Cell(ijstate, (i, j), grid))
        return array_grid

    def __str__(self):
        ret = []
        for i in range(self.height):
            ret.append("\n")
            for j in range(self.width):
                ret.append(str(self.get_cell(i, j).state))
        return "".join(ret)
