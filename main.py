#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  pileOuFace.py


import time
import sys
import unittest

from tests.ranking.test_elo import TestElo

from utils.utils import enter_nbr
from utils.utils import select_letter_in

from players.joueur import Joueur
from players.joueurMinaisi import JoueurMinaisi
from players.joueurShanon import JoueurShanon
from players.joueurChanone2 import JoueurChanone2
from players.joueurHum1 import JoueurHum1

jeux = {"pf": ['p', 'f']}


def init_player(msg, tmp, victory_cond):
    if tmp.upper() == 'M':
        j = select_letter_in(msg, 'MSCA')
        if j.upper() == 'M':
            res = JoueurMinaisi("Minaisi", victory_cond)
        elif j.upper() == "A":
            res = Joueur("Alea", victory_cond)
        elif j.upper() == "S":
            res = JoueurShanon("Shanon", victory_cond)
        elif j.upper() == "C":
            res = JoueurChanone2("Chanone", victory_cond)
    else:
        res = JoueurHum1("Hum1", victory_cond)
    return res


def play():
    # Initialisation
    condFin = enter_nbr('Partie en combien de manches ?\n')
    tmp2 = select_letter_in('Le joueur qui gagne si le pari est different '
                        + 'est-il humain (h) ou machine (m) ?\n',
                        'HM')
    condFin = enter_nbr("Partie en combien de manches ?\n")
    tmp1 = select_letter_in('Le joueur qui gagne si le pari est identique '
                        + 'est-il humain (h) ou machine (m) ?\n', 'HM')
    tmp2 = select_letter_in('Le joueur qui gagne si le pari est different '
                        + 'est-il humain (h) ou machine (m) ?\n', 'HM')
    condFin = enter_nbr('Partie en combien de manches ?\n')
    j1 = init_player("Choisissez l'algorithme pour le joueur 1 parmi Aléatoire "
                    + '(a), Minaisi (m), Shanon (s) ou Chanone Reloaded (c): ',
                    tmp1, str.__eq__)
    j2 = init_player("Choisissez l'algorithme pour le joueur 2 parmi Aléatoire "
                     + '(a), Minaisi (m), Shanon (s) ou Chanone Reloaded (c): ',
                    tmp2, str.__ne__)
    vic1 = vic2 = 0

    # Jeu
    for i in range(condFin):
        ch1 = j1.joue(jeux['pf'])
        time.sleep(0.1)
        ch2 = j2.joue(jeux['pf'])
        time.sleep(0.1)
        print("Augur : {}".format(ch1[0]))
        print("Choix : {}".format(ch2[0]))
        if ch2[0].upper() == ch1[0].upper():
            # La machine devine la pensee
            print("Paris identiques, j1 gagne.")
            vic1 += 1
            res = 'd'
        else:
            # La machine ne devine pas la pensee
            print("Paris différents, j2 gagne.")
            vic2 += 1
            res = 'v'
        if vic1 > vic2:
            aff1 = vic1
            aff2 = vic2
            aff3 = "J1"
        elif vic1 < vic2:
            aff1 = vic2
            aff2 = vic1
            aff3 = "J2"
        else:
            aff1 = aff2 = vic1
            aff3 = "une égalité"
        print("Le score est de {} à {} pour {}.".format(aff1, aff2, aff3))
        j1.clcl(ch2, res)

    # Conclusion
    if vic1 > vic2:
        print("Le joueur 1 a gagne.")
    elif vic1 < vic2:
        print("Le joueur 2 a gagne.")
    else:
        print("Il fallait vraiment le faire.")


if __name__ == '__main__':
    # play()
    unittest.main()
