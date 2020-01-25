#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import unittest
from utils.utils import enter_nbr
from utils.utils import select_letter_in


class TestUtils(unittest.TestCase):
    '''Test the utils functions.'''

    def setUp(self):
        pass

    def test_enter_nbr_correct(self):
        test_nbr = 42
        res = check_nbr(test_nbr, min=10, max=300000, default=None)
        self.assertEqual(res, test_nbr)

    def test_enter_nbr_too_big(self):
        res = check_nbr(300001, min=10, max=300000, default=None)
        self.assertEqual(res, None)

    def test_enter_nbr_too_small(self):
        res = check_nbr(0, min=10, max=300000, default=None)
        self.assertEqual(res, None)

    def test_enter_nbr_smallest(self):
        test_min = 10
        res = check_nbr(test_min, min=test_min, max=300000, default=None)
        self.assertEqual(res, test_min)

    def test_enter_nbr_biggest(self):
        test_max = 300000
        res = check_nbr(test_max, min=10, max=test_max, default=None)
        self.assertEqual(res, test_max)

    def test_enter_nbr_nan(self):
        res = check_nbr('Graal', min=10, max=300000, default=None)
        self.assertEqual(res, None)

    def test_select_letter_in(self):
        pass
