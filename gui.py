import tkinter
import time
import threading  


from constantes import *

fenetreJeu = tkinter.Tk()
fenetreJeu.title("Puissance 4")

def hauteur_grille(r):
    """Hauteur de la grille en fonction du rayon r des trous"""
    return 2*NB_LIGNES*r + (NB_LIGNES + 1)*ESPACEMENT

grille = tkinter.Canvas(fenetreJeu, width=LARGEUR_GRILLE, height=hauteur_grille(RAYON), background='blue')

def creation_disque(x, y, r, c, tag):
    """Création d'un disque tag (trou ou jeton), de rayon r et de couleur c à la position (x,y)"""
    identifiant = grille.create_oval(x-r, y-r, x+r, y+r, fill=c, width=0, tags=tag)
    return identifiant

def creation_grille(r):
    """Création de la grille avec des trous de rayon r"""
    for ligne in range(1, NB_LIGNES + 1):
        for colonne in range(1, NB_COLONNES + 1):
            creation_disque(ESPACEMENT + r + (colonne - 1) * (ESPACEMENT + 2 * r),
                            ESPACEMENT + r + (ligne - 1) * (ESPACEMENT + 2 * r),
                            r, 'white', 'trou')

def creation_jeton(colonne, ligne, c, r):  # Dépend de la grille
    """Création d'un jeton de couleur c et de rayon r à la colonne et à la ligne indiquée"""
    identifiant = creation_disque(colonne*(ESPACEMENT+2*r)-r,
                                  (NB_LIGNES-ligne+1)*(ESPACEMENT+2*r)-r,
                                  r, c, 'jeton')
    return identifiant

def mouvement_jeton(identifiant, r):
    """Mouvement d'un jeton de rayon r"""
    grille.move(identifiant, 0, ESPACEMENT+2*r)

nb_clic = 1

def on_click(event):
    """Fonction appelée lors d'un clic sur la grille"""
    global clic_active, nb_clic
    if not clic_active:
        return  # Si le clic n'est pas actif, ne rien faire
    clic_active = False  # Désactiver le clic pendant la chute du jeton
    colonne = int((event.x - ESPACEMENT) / (2 * RAYON + ESPACEMENT)) + 1
    if nb_clic % 2 == 0:
        affiche_grille_fenetre(colonne, 0, 'red')  # Couleur du jeton
    else:
        affiche_grille_fenetre(colonne, 0, 'yellow')  # Couleur du jeton
    nb_clic += 1

def affiche_grille_fenetre(colonne, ligneSupport, couleur):
    """Affichage du coup joué (avec chute du pion)"""
    global clic_active
    ligne = NB_LIGNES
    r = RAYON
    identifiant = creation_jeton(colonne, ligne, couleur, r)
    while ligne > ligneSupport:
        if ligne < NB_LIGNES:
            mouvement_jeton(identifiant, r)
        fenetreJeu.update()
        time.sleep(TEMPS_CHUTE)
        ligne -= 1
    clic_active = True  # Réactiver le clic une fois la chute terminée

clic_active = True  # Variable pour indiquer si le clic est actif ou non

grille.bind("<Button-1>", on_click)

creation_grille(RAYON)
grille.pack()

fenetreJeu.mainloop()
