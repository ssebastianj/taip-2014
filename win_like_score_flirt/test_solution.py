# -*- coding: utf-8 -*-

import unittest
import pytest
from .solution import calc_gallantry_count


class WinLikeScoreFlirtTestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_calc_gallantry_count(self):
        assert calc_gallantry_count([7, 8, 2, 10, 1, 4]) == 1
        # assert calc_gallantry_count([7, 8, 2, 10, 1, 3]) == 2
        assert calc_gallantry_count([60, 95, 100, 65]) == 0
        assert calc_gallantry_count([10, 10, 10, 10, 10, 10, 10, 10, 10, 10]) == -1

if __name__ == '__main__':
    pytest.main()
