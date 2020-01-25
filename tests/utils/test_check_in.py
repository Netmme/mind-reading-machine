#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import unittest
from utils.utils import check_in


class TestCheckIn(unittest.TestCase):
    '''Test the check_in utils functions.'''

    def setUp(self):
        pass

    def test_check_in_correct(self):
        '''Test a correct entry non case sensitive.'''

        letter_test = 'h'
        res = check_in(letter_test, 'HM')
        self.assertEqual(res, letter_test.upper())

    def test_check_in_correct_case_sensitive(self):
        '''Test a correct entry case sensitive.'''

        letter_test = 'H'
        res = check_in(letter_test, 'HM', case_sensitive=True)
        self.assertEqual(res, letter_test)

    def test_check_in_incorrect(self):
        '''Test a incorrect entry non case sensitive.'''

        letter_test = 'P'
        res = check_in(letter_test, 'HM')
        self.assertEqual(res, None)

    def test_select_letter_in_incorrect_case_sensitive(self):
        '''Test a incorrect entry case sensitive.'''

        letter_test = 'h'
        res = check_in(letter_test, 'HM', case_sensitive=True)
        self.assertEqual(res, None)

    def test_check_in_nal(self):
        '''Test a multientry.'''

        letter_test = 'GRAAL'
        res = check_in(letter_test, 'HM')
        self.assertEqual(res, None)


if __name__ == '__main__':
    unittest.main()
