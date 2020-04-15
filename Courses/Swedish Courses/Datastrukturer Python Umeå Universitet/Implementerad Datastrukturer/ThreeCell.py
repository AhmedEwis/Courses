# -*- coding: latin-1 -*-
class ThreeCell:
    """
        Datatypen 3-Cell enligt definitionen p� sidan 77 i Lars-Erik Janlert,
        Torbj�rn Wiberg Datatyper och algoritmer 2., [rev.] uppl.,Lund,
        Studentlitteratur, 2000, x, 387 s. ISBN 91-44-01364-7
    
        Implementationen avviker s� tillvida att link1 kallas parent, link2 
        kallas left och link3 kallas right eftersom cellen fr�mst ska anv�ndas 
        i tr�d och det underl�ttar l�sandet av koden.
    
        Variabler och funktioner som inleds med ett enkelt underscore "_" �r 
        privata f�r klassen och ska inte anv�ndas av de som anv�nder denna klass.
    
    """
    def __init__(self):
        """
            Syfte: Skapar en ny cell utan definierat v�rde eller l�nkar
            Parametrar: -
            Returv�rde: -
            Kommentarer: I definitionen heter denna funktion Create
        """
        self._data = None
        self._parent = None
        self._left = None
        self._right = None
    
    def setValue(self,data):
        """
            Syfte: S�tter cellens v�rde till data
            Parametrar:
            Returv�rde:
            Kommentarer:
        """
        self._data = data

    def setParent(self,link):
        """
            Syfte: S�tter cellens parent-l�nk till link
            Parametrar:
            Returv�rde:
            Kommentarer:
        """
        self._parent =link

    def setLeft(self,link):
        """
            Syfte: S�tter cellens left-l�nk till link
            Parametrar:
            Returv�rde:
            Kommentarer:
        """
        self._left =link

    def setRight(self,link):
        """
            Syfte: S�tter cellens right-l�nk till link
            Parametrar:
            Returv�rde:
            Kommentarer:
        """
        self._right =link

    def inspectValue(self):
        """
            Syfte: Returnerar cellens v�rde 
            Parametrar:
            Returv�rde:
            Kommentarer:
        """
        return self._data

    def inspectParent(self):
        """
            Syfte: Returnerar cellens parent-l�nk 
            Parametrar:
            Returv�rde:
            Kommentarer:
        """
        return self._parent

    def inspectLeft(self):
        """
            Syfte: Returnerar cellens left-l�nk
            Parametrar:
            Returv�rde:
            Kommentarer:
        """
        return self._left
    
    def inspectRight(self):
        """
            Syfte: Returnerar cellens right-l�nk
            Parametrar:
            Returv�rde:
            Kommentarer:
        """
        return self._right    