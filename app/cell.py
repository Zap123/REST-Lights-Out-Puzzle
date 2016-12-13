class Cell:
    def __init__(self, state, pos, grid):
        self.state = state
        self.pos = pos
        self.cluster = []

    def neighbours(self, grid):
        grid_size = {'height': grid.height, 'width': grid.width}
        pos = self.pos
        n4list = []
        if pos[0] > 0:
            n4list.append((pos[0] - 1, pos[1]))  # up
        if pos[1] < grid_size['width'] - 1:
            n4list.append((pos[0], pos[1] + 1))  # right
        if pos[1] > 0:
            n4list.append((pos[0], pos[1] - 1))  # left
        if pos[0] < grid_size['height'] - 1:
            n4list.append((pos[0] + 1, pos[1]))  # down

        return n4list

    def neighbours_cells(self, grid):
        """convert positions to cells"""
        npos = self.neighbours(grid)
        nlist = [grid.get_cell(n[0], n[1]) for n in npos]
        return nlist
