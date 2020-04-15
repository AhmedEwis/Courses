# -*- coding: latin-1 -*-

#Written by Lena Kallin Westin <kallin@cs.umu.se>.
#May be used in the course Datastrukturer och Algoritmer (Python) at Ume� University.
#Usage exept those listed above requires permission by the author.

"""
Datatypen Bin�rt s�ktr�d n�stan enligt definitionen p� sidan 287 i Lars-Erik 
Janlert, Torbj�rn Wiberg Datatyper och algoritmer 2., [rev.] uppl.,Lund,
Studentlitteratur, 2000, x, 387 s. ISBN 91-44-01364-7 

Det som skiljer �r att insertLeft och insertRight har tagits bort ut ytan och 
satts med en funktion place som placerar in noden p� korrekt st�lle.

Variabler och funktioner som inleds med ett enkelt underscore "_" �r privata
f�r klassen och ska inte anv�ndas av de som anv�nder denna klass.

Denna klass implementerar ett Bin�rt s�ktr�d med hj�lp av ett 3-cell.
"""
from ThreeCell import ThreeCell 

class BinSearchTree3Cell: 
    
    def __init__(self, val, cmpFcn):
        """
            Syfte: Skapar en tomt bin�rt s�ktr�d
            Pararmetrar: val - rotens v�rde
                         cmpFcn - j�mf�relsefunktionen som anv�nds i tr�det
            Returv�rde: 
            Kommentarer: Ett tomt bin�rt s�ktr�d best�r av en rotnod med v�rdet
                         val(Make)
        """ 
        self._root = ThreeCell()
        self._root.setValue(val)
        self._cmpFcn = cmpFcn
      
    def place(self, val):
        """
            Syfte: S�tter in ett nytt v�rde val p� r�tt st�lle i tr�det.
            Parametrar: val - v�rdet som ska s�ttas in
            Returv�rde: Returnerar positionen f�r den nya noden.
            Kommentarer: 
        """
        placed = False
        pos = self._root
        while not placed:
            if self._cmpFcn(pos.inspectValue(), val):
                if self.hasRightChild(pos):
                    pos = self.rightChild(pos)
                else:
                    placed = True
                    newCell = ThreeCell()
                    newCell.setValue(val)
                    newCell.setParent(pos)
                    pos.setRight(newCell)   
            else:
                if self.hasLeftChild(pos):
                    pos = self.leftChild(pos)
                else:
                    placed = True
                    newCell = ThreeCell()
                    newCell.setValue(val)
                    newCell.setParent(pos)
                    pos.setLeft(newCell)                

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
    
    def _findMin(self, pos):
        """
            Syfte: Letar reda p� positionen f�r det minsta elementet i tr�det som 
                har pos som rot.
            Parametrar: pos - roten i deltr�det vi ska hitta min i.
            Returv�rde: Ger positionen till det minsta elementet
            Kommentarer:
        """        
        min = pos.inspectValue()
        minpos = pos
        while pos.inspectLeft() != None:
            pos = self.leftChild(pos)
            if self._cmpFcn(pos.inspectValue(), min):
                min = minpos.inspectValue()
                minpos = pos
        return minpos
        
    def deleteNode(self, pos):
        """
            Syfte: Tar bort noden p� angiven position
            Parametrar: pos - positionen som ska bort
            Returv�rde: Ger positionen till f�r�ldern till positionen pos
            Kommentarer: F�ruts�tts att tr�det inte �r tomt och att det finns en 
                         nod p� angiven position 
        """
        
        # Finns det b�de ett barn till v�nster och ett till h�ger?
        if pos.inspectLeft() != None and pos.inspectRight() != None:
            # V�lj det minsta enligt g�llande ordning fr�n h�ger deltr�d som 
            #  ers�ttning. 
            oldPos = pos
            minpos = self._findMin(self.rightChild(pos))
            oldPos.setValue(minpos.inspectValue())
            if minpos.inspectLeft() == None and minpos.inspectRight() == None:
                parent = minpos.inspectParent()
                if parent.inspectRight() == minpos:
                    parent.setRight(None) 
                else:
                    parent.setLeft(None)
            else:
                self.deleteNode(minpos)                
        elif pos.inspectRight() != None:
            # Flytta upp h�ger deltr�d ett sn�pp
            parent = pos.inspectParent()
            if parent == None:
                # Vi �r i roten
                self._root = pos.inspectRight()  
                pos.inspectRight().setParent(None)        
            elif parent.inspectRight() == pos:
                parent.setRight(pos.inspectRight())                
            else:    
                parent.setLeft(pos.inspectRight()) 
            pos.inspectRight().setParent(parent)
        elif pos.inspectLeft() != None:
            # Flytta upp v�nster deltr�d ett sn�pp
            parent =pos.inspectParent()
            if parent == None:
                # Vi �r i roten
                self._root = pos.inspectLeft() 
                pos.inspectLeft().setParent(None)
            elif parent.inspectRight() == pos:
                parent.setRight(pos.inspectLeft())
            else:    
                parent.setLeft(pos.inspectLeft())   
                
