class Cellgame:
    def __init__(self):
        pass

    def move(self, cell, grid):
        cells_to_change = [cell] + cell.neighbours_cells(grid)
        self.invert_cells(cells_to_change)

    @classmethod
    def invert_cells(cls, cells):
        for cell in cells:
            cell.state = 1 - cell.state

    def is_game_over(self, grid):
        array = []
        for i in range(grid.height):
            array.append([])
            for j in range(grid.width):
                ijl = grid.get_cell(i, j)
                if ijl.state != 1:
                    return False
        return True
