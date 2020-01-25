#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def check_nbr(nbr, min=0, max=300000, default=None):
    '''Check if a number match conditions.'''
    if nbr.isdigit():
        res = int(nbr)
        if min > res or res > max:  # add a check if it's an int
            res = default
    else:
        res = default

    return res


def check_in(choice, list_choice, case_sensitive=None, default=None):
    '''Check if a given element is in a list.'''
    if not case_sensitive:
        choice = choice.upper()
    if len(choice) != 1 or choice not in list_choice:
        choice = default

    return choice
