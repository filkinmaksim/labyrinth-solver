class Labyrinth:
    """Classe définissant un Labyrinthe défini par:
    - une taille
    - un début
    - une fin
    - une matrice contenant les cellules
    - une matrice contenant les murs
    - une dimension"""

    def __init__(self, dimension, size):
        self.Dimension = dimension
        self.size = size
        self.start = dimension*[0]
        self.end = size
        

    def setStart(self, start ):
        self.start = start

    def setEnd(self, end):
        self.end = end


