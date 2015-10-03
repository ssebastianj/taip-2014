# -*- coding: utf-8 -*-

import unittest
import pytest
from .solution import find_lists_numbers


class FindMissingListsNumbersTestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_find_lists_number(self):
        assert find_lists_numbers([3, 1, 2, 4, 5]) == [2, 5]
        assert find_lists_numbers([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == [1, 4, 10]
