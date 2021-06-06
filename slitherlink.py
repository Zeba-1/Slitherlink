# Slitherlink for UGE-AP2 by Zeba & Dwarzen in Python3
# Subject: https://elearning.u-pem.fr/pluginfile.php/511264/mod_resource/content/3/projet.pdf

import fltk as fl
import math

TAILLE_CASE = 150
TAILLE_MARGE = 50

# fonction pour gerer les segments

def trace_segment(etat, segment):
    """
    Cette fonction trace un segment sur le plateau
    Cad elle ajoute etat[segment] = 1
    """
    if segment not in etat:
        etat[segment] = 1
    elif etat[segment] == 1:
        efface_segment(etat, segment)


def interdi_segment(etat, segment):
    """
    Cette fonction interdit un segment sur le plateau
    Cad elle ajoute etat[segment] = -1
    """
    if segment not in etat:
        etat[segment] = -1
    else:
        efface_segment(etat, segment)


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
    etat = {}


def gestion_clique(ev, tev, marge, tailleCase, etat, dim):
    """
    recuepre les coor d'un clique, si le joueur clique sur un segment
    alors il creer le segment (ou le retire si il est deja présent)
    """
    x, y = (fl.abscisse(ev), fl.ordonnee(ev))
    # On verifie qu'on ne sort pas du plateau
    if marge < x < marge + dim[0] * tailleCase and marge < y < marge + dim[1] * tailleCase:
        dx = (x - marge) / tailleCase
        dy = (y - marge) / tailleCase

        if tev == 'ClicGauche':  # trace un segment
            if  -0.2 < dx - round(dx) < 0.2:
                trace_segment(etat, ((round(dx), round(dy - 0.5)), (round(dx), round(dy - 0.5)+1)))
            elif -0.2 < dy - round(dy) < 0.2:
                trace_segment(etat, ((round(dx - 0.5), round(dy)), (round(dx - 0.5)+1, round(dy))))
        elif tev == 'ClicDroit':  # interdit un segment
            if  -0.2 < dx - round(dx) < 0.2:
                interdi_segment(etat, ((round(dx), round(dy - 0.5)), (round(dx), round(dy - 0.5)+1)))
            elif -0.2 < dy - round(dy) < 0.2:
                interdi_segment(etat, ((round(dx - 0.5), round(dy)), (round(dx - 0.5)+1, round(dy))))


def check_boucle(etat):
    """
    Check si la figure dessinner par les points, fait une boucle ou non
    """
    if len(etat) < 1:
        return False

    checkedSeg = list(etat.keys())[0] # Premier point de notre boucle
    premier = checkedSeg[0] # Segment sur lequel on est
    checkedPoint = checkedSeg[1] # point qu'on regarde

    if len(recup_segment(etat, premier, 1)) != 2:
        return False

    while checkedPoint != premier: # Tant qu'on as pas fait une boucle
        lstSeg = recup_segment(etat, checkedPoint, 1)
        if len(lstSeg) != 2:
            return False

        lstSeg.remove(checkedSeg) # On retire le segment que l'on regardais
        checkedSeg = lstSeg[0] # On regarde le nouveau segment
        
        # On s'assure de ne pas reagarder le meme point
        if checkedSeg[0] == checkedPoint:
            checkedPoint = checkedSeg[1]
        else:
            checkedPoint = checkedSeg[0]

    return True


# fonction qui gere les sommets

def recup_segment(etat, sommet, typeSeg):
    """
    focntion qui renvoie la list des segment adjacent a sommet
    don l'etat est typeSeg
    typeSeg: 1 = tarce, -1 = interdit, None = vierge
    """
    lstSeg = []
    for segement, Type in etat.items():
        if sommet in segement and Type == typeSeg:
            lstSeg.append(segement)
    return lstSeg


# fonction qui gere les cases

