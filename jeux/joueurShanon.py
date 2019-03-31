#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  pileOuFace.py
        
import random
import re
import time
from jeux.joueur import Joueur

# d: defaite	v: victoire
# c: change	m: maintient
# n: NULL
#
# Contenu de la mémoire :
# 
#	c/m revu num
# d-c-d c   V	 0
# | |-v c	 1
# |-m-d m	 2
# | |-v c	 3
# v-c-d c   V	 4
# | |-v m	 5
# |-m-d m	 6
#   |-v c   V	 7
#

class JoueurShanon(Joueur):
    def __init__(self, nom):
        Joueur.__init__(self, nom)
        self.prec = {'dcd':('n', False), 'dcv':('n', False), 'dmd':('n', False),
                     'dmv':('n', False), 'vcd':('n', False), 'vcv':('n', False),
                     'vmd':('n', False), 'vmv':('n', False)}
        self.derCoup = self.serie = ''
    
    def _joue(self, jeu, nbr):
        return random.sample(jeu, 1)

    def joue(self, jeu):
        if self.serie in self.prec and self.prec[self.serie][1]: # Verifie si le comportement actuel est enregistre
            if self.prec[self.serie][0] != 'c':
                if self.derCoup == 'p':
                    res = 'f'
                else:
                    res = 'p'
            else:
                res = self.derCoup
        else:               # Si le comportement n'est pas connu jouer au hasard
            res = self._joue(jeu, 1)
        
        return res

        
    def clcl(self, coup, res):
        if self.derCoup != '':
                # Mettre a jour la memoire du comportement
            if self.serie in self.prec:
                if (coup == self.derCoup and self.prec[self.serie][0] == 'c') and \
                   (coup != self.derCoup and self.prec[self.serie][0] == 'm'):  # Si le comportement a deja ete rencontre
                    self.prec[self.serie][1] == True
                elif self.prec[self.serie][0] == 'n': # Si le comportement n'a jamais ete rencontre
                    if coup == self.derCoup:
                        self.prec[self.serie][0] = 'c'
                    else:
                        self.prec[self.serie][0] = 'm'
                else:   # Si un autre comportement avait ete enregistre
                    self.prec[self.serie][0] = 'n'
                    self.prec[self.serie][1] = False
                    
                # Mettre à jour la serie de coups
            self.serie = self.serie[len(self.serie)-1:]   # a la deuxieme execution ca fait [-1:] d'une chaine vide, peu rigoureux
            self.serie += res
            if coup != self.derCoup:
                self.serie += 'c'
            else:
                self.serie += 'm'
        self.derCoup = coup
        print("Memoire :", self.serie)
