#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import unittest
from utils.utils import check_nbr


class TestCheckNbr(unittest.TestCase):
    '''Test the utils functions.'''

    def setUp(self):
        pass

    def test_check_nbr_correct(self):
        '''Test for a correct entry.'''

        test_nbr = '42'
        res = check_nbr(test_nbr, min=10, max=300000, default=None)
        self.assertEqual(res, int(test_nbr))

    def test_check_nbr_too_big(self):
        '''Test for a number too big.'''

        res = check_nbr('300001', min=10, max=300000, default=None)
        self.assertEqual(res, None)

    def test_check_nbr_too_small(self):
        '''Test for a number too small.'''

        res = check_nbr('0', min=10, max=300000, default=None)
        self.assertEqual(res, None)

    def test_check_nbr_smallest(self):
        '''Test for the smallest number.'''

        test_min = '10'
        res = check_nbr(test_min, min=int(test_min), max=300000, default=None)
        self.assertEqual(res, int(test_min))

    def test_check_nbr_biggest(self):
        '''Test for the biggest number.'''

        test_max = '300000'
        res = check_nbr(test_max, min=10, max=int(test_max), default=None)
        self.assertEqual(res, int(test_max))

    def test_check_nbr_nan(self):
        '''Test for not a number.'''

        res = check_nbr('Graal', min=10, max=300000, default=None)
        self.assertEqual(res, None)


if __name__ == '__main__':
    unittest.main()
