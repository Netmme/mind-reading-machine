#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  pileOuFace.py

import sys
from os import urandom
from imprandom.imprandom import ponderate_choice

sys.path.append('../')


class Joueur():
    def __init__(self, nom, condVic):
        self.nom = nom
        self.condVic = condVic

    def _swap(self, choice):
        """ ! Transformation de la donnée: un mot devient une lettre"""
        if choice == 'p':
            res = 'f'
        else:
            res = 'p'
        return res

    def _toVictory(self, choice):
        if not self.condVic(choice, choice):
            choice = self._swap(choice)
        return choice

    def _choose(self, poss, weight):
        return ponderate_choice(weight, poss)

    def _joue(self, jeu):
        return self._choose(jeu, [1 for i in jeu])

    def joue(self, jeu):
        return self._joue(jeu)

    def clcl(self, coup, res):
        pass
