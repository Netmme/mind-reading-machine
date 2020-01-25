#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import argparse


def configure_parser():
    parser = argparse.ArgumentParser(description='Player 1 has to guess '
                                                 + 'right the choice of '
                                                 + 'Player 2. Player 2 wins '
                                                 + 'when Player 1 is wrong.')
    subparsers = parser.add_subparsers(help='Different utilisations\' mode.',
                                       dest='mode')

    # Play mode's parser
    parser_play = subparsers.add_parser('play', help='Play mode.')
    parser_play.add_argument('--hand',
                             help='How many hand should be the game.')
    parser_play.add_argument('-p1 --player1',
                             help='Store the type of player 1.')
    parser_play.add_argument('-p2 --player2',
                             help='Store the type of player 2.')

    return parser


if __name__ == '__main__':
    pass
