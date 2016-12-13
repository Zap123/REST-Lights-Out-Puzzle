import unittest
from app.cellgame import Cellgame
from app.grid import Grid


class TestCellgame(unittest.TestCase):
    def test_move01(self):
        g = Grid(4, 3)
        c = Cellgame()
        cell_01 = g.get_cell(0, 1)
        cell_01.state = 1
        print(g)
        print(cell_01.neighbours_cells(g))
        c.move(cell_01, g)
        print(g)

        self.assertCountEqual([1, 1, 1], [g.get_cell(r[0], r[1]).state for r in [(0, 2), (0, 0), (1, 1)]])

    def test_move21(self):
        g = Grid(4, 3)
        cell_21 = g.get_cell(2, 1)
        cell_21.state = 1
        c = Cellgame()
        print(g)
        print(cell_21.neighbours(g))
        c.move(cell_21, g)
        print(g)
        self.assertCountEqual([1, 1, 1, 1], [g.get_cell(r[0], r[1]).state for r in [(1, 1), (2, 2), (2, 0), (3, 1)]])

    def test_move00_blank(self):
        g = Grid(4, 3)
        cell_00 = g.get_cell(0, 0)
        c = Cellgame()
        print(g)
        print(cell_00.neighbours(g))
        c.move(cell_00, g)
        print(g)
        print(repr(g))
        self.assertCountEqual([1, 1, 1], [g.get_cell(r[0], r[1]).state for r in [(0, 0), (0, 1), (1, 0)]])

    def test_move32(self):
        g = Grid(4, 3)
        cell_21 = g.get_cell(3, 2)
        cell_21.state = 1
        c = Cellgame()
        print(g)
        print(cell_21.neighbours(g))
        c.move(cell_21, g)
        print(repr(g))
        print(g)
        self.assertCountEqual([1, 1], [g.get_cell(r[0], r[1]).state for r in [(2, 2), (3, 1)]])

    def test_move32_blank(self):
        g = Grid(4, 3)
        cell_32 = g.get_cell(3, 2)
        c = Cellgame()
        print(g)
        print(cell_32.neighbours(g))
        c.move(cell_32, g)
        print(g)
        self.assertCountEqual([1, 1, 1], [g.get_cell(r[0], r[1]).state for r in [(2, 2), (3, 2), (3, 1)]])

    def test_move21_blank_square(self):
        g = Grid(4, 4)
        cell_21 = g.get_cell(2, 1)
        c = Cellgame()
        print(g)
        print(cell_21.neighbours(g))
        c.move(cell_21, g)
        print(g)
        self.assertCountEqual([1, 1, 1, 1, 1], [g.get_cell(r[0], r[1]).state for r in [(1, 1), (2, 2), (2, 1), (2, 0), (3, 1)]])

    def test_move23_blank_square(self):
        g = Grid(4, 4)
        cell_23 = g.get_cell(2, 3)
        c = Cellgame()
        print(g)
        print(cell_23.neighbours(g))
        c.move(cell_23, g)
        print(g)
        self.assertCountEqual([1, 1, 1, 1], [g.get_cell(r[0], r[1]).state for r in [(1, 3), (2, 2), (3, 3), (2, 3)]])

if __name__ == '__main__':
    unittest.main()
