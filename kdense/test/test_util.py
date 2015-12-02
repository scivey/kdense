import unittest
from .. import util

SEARCH_DATA = (
    5.3,
    7.8,
    9.6,
    11.2,
    15.3,
    18.7,
    25.18,
    43.59,
    47.2,
    58.1,
    61.2,
    62.17,
    63.89,
    65.6,
    67.92,
    83.5,
    96.2,
    107.58
)

class TestUtil(unittest.TestCase):
    def test_binsearch_closest_1(self):
        idx, point = util.binsearch_closest(23.1, list(SEARCH_DATA))
        self.assertEqual(5, idx)
        self.assertEqual(18.7, point)

    def test_binsearch_closest_2(self):
        idx, point = util.binsearch_closest(7.9, list(SEARCH_DATA))
        self.assertEqual(1, idx)
        self.assertEqual(7.8, point)

    def test_binsearch_closest_3(self):
        idx, point = util.binsearch_closest(97.8, list(SEARCH_DATA))
        self.assertEqual(16, idx)
        self.assertEqual(96.2, point)

    def test_binsearch_exact_1(self):
        idx, point = util.binsearch_closest(47.2, list(SEARCH_DATA))
        self.assertEqual(8, idx)
        self.assertEqual(47.2, point)

    def test_binsearch_exact_2(self):
        idx, point = util.binsearch_closest(83.5, list(SEARCH_DATA))
        self.assertEqual(15, idx)
        self.assertEqual(83.5, point)

    def test_binsearch_closest_before_any(self):
        idx, point = util.binsearch_closest(1.2, list(SEARCH_DATA))
        self.assertEqual(0, idx)
        self.assertEqual(5.3, point)

    def test_binsearch_closest_after_all(self):
        idx, point = util.binsearch_closest(206.8, list(SEARCH_DATA))
        self.assertEqual(17, idx)
        self.assertEqual(107.58, point)
