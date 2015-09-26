# -*- coding: utf-8 -*-

import unittest
import pytest
from .solution import encrypt, partition, replace, reverse


class EncryptionKitTestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_partition(self):
        assert partition('alazareselfacil', 3, 5, 8, 15) == ('aza', 'selfacil')

    def test_reverse(self):
        assert reverse('aza') == 'aza'
        assert reverse('selfacil') == 'licafles'

    def test_replace(self):
        assert replace('aza') == 'bab'
        assert replace('licafles') == 'mjdbgmft'

    def test_encryption(self):
        assert encrypt('alazareselfacil', 1, [(3, 5, 8, 15)]) == 'almjdbgmftrebab'
        assert encrypt('aa', 1, [(1, 1, 2, 2)]) == 'bb'

        assert encrypt(
            'alazareselfacil',
            2,
            [(3, 5, 8, 15),
            (3, 5, 8, 15)]) == 'alcbcfsugnbgekn'

        assert encrypt(
            'zabcdefghi',
            5,
            [(1, 1, 10, 10),
            (1, 5, 6, 10),
            (2, 4, 7, 9),
            (1, 1, 2, 10),
            (1, 8, 9, 10)]) == 'defghgjklm'

if __name__ == '__main__':
    pytest.main()
