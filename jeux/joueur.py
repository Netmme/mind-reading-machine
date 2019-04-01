#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  pileOuFace.py

class Joueur():
    def __init__(self, nom, condVic):
        self.nom = nom
        if (condVic == str.__eq__):
            self.condVic = lambda x, y: x == y
        else:
            self.condVic = lambda x, y: x != y
    
    def _joue(self, jeu):
        pass
        
    def joue(self, jeu):
        pass
        
    def clcl(self, coup, res):
        pass
        

