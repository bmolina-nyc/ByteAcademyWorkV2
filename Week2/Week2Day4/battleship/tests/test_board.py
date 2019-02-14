import unittest
from gameboard import GameBoard


class TestBoard(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_get_set(self):
        gb = GameBoard(5, 5)
        gb[1, 1] = 'S'
        self.assertEqual(gb[1, 1], 'S', 'setitem and getitem work as expected')

    def test_count(self):
        gb = GameBoard(5, 5)
        gb[3, 3] = 'X'
        self.assertEqual(gb.count('X'), 1, 'count should correctly count placed tiles')
