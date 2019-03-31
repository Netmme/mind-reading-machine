#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  pileOuFace.py


import random
import sys
from jeux.joueurMinaisi import JoueurMinaisi
from jeux.joueurShanon import JoueurShanon
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


def saisieLettre(msg, listeChoix):
    verif = True
    while verif:
        choix = input(msg)
        if choix[0].upper() in listeChoix:
            verif = False
        else:
            print("Erreur de saisie")
    return choix[0].upper()


# ==================
# ==================


def choixAlgo(msg, tmp):
    if tmp.upper() == 'M':
        j = saisieLettre(msg, 'MS')
        if j.upper() == 'M':
            res = JoueurMinaisi("Minaisi")
        elif j.upper() == "S":
            res = JoueurShanon("Shanon")
    else:
        res = JoueurHum1("Hum1")
        
    return res
    
    
# ==================
# ==================


if __name__ == '__main__':
        #Initialisation
    if len(sys.argv) >= 2:
        tmp1 = sys.argv[1]
        if len(sys.argv) >= 3:
            tmp2 = sys.argv[2]
            if len(sys.argv) >= 4:
                condFin = int(sys.argv[3])
            else:
                condFin = saisieNbr("Partie en combien de manches ?\n")
        else:
            tmp2 = saisieLettre("Le joueur qui gagne si le pari est different est-il humain (h) ou machine (m) ?\n", 'HM')
            condFin = saisieNbr("Partie en combien de manches ?\n")
    else:
        tmp1 = saisieLettre("Le joueur qui gagne si le pari est identique est-il humain (h) ou machine (m) ?\n", 'HM')
        tmp2 = saisieLettre("Le joueur qui gagne si le pari est different est-il humain (h) ou machine (m) ?\n", 'HM')
        condFin = saisieNbr("Partie en combien de manches ?\n")
    j1 = choixAlgo("Choisissez l'algorithme pour le joueur 1 parmi Minaisi(m) ou Shanon (s) : ", tmp1)
    j2 = choixAlgo("Choisissez l'algorithme pour le joueur 1 parmi Minaisi(m) ou Shanon (s) : ", tmp2)
    vic1 = vic2 = 0
    
        # Jeu
    for i in range(condFin):
        ch1 = j1.joue(jeux['pf'])
        ch2 = j2.joue(jeux['pf'])
        print("Augur : {}".format(ch1[0]))
        if ch2.upper() == ch1[0][0]:    # La machine devine la pensee
            print("Paris identiques, j1 gagne.")
            vic1 += 1
            res = 'd'
        else:               # La machine ne devine pas la pensee
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


