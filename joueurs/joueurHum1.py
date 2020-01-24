#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  pileOuFace.py

from jeux.joueur import Joueur

class JoueurHum1(Joueur):
    def __init__(self, nom, condVic):
        Joueur.__init__(self, nom, condVic)
    
    def _saisieChoix(self, msg, jeu):
        choix = input(msg)
        while not (choix.upper() in [e[0].upper() for e in jeu]):
            print("Erreur saisie")
            choix = input(msg)
        
        return choix
    
    def joue(self, jeu):
        return self._saisieChoix("Pile (p) ou Face (f) ? ", jeu)
