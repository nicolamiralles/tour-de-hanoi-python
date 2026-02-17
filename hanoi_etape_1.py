# --------------------------------------------------------------------
# Créé par : MIRALLES Nicola
# Classe : TF
# Date de création : 18/10/2024
# Version = '1.0'
# --------------------------------------------------------------------


from collections import deque

N = 5  # nombre d'étages de la tour


def hanoi(n, d, a, i):  # n est le nombre d'étages, d le numéro de la tour de départ
    # a est le numero de la tour d'arrivée et i celui de la tour intermédiaire
    if n == 1 :
        mvt.append((d, a))
    else :
        hanoi(n - 1, d, i, a)
        mvt.append((d, a))
        hanoi(n - 1, i, a, d)
        

def test1():
    print("Test 1")
    if mvt == deque(
        [
            (0, 1),
            (0, 2),
            (1, 2),
            (0, 1),
            (2, 0),
            (2, 1),
            (0, 1),
            (0, 2),
            (1, 2),
            (1, 0),
            (2, 0),
            (1, 2),
            (0, 1),
            (0, 2),
            (1, 2),
            (0, 1),
            (2, 0),
            (2, 1),
            (0, 1),
            (2, 0),
            (1, 2),
            (1, 0),
            (2, 0),
            (2, 1),
            (0, 1),
            (0, 2),
            (1, 2),
            (0, 1),
            (2, 0),
            (2, 1),
            (0, 1),
        ]
    ):
        print("Vous pouvez passer à l'étape 2")
    else:
        print("Il y a surement un problème.")
    print("\n")


# génération de la liste des mouvements
mvt = deque()  # deque des mouvements
hanoi(N, 0, 1, 2)  # cree la liste des mouvements

#test1()
