from app.grid import Grid
from app.cellgame import Cellgame

class Game:
    def __init__(self, height, width):
        self.height = height
        self.width = width
        self.status = "running"
        self.grid = Grid(height, width)
        self.rules = Cellgame()

    def event_grid(self, x, y):
        self.rules.move(self.grid.get_cell(x, y), self.grid)