def statut_case(indices, etat, case):
    """
    Indique si la case est satisfaite(bon nombre de segment autour)
    si il reste des segment a mettre ou si il y en a trop !
    """
    y, x = case
    nb = indices[y][x]
    nbSeg = 0

    # On check tout les segment autour de notre case
    try: 
        if etat[((x, y), (x+1, y))] == 1: nbSeg += 1
    except KeyError: pass
    try: 
        if etat[((x, y), (x, y+1))] == 1: nbSeg += 1
    except KeyError: pass
    try: 
        if etat[((x+1, y), (x+1, y+1))] == 1: nbSeg += 1
    except KeyError: pass
    try: 
        if etat[((x, y+1), (x+1, y+1))] == 1: nbSeg += 1
    except KeyError: pass

    if nbSeg == nb:
        return True
    elif nbSeg > nb:
        return False
    elif nbSeg < nb:
        return None


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
                indices[i].append(int(char))
        i += 1

    grilleTxt.close()
    return indices


# fonction graphique !

def dessine_plateau(indices, etat, marge, tailleCase):
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

    dessine_indices(indices, etat, marge, tailleCase) # On ajoute les indices
    return (len(indices[0]), len(indices))

def dessine_indices(indices, etat, marge, tailleCase):
    """
    Mets les indices données au centre des cases
    """
    fl.efface("indice")
    for x, ligne in enumerate(indices):
        for y, indice in enumerate(ligne):
            if indice == None: continue # Si il n'y a pas d'indice on passe
            # On regarde si la case est completer ou non
            statut = statut_case(indices, etat, (x, y))
            # choix de la couleur de l'indice
            color = "black"
            if statut == True: color = "green"
            elif statut == False: color = "red"
            fl.texte(marge+(tailleCase/2) + y*tailleCase,
                     marge+(tailleCase/2) + x*tailleCase,
                     str(indice), ancrage='center', taille=40,
                     tag="indice", couleur=color)

def dessine_segment(etat, marge, tailleCase):
    """
    finctio qui dessine tout les segments sur le plateau.
    """
    fl.efface('ligne')
    for segment, typeSeg in etat.items():
        a, b = segment
        ax, ay = ((a[0] * tailleCase) + marge, (a[1] * tailleCase) + marge)
        bx, by = ((b[0] * tailleCase) + marge, (b[1] * tailleCase) + marge)
        if typeSeg == 1:
            fl.ligne(ax, ay, bx, by, tag='ligne', epaisseur=10)
        elif typeSeg == -1:
            fl.texte((ax + bx)/2, (ay + by)/2, 'X', 'red', 'center',
                     tag='ligne')


# Gestion des commande

def commade(touche):
    if touche == 'q':
        fl.ferme_fenetre()

# VICTOIRE

def deter_VICTOIRE(etat, indices, dim):
    """
    Regarde si toute les conditions de victroire sont remplie
    """
    for x, ligne in enumerate(indices):
        for y, indice in enumerate(ligne):
            if indice == None: continue # Si y'a pas d'indice
            if statut_case(indices, etat, (x, y)) != True:
                return False

    if check_boucle(etat) != True:
        return False

    return True

def ecran_fin():
    fl.ferme_fenetre()
    fl.cree_fenetre(400, 200)
    fl.texte(200, 90, "Puzzle résolue !", ancrage='center')
    fl.texte(200, 110, "vous pouver fermez la fenetre", ancrage='center',
             taille=12)
    fl.attend_fermeture()

# programme principal
if __name__ == '__main__':

    # Menue

    # Declaration des variable
    indices = cree_grille("test.txt")
    etat = {}
    dim = dessine_plateau(indices, etat, TAILLE_MARGE, TAILLE_CASE)

    # Boucle de jeux
    jeu = True
    while jeu:
        ev = fl.attend_ev()
        tev = fl.type_ev(ev)
        if tev == 'ClicDroit' or tev == 'ClicGauche':
            gestion_clique(ev, tev, TAILLE_MARGE, TAILLE_CASE, etat, dim)
        else:
            commade(fl.touche(ev))
        dessine_segment(etat, TAILLE_MARGE, TAILLE_CASE)
        dessine_indices(indices, etat, TAILLE_MARGE, TAILLE_CASE)

        if deter_VICTOIRE(etat, indices, dim) == True:
            ecran_fin()
            jeu = False