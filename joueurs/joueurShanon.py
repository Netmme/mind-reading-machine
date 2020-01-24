#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  pileOuFace.py
# d: defaite    v: victoire
# c: change     m: maintient
# '': NULL
#
# Contenu de la mémoire :
# dico : cle + [valeur, boolean : choix validé ou non]
#
#   c/m memoir  num
# d-c-d c   V   0
# | |-v ''      1
# |-m-d ''      2
# | |-v c       3
# v-c-d c   V   4
# | |-v ''      5
# |-m-d m	    6
#   |-v c   V   7


from joueurs.joueur import Joueur


class JoueurShanon(Joueur):
    def __init__(self, nom, condVic):
        Joueur.__init__(self, nom, condVic)
        self.tactic = {'dcd': ['', False], 'dcv': ['', False],
                       'dmd': ['', False], 'dmv': ['', False],
                       'vcd': ['', False], 'vcv': ['', False],
                       'vmd': ['', False], 'vmv': ['', False]}
        self.derCoup = self.serie = ''

    def _tac_to_choice(self, jeu, tac):
        if tac == 'c':
            choice = self._swap(self.derCoup)
        else:
            choice = self.derCoup
        return choice

    def joue(self, jeu):
        # Verifie si le comportement actuel est enregistre
        if self.serie in self.tactic and self.tactic[self.serie][1]:
            tac = self.tactic[self.serie][0]
            choice = self._tac_to_choice(jeu, tac)
            res = self._toVictory(choice)
        # Si le comportement n'est pas connu jouer au hasard
        else:
            res = self._joue(jeu)
        return res

    def clcl(self, coup, res):
        if self.derCoup != '':
            # Mettre a jour la memoire du comportement
            if self.serie in self.tactic:
                # Si le comportement a deja ete rencontre
                if (coup == self.derCoup and self.tactic[self.serie][0] == 'm') or \
                   (coup != self.derCoup and self.tactic[self.serie][0] == 'c'):
                    self.tactic[self.serie][1] = True
                # Si le comportement n'a jamais ete rencontre
                elif not self.tactic[self.serie][0]:
                    if coup == self.derCoup:
                        self.tactic[self.serie][0] = 'm'
                    else:
                        self.tactic[self.serie][0] = 'c'
                # Si un autre comportement avait ete enregistre
                else:
                    self.tactic[self.serie][0] = ''
                    self.tactic[self.serie][1] = False
            # Mettre à jour la serie de coups
            self.serie = self.serie[len(self.serie)-1:]     # a la deuxieme execution ca fait [-1:] d'une chaine vide, peu rigoureux
            if coup != self.derCoup:
                self.serie += 'c'
            else:
                self.serie += 'm'
            self.serie += res
        self.derCoup = coup
