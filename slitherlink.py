# Slitherlink for UGE-AP2 by Zeba & Dwarzen in Python3
# Subject: https://elearning.u-pem.fr/pluginfile.php/511264/mod_resource/content/3/projet.pdf

import fltk as fl
import math

TAILLE_CASE = 150
TAILLE_MARGE = 50

# fonction pour gerer les segments

def ordre_segment(segment):
    """
    Cette fonction s'assure que le segment est dans le bonne ordre
    Cad que ((a,b), (c,d)) == ((c,d), (a,b))
    """


def est_trace(etat, segment):
    """
    Cette fonction regarde si un segment est trace sur le plateau
    Cad si il existe dans etat ET si etat[segment] == 1
    """


def est_interdit(etat, segment):
    """
    Cette fonction regarde si un segment est interdit sur le plateau
    Cad si il existe dans etat ET si etat[segment] == -1
    """


def est_vierge(etat, segment):
    """
    Cette fonction regarde si un segment n'est ni trace ni interdit
    Cad si il n'existe pas dans etat
    """


def trace_segment(etat, segment):
    """
    Cette fonction trace un segment sur le plateau
    Cad elle ajoute etat[segment] = 1
    """
    if segment not in etat:
        etat[segment] = 1
    else:
        efface_segment(etat, segment)


def interdi_segment(etat, segment):
    """
    Cette fonction interdit un segment sur le plateau
    Cad elle ajoute etat[segment] = -1
    """


def efface_segment(etat, segment):
    """
    Cette fonction efface un segment du plateau
    Cad elle le retire du dict etat
    """
    if segment in etat:
        del etat[segment]


def efface_TOUTsegment(etat):
    """
    Cette fonction efface tout les segments
    """


def gestion_clique(coor, marge, tailleCase, etat):
    """
    recuepre les coor d'un clique, si le joueur clique sur un segment
    alors il creer le segment (ou le retire si il est deja présent)
    """
    x, y = coor
    dx = (x - marge) / tailleCase
    dy = (y - marge) / tailleCase

    if  -0.2 < dx - round(dx) < 0.2:
        trace_segment(etat, ((round(dx), round(dy - 0.5)), (round(dx), round(dy - 0.5)+1)))
    elif -0.2 < dy - round(dy) < 0.2:
        trace_segment(etat, ((round(dx - 0.5), round(dy)), (round(dx - 0.5)+1, round(dy))))


# fonction qui gere les sommets

def recup_segment(etat, sommet, typeSeg):
    """
    focntion qui renvoie la list des segment adjacent a sommet
    don l'etat est typeSeg
    typeSeg: 1 = tarce, -1 = interdit, None = vierge
    """


# fonction qui gere les cases

def statut_case(indices, etat, case):
    """
    Indique si la case est satisfaite(bon nombre de segment autour)
    si il reste des segment a mettre ou si il y en a trop !
    """


# fonction pour la grille
def cree_grille(fichier):
    """
    transforme le contenue d'un fichier txt en liste de liste
    pour former le plateau de jeu !
    """
    grilleTxt = open(fichier, "r")
    indices = []

    i = 0
    for ligne in grilleTxt:
        indices.append([])
        for char in ligne.rstrip("\n"):
            if char == "_":
                indices[i].append(None)
            else:
                indices[i].append(char)
        i += 1

    grilleTxt.close()
    return indices

# fonction graphique !

def dessine_plateau(indices, marge, tailleCase):
    """
    fonction qui dessinne le plateau en fonction du tableau indices
    d'une marge et d'une de case spécifique
    Cette foncion recrer un fenetre avec une taille choisie en
    fonction du tableau indices.
    """
    fl.cree_fenetre(len(indices[0]) * tailleCase + marge*2,
                    len(indices) * tailleCase + marge*2)

    # boucle pour le dessin des points
    for x in range(len(indices[0])+1):
        for y in range(len(indices)+1):
            fl.cercle(marge+(x*tailleCase), marge+(y*tailleCase), 10,
                      remplissage='black')

    # boucle pour le dessin des indices
    for x, ligne in enumerate(indices):
        for y, indice in enumerate(ligne):
            if indice == None: continue
            fl.texte(marge+(tailleCase/2) + y*tailleCase,
                     marge+(tailleCase/2) + x*tailleCase,
                     indice, ancrage='center', taille=40)
            


def dessine_segment(etat, marge, tailleCase):
    """
    finctio qui dessine tout les segments sur le plateau.
    """
    fl.efface('ligne')
    for segment, typeSeg in etat.items():
        a, b = segment
        ax, ay = ((a[0] * tailleCase) + marge, (a[1] * tailleCase) + marge)
        bx, by = ((b[0] * tailleCase) + marge, (b[1] * tailleCase) + marge)
        print(a, b)
        fl.ligne(ax, ay, bx, by, tag='ligne')


# programme principal
if __name__ == '__main__':

    #Declaration des variable
    indices = cree_grille("test.txt")
    dessine_plateau(indices, TAILLE_MARGE, TAILLE_CASE)
    etat = {}

    while True:
        coorClique = fl.attend_clic_gauche()
        gestion_clique(coorClique, TAILLE_MARGE, TAILLE_CASE, etat)
        print(etat)
        dessine_segment(etat, TAILLE_MARGE, TAILLE_CASE)

    fl.attend_fermeture()