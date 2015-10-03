# -*- coding: utf-8 -*-

import unittest
import pytest
from .solution import check_mixing_randomness


class RandomCardsTestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_card_mixing_randomness(self):
        assert check_mixing_randomness([('1', 'b'), ('2', 'c'),
                                        ('3', 'e'), ('4', 'o')])  == 'B'

        assert check_mixing_randomness([('1', 'b'), ('2', 'b'),
                                        ('3', 'c')]) == 'M'

        assert check_mixing_randomness([('1', 'b'), ('1', 'c'),
                                        ('2', 'e')]) == 'M'

        assert check_mixing_randomness([('5', 'c'), ('2', 'b'), ('4', 'e'),
                                        ('3', 'o'), ('12', 'b'), ('1', 'c'),
                                        ('7', 'e'), ('6', 'c'), ('12', 'e'),
                                        ('4', 'o'), ('1', 'b'), ('6', 'o'),
                                        ('3', 'e'), ('12', 'o'), ('11', 'e'),
                                        ('12', 'c'), ('5', 'o'), ('10', 'b'),
                                        ('9', 'o'), ('3', 'c'), ('4', 'b'),
                                        ('11', 'c'), ('8', 'e'), ('9', 'c'),
                                        ('1', 'e'), ('4', 'c'), ('8', 'b'),
                                        ('2', 'o'), ('6', 'b'), ('9', 'e'),
                                        ('7', 'b'), ('5', 'e')]) == 'B'
