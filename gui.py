from constantes import NB_COLONNES, NB_LIGNES, TEMPS_CHUTE, LARGEUR_GRILLE, ESPACEMENT, RAYON
import tkinter

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

creation_grille(RAYON)
grille.pack()  # Affichage de la grille dans la fenêtre

# Lancement gui Tkinter
fenetreJeu.mainloop()

