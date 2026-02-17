class Pile:
    """Classe modélisant une Pile"""
    # Constructeur
    def __init__(self):
        self._elements = []
        
    def est_vide(self):
        return len(self._elements) == 0
    
    def sommet(self):
        return self._elements[-1]
    
    def empiler(self, e):
        self._elements.append(e)
    
    def depiler(self):
        if not(self.est_vide()):
            return self._elements.pop()
        else:
            return None
        
    def __repr__(self):
        """ Surcharge de la fonction print() """
        return str(self._elements)


        
    


    