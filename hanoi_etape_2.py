from hanoi_etape_1 import *
from pile import *


class Tour(Pile):
    """On surcharge la pile pour lui ajouter un numéro (0, 1 ou 2) et une méthode hauteur"""

    def __init__(self, numero_tour):
        super().__init__()
        self.numero_tour = numero_tour

    def get_numero_tour(self):
        return self.__numero_tour

    def hauteur(self):
        return len(self)


class Etat:
    """classe contenant une liste de 3 tours contenant des entiers représentant la taille des disques"""

    def __init__(self):
        # Lors de l'initialisation penser à empiler les N tailles de disques dans la tour d'indice 0
        self.__tour1 = Pile()
        self.__tour2 = Pile()
        self.__tour3 = Pile()
        
        for n in range(N, 0, -1):
            self.__tour1.empiler(n)
    
    def get_tours(self):
        return (self.__tour1, self.__tour2, self.__tour3)  # contient la liste des 3 tours


def bouger():
    """récupère et enlève le premier mouvement dans le deque des mouvements restants
       modifie l'état actuel puis l'affiche
    """
    if len(mvt) != 0:
        d, a = mvt.popleft()
        tour = etat.get_tours()
        
        depart = tour[d]
        arrivee = tour[a]
        disque = depart.depiler()
        arrivee.empiler(disque)
        
        print("mouvement :", d, a)
        print("etat :", tour)


def test2():
    print("Test 2")
    print("etat initial : ", etat.get_tours())
    while len(mvt) != 0:
        bouger()

etat = Etat()
#test2()
