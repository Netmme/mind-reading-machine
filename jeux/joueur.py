#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  pileOuFace.py


from os import urandom


class Joueur():
    def __init__(self, nom, condVic):
        self.nom = nom
        self.condVic = condVic

    """ /!\ Transformation de la donnée: un mot devient une lettre"""
    def _swap(self, choice):
        if choice == 'p':
            res = 'f'
        else:
            res = 'p'
        return res

    def _toVictory(self, choice):
        if not self.condVic(choice, choice):
            choice = self._swap(choice)
        return choice

    def _choose(self, possibilities, poids):
        def sum_list(l):
            tot = 0
            for i in l:
                tot += i
            return tot

        tot = sum_list(poids)
        rand = urandom(tot)
        ind_choice = int.from_bytes(rand, 'big') % tot
        i = 1
        while ind_choice >= sum_list(poids[:i]) and i + 1 < len(possibilities):
            i += 1
        if ind_choice < sum_list(poids[:i]):
            the_choice = possibilities[i - 1]
        else:
            the_choice = possibilities[i]
        the_choice = self._toVictory(the_choice)
        return the_choice

    def _joue(self, jeu):
        return self._choose(jeu, [1 for i in jeu])

    def joue(self, jeu):
        return self._joue(jeu)

    def clcl(self, coup, res):
        pass
