#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  pileOuFace.py
        
import random
import math
from jeux.joueur import Joueur

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
#

class JoueurChanone2(Joueur):
    def __init__(self, nom, condVic):
        Joueur.__init__(self, nom, condVic)
        self.prec = {'dcd':[1, 1], 'dcv':[1, 1], 'dmd':[1, 1],
                     'dmv':[1, 1], 'vcd':[1, 1], 'vcv':[1, 1],
                     'vmd':[1, 1], 'vmv':[1, 1]}
        self.derCoup = self.serie = ''

    def _joue(self, jeu):
        return random.choices(jeu)[0]

    def joue(self, jeu):
        if self.serie in self.prec: # Les choix sont fait en fonction de la distribution
            choix = random.choices(['m', 'c'], [self.prec[self.serie][0], self.prec[self.serie][1]])[0]
            if self.condVic(choix, 'c'):
                if self.derCoup == 'p':
                    res = 'f'
                else:
                    res = 'p'
            else:
                res = self.derCoup
        else:   # Si le comportement n'a pas de stats (impossible) ou cle innexistante
            res = self._joue(jeu)
            
        return res

        
    def clcl(self, coup, res):
        compression = lambda x: pow(math.log(x), 2) + 1
        # ~ compression = lambda x: x
        if self.derCoup != '':
                # Mettre a jour la memoire du comportement
            if self.serie in self.prec:
                if (coup == self.derCoup):
                    self.prec[self.serie][0] += 1
                else:
                    self.prec[self.serie][1] += 1
                if self.prec[self.serie][0] + self.prec[self.serie][1] >= 10:
                    for i in range(len(self.prec[self.serie])):
                        self.prec[self.serie][i] = compression(self.prec[self.serie][i])
                # Mettre à jour la serie de coups
            self.serie = self.serie[len(self.serie)-1:]   # a la deuxieme execution ca fait [-1:] d'une chaine vide, peu rigoureux
            if coup != self.derCoup:
                self.serie += 'c'
            else:
                self.serie += 'm'
            self.serie += res
        self.derCoup = coup
