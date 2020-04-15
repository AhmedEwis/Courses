# -*- coding: latin-1 -*-

#Written by Lena Kallin Westin <kallin@cs.umu.se>.
#May be used in the course Datastrukturer och Algoritmer (Python) at Ume� University.
#Usage exept those listed above requires permission by the author.

"""
Datatypen Bin�rt tr�d enligt definitionen p� sidan 225 i Lars-Erik Janlert,
Torbj�rn Wiberg Datatyper och algoritmer 2., [rev.] uppl.,Lund,
Studentlitteratur, 2000, x, 387 s. ISBN 91-44-01364-7 

Variabler och funktioner som inleds med ett enkelt underscore "_" �r privata
f�r klassen och ska inte anv�ndas av de som anv�nder denna klass.

Denna klass implementerar ett Bin�rt tr�d med hj�lp av ett 3-cell.
"""
from ThreeCell import ThreeCell 

class BinTree3Cell: 
    
    def __init__(self):
        """
            Syfte: Skapar en tomt bin�rt tr�d
            Pararmetrar: 
            Returv�rde: 
            Kommentarer: Ett tomt bin�rt tr�d best�r av en tom rotnod (Create)
        """ 
        self._root = ThreeCell()
      
    def insertLeft(self, pos):
        """
            Syfte: S�tter in en ny nod som v�nster barn till noden i position pos.
            Parametrar: pos - positionen som ska f� ett v�nsterbarn
            Returv�rde: Returnerar positionen f�r den nya noden.
            Kommentarer: Det f�ruts�tts att det inte finns ett barn d�r redan.
        """
        node = ThreeCell()
        pos.setLeft(node)    
        node.setParent(pos)
        return node
    
    def insertRight(self, pos):
        """
            Syfte: S�tter in en ny nod som h�ger barn till noden i position pos.
            Parametrar: pos - positionen som ska f� ett h�gerbarn
            Returv�rde: Returnerar positionen f�r den nya noden.
            Kommentarer: Det f�ruts�tts att det inte finns ett barn d�r redan.
        """
        node = ThreeCell()
        pos.setRight(node)        
        node.setParent(pos)
        return node       
    
    def setLabel(self, val, pos):
        """
            Syfte: �ndrar v�rdet p� noden p� position pos till val.
            Parametrar: pos - positionen som ska f� ett v�rde
                        val - v�rdet som ska s�ttas in
            Returv�rde: Returnerar positionen f�r den nya noden.
            Kommentarer: 
        """     
        pos.setValue(val)

    def isempty(self):
        """
            Syfte: Testar om det bin�ra tr�det �r tomt
            Returv�rde: Returnerar sant om tr�det �r tomt, annars falskt
            Kommentarer: Ett tomt tr�d best�r av en tom rotnod
        """        
        return self._root.inspectValue == None and self._root.inspectRight == None and self._root.inspectLeft == None and self._root.inspectParent == None
                
    def hasLeftChild(self, pos):
        """
            Syfte: Kontrollerar om det finns ett barn till v�nster om positionen pos
            Parametrar: pos - positionen som kontrolleras
            Returv�rde: True och det finns ett barn till v�nster, annars false
            Kommentarer: 
        """
        return pos.inspectLeft() != None
    
    def hasRightChild(self, pos):
        """
            Syfte: Kontrollerar om det finns ett barn till h�ger om positionen pos
            Parametrar: pos - positionen som kontrolleras
            Returv�rde: True och det finns ett barn till h�ger, annars false
            Kommentarer: 
        """    
        return pos.inspectRight() != None
        
    def hasLabel(self, pos):
        """
            Syfte: Kontrollerar om det finns ett v�rde i noden p� positionen pos
            Parametrar: pos - positionen som kontrolleras
            Returv�rde: True och det finns ett v�rde, annars false
            Kommentarer: 
        """    
        return pos.inspectValue() != None

    def inspectLabel(self, pos):
        """
            Syfte: Returnerar v�rdet i noden p� positionen pos
            Parametrar: pos - positionen som kontrolleras
            Returv�rde: V�rdet p� positionen pos
            Kommentarer: Odefinierat vad som h�nder om det inte finns ett v�rde 
                         p� angiven position
        """    
        return pos.inspectValue()

    def root(self):
        """
            Syfte: Returnerar positionen f�r roten
            Parametrar: 
            Returv�rde: Positionen f�r roten
            Kommentarer: 
        """ 
        return self._root

    def leftChild(self, pos):
        """
            Syfte: Ger positionen till barnet till v�nster om positionen pos
            Parametrar: pos - positionen som kontrolleras
            Returv�rde: Ger positionen till barnet till v�nster om positionen pos
            Kommentarer: Odefinierat vad som h�nder om det inte finns ett barn till v�nster
        """
        return pos.inspectLeft()
    
    def rightChild(self, pos):
        """
            Syfte: Ger positionen till barnet till h�ger om positionen pos
            Parametrar: pos - positionen som kontrolleras
            Returv�rde: Ger positionen till barnet till h�ger om positionen pos
            Kommentarer: Odefinierat vad som h�nder om det inte finns ett barn till h�ger
        """
        return pos.inspectRight()
        
    def parent(self, pos):
        """
            Syfte: Ger positionen till f�r�lderna till positionen pos
            Parametrar: pos - positionen som kontrolleras
            Returv�rde: Ger positionen till f�r�ldern till positionen pos
            Kommentarer: Odefinierat om angiven pos �r rot
        """
        return pos.inspectParent()
        
    def deleteNode(self, pos):
        """
            Syfte: Tar bort noden p� angiven position
            Parametrar: pos - positionen som ska bort
            Returv�rde: Ger positionen till f�r�ldern till positionen pos
            Kommentarer: F�ruts�tts att tr�det inte �r tomt, att det finns en 
                         nod p� angiven position och att den noden �r ett l�v.
                         Annars raderas alla noder under pos ocks�...
        """
        
        parent =self.parent(pos)
        if parent.inspectRight() == pos:
            parent.setRight(None)
        else:    
            parent.setLeft(None)
        if pos.inspectLeft() != None:
            self.deleteNode(pos.inspectLeft())
        if pos.inspectRight() != None:
            self.deleteNode(pos.inspectRight())
        
