#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import unittest

from ranking.elo_score import expected
from ranking.elo_score import points_transfer

from tests.ranking.player_test_score import PlayerTestScore


class TestElo(unittest.TestCase):
    '''Test the ELO score.'''

    def setUp(self, alice_mean=1900, bob_mean=1500,
              expected_alice=0.9, expected_bob=0.1,
              k_factor=32, bob_win=29, bob_draw=13, bob_loss=-3):
        # Initializing players for tests purpose
        self.p1 = PlayerTestScore('Alice', alice_mean)
        self.p2 = PlayerTestScore('Bob', bob_mean)
        # Saving reference values for tests
        self.expected_alice = expected_alice
        self.expected_bob = expected_bob
        self.bob_win = bob_win
        self.bob_draw = bob_draw
        self.bob_loss = bob_loss
        self.k_factor = k_factor

    def test_expected(self):
        '''The function give the correct expected chance to win.'''
        expected_alice = round(expected(self.p1.mean, self.p2.mean), 1)
        expected_bob = round(expected(self.p2.mean, self.p1.mean), 1)
        self.assertEqual(expected_alice, self.expected_alice)
        self.assertEqual(expected_bob, self.expected_bob)

    def test_points_transfer_win(self):
        '''Test transfer point in case of win.'''
        bob_win = round(
            points_transfer(1, self.expected_bob, self.k_factor),
            0)
        self.assertEqual(bob_win, self.bob_win)

    def test_points_transfer_draw(self):
        '''Test transfer point in case of draw.'''
        bob_draw = round(
            points_transfer(0.5, self.expected_bob, self.k_factor),
            0)
        self.assertEqual(bob_draw, self.bob_draw)

    def test_points_transfer_loss(self):
        '''Test transfer point in case of loss.'''
        bob_loss = round(
            points_transfer(0, self.expected_bob, self.k_factor),
            0)
        self.assertEqual(bob_loss, self.bob_loss)


if __name__ == '__main__':
    unittest.main()
