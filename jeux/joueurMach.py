#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  pileOuFace.py
        
import random
import re
import time
from jeux.joueur import Joueur

class JoueurMach(Joueur):
    def __init__(self, nom, condVic):
        Joueur.__init__(self, nom, condVic)
        
    def _joue(self, jeu):
        return random.choices(jeu)[0]
        
    def joue(self, jeu):
        res = self._joue(jeu)
        return res
        
    def clcl(self, coup, res):
        pass
