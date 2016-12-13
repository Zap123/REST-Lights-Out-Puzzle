import unittest
from app.game import Game


class TestGame(unittest.TestCase):
    def test_init(self):
        game = Game(6, 6)

        cell_01 = game.grid.get_cell(0, 1)
        cell_01.state = 1
        print(game.grid)
        game.event_grid(cell_01.pos[0], cell_01.pos[1])
        print(game.grid)

        self.assertCountEqual([1, 1, 1], [game.grid.get_cell(r[0], r[1]).state for r in [(0, 2), (0, 0), (1, 1)]])

    def test_cluster(self):
        game = Game(6, 6)

        cell_01 = game.grid.get_cell(0, 1)
        cell_01.state = 1
        cell_02 = game.grid.get_cell(0, 2)
        cell_02.state = 1
        cell_11 = game.grid.get_cell(1, 1)
        cell_11.state = 1

        cell_12 = game.grid.get_cell(1, 2)
        cell_12.state = 0

        print(game.grid)
        game.event_grid(cell_12.pos[0], cell_12.pos[1])
        print(game.grid)

        #FIXME
        #self.assertCountEqual([1, 1, 1], [game.grid.get_cell(r[0], r[1]).status for r in [(0, 2), (0, 0), (1, 1)]])



if __name__ == '__main__':
    unittest.main()
