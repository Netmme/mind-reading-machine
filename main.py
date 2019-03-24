#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  pileOuFace.py


import random
import sys
from jeux.joueurMinaisi import JoueurMinaisi
from jeux.joueurHum1 import JoueurHum1

jeux = {"pf": ["Pile", "Face"]}

# ==================
# ==================

def saisieNbr(msg, min = 0, max = 300000):
    verif = True
    while verif:
        nbr = input(msg)
        if nbr.isdigit():
            res = int(nbr)
            if min < res <max:
                verif = False
            else:
                print("Erreur, nombre impossible.")
        else:
            print("Erreur de saisie")
    
    return res

# ==================
# ==================

def saisieJoueur(msg):
    joueur = input(msg)
    if joueur[0].upper() == "H":
        res = JoueurHum1
    else:
        res = JoueurMach
    return res

# ==================
# ==================

if __name__ == '__main__':
        #Initialisation
    # ~ j = saisieJoueur("Le joueur qui fait deviner est-il humain (h) ou machine (m) ?\n")
    j1 = JoueurMinaisi("Alice")
    # ~ j = saisieJoueur("Le joueur qui devine est-il humain (h) ou machine (m) ?\n")
    j2 = JoueurHum1("Bob")
    # ~ condFin = saisieNbr("Partie en combien de manches ?\n")
    condFin = int(sys.argv[1])
    nbrGa = nbrPe = 0
    
        # Jeu
    for i in range(condFin):
        ch1 = j1.minasiJoue(jeux['pf'])
        ch2 = j2.joue(jeux['pf'])
        print("Augur : {}".format(ch1[0]))
        if ch2.upper() == ch1[0][0]:
            print("Perdu :/")
            nbrPe += 1
        else:
            print("Gagné :D")
            nbrGa += 1
        print("Tu en es à : {} manches gagnées, {} manches perdues".format(nbrGa, nbrPe))
        j1.minasiClcl(ch2)
    
        # Conclusion
    if nbrGa > nbrPe:
        print("T'es un boss!")
    elif nbrGa < nbrPe:
        print("Ca arrive...")
    else:
        print("Il fallait vraiment le faire.")


