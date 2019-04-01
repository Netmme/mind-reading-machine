# mind-reading-machine
Algorithmes pour gagner aux jeux à information complète et imparfaite tel que le pile ou face; pierre, feuille, ciseaux;...

## Versions

### Version 0

Creation du projet.
* Jeu "Presque Pile ou Face" intégré.
* Algorithme de Minaisi adapté intégré.

### Version 0.5

Ammélioration du projet pour qu'il ait une certaine consistance.
* Ajout de la MRM de Shanon.
* Ajout du choix de l'algorithme de la machine, pour jouer contre Shanon ou Minaisi.
* Lissage de l'interface, accepte le type de joueur en paramètre *(ex: ./main.py m h 8)*.
* La machine doit être le joueur 1 sinon cela ne fonctionne pas *(à corriger)*.

### Version 1.0

Projet fonctionnel, plusieurs algorithmes sont disponnibles mais qu'un seul jeu.
* Ajout de la MRM Chanone Reloaded
* Ajout des algorithmes de MRM lors du choix.
* Adaptation des joueurs à leur condition de victoire, n'importe quel joueur peut être machine ou humain.
* Correction des bugs qui empêchaient de jouer.

## Mode d'emploie

* Rendre le main exécutable (ou pas c'est comme vous voulez).
* Passer le type de joueur du joueur 1 :**h**(umain) ou **m**(achine), le type du joueur 2 et le nombre de manches en paramètre du programme. Ou pas, si des paramètres sont manquants ils seront redemandés.
* Si un ou des joueurs sont des machines, renseigner l'algo.
* Parier sur qui va gagner.

## Futurs ajouts

*[] Pierre, Feuilles, Ciseaux
*[] Nouvelle MRM
*[] Statistiques lors d'une partie
*[] Fonction aléatoire plus performante
*[] Interface graphique

## Règles des jeux

### Presque Pile ou Face

Chaque joueur doit choisir entre pile ou face. Le joueur A gagne si les deux joueurs ont fait le même choix. À l'inverse le joueur B gagne lorsque les choix sont différents.


## Références:

Apprentissage pour l'anticipation de comportements de joueurs humains dans les à information complète et imparfaite: les "Mind-Reading Machines" - Jean-Daniel Zucker, Christophe Meyer - Revue d'intelligence artificielle volume n14
