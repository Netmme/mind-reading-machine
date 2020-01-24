#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import sys


def expected(rating_a, rating_b):
    denominator = 1 + pow(10, (rating_b - rating_a)/400)
    expected = 1/denominator

    return expected


def points_transfer(score, expected, k_factor):
    rating_diff = (score - expected) * k_factor

    return rating_diff


def main(arg):
    pass


if __name__ == '__main__':
    main(sys.argv)
