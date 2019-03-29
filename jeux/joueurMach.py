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
        
    def joue(self, jeu):
        return random.sample(jeu, 1)
        
    def clcl(self, coup):
        pass
