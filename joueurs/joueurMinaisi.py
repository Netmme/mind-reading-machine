#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  pileOuFace.py


import re
import time
from jeux.joueur import Joueur


class JoueurMinaisi(Joueur):
    def __init__(self, nom, condVic):
        Joueur.__init__(self, nom, condVic)
        self.prec = ""

    def joue(self, jeu):
        cptP = cptF = 1
        if len(self.prec) > 1:
            motif = ""
            ind = 0
            i = -1
            motif = self.prec[i] + motif
            ind = self.prec[:-1].find(motif)
            # Met a jour le motif
            while ind != -1:
                curs = 0
                # Cherche toutes les occurences du motif
                while ind != -1 and curs < len(self.prec) - 1:
                    curs += ind
                    if self.prec[curs + len(motif)] == 'p':
                        cptP += 1
                    else:
                        cptF += 1
                    curs += 1
                    ind = self.prec[curs:-1].find(motif)
                i -= 1
                motif = self.prec[i] + motif
                ind = self.prec[:-1].find(motif)
        return self._choose(jeu, [cptP, cptF])

    """Mise à jour de la mémoire"""
    def clcl(self, coup, res):
        self.prec += coup
