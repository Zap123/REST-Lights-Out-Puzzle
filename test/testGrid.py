import unittest
from app.grid import Grid

import json


class TestGrid(unittest.TestCase):
    def test_init(self):
        g = Grid(4, 3)
        cell_12 = g.get_cell(1, 2)
        print(cell_12.pos)
        print(g)
        self.assertEqual(cell_12.pos, (1, 2))

    def test_neighbours12(self):
        g = Grid(4, 3)
        cell_12 = g.get_cell(1, 2)
        print(cell_12.neighbours(g))
        self.assertCountEqual(cell_12.neighbours(g), [(0, 2), (2, 2), (1, 1)])

    def test_neighbours00(self):
        g = Grid(4, 3)
        cell_00 = g.get_cell(0, 0)
        print(cell_00.neighbours(g))
        self.assertCountEqual(cell_00.neighbours(g), [(1, 0), (0, 1)])

    def test_neighbours002(self):
        g = Grid(4, 3)
        cell_00 = g.get_cell(0, 0)
        n = cell_00.neighbours(g)

        self.assertCountEqual([n.pos for n in cell_00.neighbours_cells(g)], [(1, 0), (0, 1)])

    def test_serialize(self):
        g = Grid(4, 3)
        level_dict = g.serialize_level()

        print(level_dict)
        level_json = json.dumps(level_dict)
        print(level_dict[1][1])
        # self.assertCountEqual([n.pos for n in cell_00.neighbours_cells()], [(1,0),(0,1)])

    def test_import_level(self):
        g = Grid(4, 3)
        level_dict = g.serialize_level()

        level = g.import_level(level_dict)
        print(g)
        # self.assertCountEqual([n.pos for n in cell_00.neighbours_cells()], [(1,0),(0,1)])


if __name__ == '__main__':
    unittest.main()
