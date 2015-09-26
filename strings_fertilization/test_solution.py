# -*- coding: utf-8 -*-

import unittest
import pytest
from .solution import observar


class StringsFertilization(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_observar(self):
        assert observar(
            2,
            [(0, 'aa', 1),
            (0, 'ba', 1),
            (1, 'ba', 2),
            (2, 'aa', 2)]) == [1, 2, 1, 2]

        assert observar(
            26,
            [(0, 'abcdefghijklmnopqrstuvwxyz', 1),
            (1, 'bcdefghijklmnopqrstuvwxyza', 2),
            (1, 'cdefghijklmnopqrstuvwxyzab', 3),
            (1, 'defghijklmnopqrstuvwxyzabc', 4),
            (1, 'efghijklmnopqrstuvwxyzabcd', 5),
            (1, 'fghijklmnopqrstuvwxyzabcde', 6),
            (1, 'ghijklmnopqrstuvwxyzabcdef', 7),
            (1, 'hijklmnopqrstuvwxyzabcdefg', 8),
            (1, 'ijklmnopqrstuvwxyzabcdefgh', 9),
            (1, 'jklmnopqrstuvwxyzabcdefghi', 10),
            (1, 'klmnopqrstuvwxyzabcdefghij', 11),
            (1, 'lmnopqrstuvwxyzabcdefghijk', 12),
            (1, 'mnopqrstuvwxyzabcdefghijkl', 13),
            (1, 'nopqrstuvwxyzabcdefghijklm', 14),
            (1, 'opqrstuvwxyzabcdefghijklmn', 15),
            (1, 'pqrstuvwxyzabcdefghijklmno', 16),
            (1, 'qrstuvwxyzabcdefghijklmnop', 17),
            (1, 'rstuvwxyzabcdefghijklmnopq', 18),
            (1, 'stuvwxyzabcdefghijklmnopqr', 19),
            (1, 'tuvwxyzabcdefghijklmnopqrs', 20),
            (1, 'uvwxyzabcdefghijklmnopqrst', 21),
            (1, 'vwxyzabcdefghijklmnopqrstu', 22),
            (1, 'wxyzabcdefghijklmnopqrstuv', 23),
            (1, 'xyzabcdefghijklmnopqrstuvw', 24),
            (1, 'yzabcdefghijklmnopqrstuvwx', 25),
            (1, 'zabcdefghijklmnopqrstuvwxy', 26)]) == [1, 1, 1, 1, 1, 1, 1, 1,
                                                        1, 1, 1, 1, 1,1, 1, 1,
                                                        1, 1, 1, 1, 1, 1, 1, 1,
                                                        1, 1]

if __name__ == '__main__':
    pytest.main()
