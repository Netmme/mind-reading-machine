#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  pileOuFace.py
        
import random
import re
import time
from jeux.joueur import Joueur

class JoueurMach(Joueur):
    def __init__(self, nom):
        Joueur.__init__(self, nom)
        self.prec = ""
        
    def joue(self, jeu):
        return random.sample(jeu, 1)
        
    def minasiJoue(self, jeu):
        cptP = cptF = 1
        if len(self.prec) > 1:
            motif = ""
            ind = 0 
            i = -1
            motif = self.prec[i] + motif
            ind = self.prec[:-1].find(motif)
            while ind != -1:
                curs = 0
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

        return random.choices(jeu, [cptP, cptF])

        
    def minasiClcl(self, coup):
        self.prec += coup
