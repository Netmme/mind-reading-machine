#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import sys
from ranking.elo_score import expected
from ranking.elo_score import points_transfer
from tests.ranking.player_test_score import PlayerTestScore


def test_elo():
    k_factor = 32
    p1 = PlayerTestScore('Alice', 1900)
    p2 = PlayerTestScore('Bob', 1500)

    expected_alice = expected(p1.mean, p2.mean)
    expected_bob = expected(p2.mean, p1.mean)
    bob_win = points_transfer(1, expected_bob, k_factor)
    bob_draw = points_transfer(0.5, expected_bob, k_factor)
    bob_loss = points_transfer(0, expected_bob, k_factor)
    print("Alice's expected chance to win:", expected_alice)
    print("Bob's expected chance to win:", expected_bob)
    print("Bob wins:", bob_win)
    print("Bob draws:", bob_draw)
    print("Bob looses:", bob_loss)


def main(arg):
    basic_test()


if __name__ == '__main__':
    main(sys.argv)
