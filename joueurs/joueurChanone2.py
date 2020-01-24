#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#

# d: defaite	v: victoire
# c: change	m: maintient
# n: NULL
#
# Contenu de la mémoire :
#
#   c/m m   c
# d-c-d 1   2
# | |-v 2   4
# |-m-d 4   2
# | |-v 5   3
# v-c-d 1   4
# | |-v 1   5
# |-m-d 7   6
#   |-v 1   7


import math
from joueurs.joueur import Joueur


class JoueurChanone2(Joueur):
    def __init__(self, nom, condVic):
        Joueur.__init__(self, nom, condVic)
        self.tactic = {'dcd': [1, 1], 'dcv': [1, 1], 'dmd': [1, 1],
                       'dmv': [1, 1], 'vcd': [1, 1], 'vcv': [1, 1],
                       'vmd': [1, 1], 'vmv': [1, 1]}
        self.derCoup = self.serie = ''

    def joue(self, jeu):
        # Les choix sont fait en fonction de la distribution
        if self.serie in self.tactic:
            res = self._choose(jeu, self.tactic[self.serie])
        # Si le comportement n'a pas de stats (impossible) ou cle innexistante
        else:
            res = self._joue(jeu)
        return res

    def clcl(self, coup, res):
        # compression = lambda x: pow(math.log(x), 2) + 1 # A améliorer
        if self.derCoup != '':
                # Mettre a jour la memoire du comportement
            if self.serie in self.tactic:
                if (coup == self.derCoup):  # pas adaptable si le but est de faire différent
                    self.tactic[self.serie][0] += 1
                else:
                    self.tactic[self.serie][1] += 1
                # if self.tactic[self.serie][0] + self.tactic[self.serie][1] >= 10:
                #     for i in range(len(self.tactic[self.serie])):
                #         self.tactic[self.serie][i] = compression(self.tactic[self.serie][i])
                # Mettre à jour la seirie de coups
            self.serie = self.serie[len(self.serie)-1:]   # a la deuxieme execution ca fait [-1:] d'une chaine vide, peu rigoureux
            if coup != self.derCoup:
                self.serie += 'c'
            else:
                self.serie += 'm'
            self.serie += res
        self.derCoup = coup
