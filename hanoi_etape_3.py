from tkinter import *
from hanoi_etape_2 import *

LARGEUR = 900  # largeur fenêtre
HAUTEUR = 300  # hauteur fenêtre
# Les disques ont des largeurs de 1 à N
HAUTEUR_DISQUE = 40

base = LARGEUR / 4  # largeur de la base de la tour initiale
unite = base / N  # largeur d'une unité la base fait donc N unités de large
intervalle = base / 4  # intervalle à laisser entre les tours entre elles
# et entre le cadre et les tours de côté.


class Disque:
    """Disque graphique"""

    def __init__(self, taille, num_tour, etage, espace = 5):
        self.__largeur = taille * unite
        self.__hauteur = HAUTEUR_DISQUE
        self.__x = (
            intervalle
            + base / 2
            - self.__largeur / 2
            + (num_tour * (intervalle + base))
        )
        self.__y = HAUTEUR - etage * (HAUTEUR_DISQUE + espace )
        self.__oval = cnv.create_oval(
            self.__x,
            self.__y,
            self.__x + self.__largeur,
            self.__y + self.__hauteur,
            fill="purple"
        )


class Etat_graphique(Etat):
    """ On surchage la classe Etat pour lui ajouter une methode afficher() qui effectue un affichage graphique de l'état
        classe contenant une liste de 3 tours contenant des disques"""

    def effacer(self):
        cnv.delete("all")

    def afficher(self):
        self.effacer()
        self.__graphique = [Tour(0), Tour(1), Tour(2)]
        for i in range(3):
            pile_tmp = Pile()
            while not (self.get_tours()[i].est_vide()):
                taille = self.get_tours()[i].depiler()
                pile_tmp.empiler(taille)

            etage = 0
            while not (pile_tmp.est_vide()):
                taille = pile_tmp.depiler()
                etage += 1
                self.__graphique[i].empiler(Disque(taille, i, etage))
                self.get_tours()[i].empiler(taille)


def bouger():
    """récupère et enlève le premier mouvement dans le deque des mouvements restants
       modifie l'état actuel puis l'affiche
       Pour cette étape, on réécris la fonction bouger() pour ajouter les instructions Tkinter
    """
    if len(mvt) != 0:
        d, a = mvt.popleft()
        tour = etat.get_tours()
        
        depart = tour[d]
        arrivee = tour[a]
        disque = depart.depiler()
        arrivee.empiler(disque) # recopier le code de l'étape 2

        etat.afficher()
        cnv.after(500, bouger)  # La fonction bouger se rappelle elle même après 500 ms


# initialisation graphique
root = Tk()
cnv = Canvas(root, width=LARGEUR, height=HAUTEUR, bg="ivory")
cnv.pack()

etat = Etat_graphique()
etat.afficher()

def test3():
    bouger()
    root.mainloop()

test3()