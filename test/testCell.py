import unittest
from app.cell import Cell
from app.grid import Grid


class TestCell(unittest.TestCase):
    def test_init(self):
        c = Cell(0, (1, 1), Grid(4, 3))
        self.assertEqual(c.pos, (1, 1))


if __name__ == '__main__':
    unittest.main()
