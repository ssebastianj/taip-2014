# -*- coding: utf-8 -*-

import unittest
import pytest
from  .solution import calc_minimum_travels


class CalcMininumTravelsTestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_calc_minimum_travels(self):
        assert calc_minimum_travels([4, 5, 2, 3, 1]) == 3
        assert calc_minimum_travels([1, 2, 3]) == 1
        assert calc_minimum_travels([9, 4, 2, 7, 8, 3, 5, 6, 1]) == 4
