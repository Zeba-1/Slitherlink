# Slitherlink for UGE-AP2 by Zeba & Dwarzen in Python3
# Subject: https://elearning.u-pem.fr/pluginfile.php/511264/mod_resource/content/3/projet.pdf


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


def efface_TOUTsegment(etat):
    """
    Cette fonction efface tout les segments
    """


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

# fonction graphique !

def dessine_plateau(indices, marge, tailleCase):
    """
    fonction qui dessinne le plateau en fonction du tableau indices
    d'une marge et d'une de case spécifique
    Cette foncion recrer un fenetre avec une taille choisie en
    fonction du tableau indices.
    """


def dessine_segment(etat, marge, tailleCase):
    """
    finctio qui dessine tout les segments sur le plateau.
    """


# programme principal
if __name__ == '__main__':
    pass