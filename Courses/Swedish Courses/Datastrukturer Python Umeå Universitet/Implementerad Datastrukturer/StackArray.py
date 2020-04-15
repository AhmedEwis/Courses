# -*- coding: latin-1 -*-

#Written by Lena Kallin Westin <kallin@cs.umu.se>.
#May be used in the course Datastrukturer och Algoritmer (Python) at Ume� University.
#Usage exept those listed above requires permission by the author.

class EmptyStackError(Exception):
    pass
class FullStackError(Exception):
    pass
"""
Datatypen Stack enligt definitionen p� sidan 134 i Lars-Erik Janlert,
Torbj�rn Wiberg Datatyper och algoritmer 2., [rev.] uppl.,Lund,
Studentlitteratur, 2000, x, 387 s. ISBN 91-44-01364-7

Variabler och funktioner som inleds med ett enkelt underscore "_" �r privata
f�r klassen och ska inte anv�ndas av de som anv�nder denna klass.

Denna klass implementerar stacken med hj�lp av en Array
"""
class StackArray:
    def __init__(self, size = 100):
        """
            Syfte: Skapar en tom stack med hj�lp av en Array
            Returv�rde: -
            Kommentarer: I boken heter denna funktion Empty. 
        """	          
        self._array = [None for i in range(size)]
        self._top = -1 #index för översta värdet
        self._size = size #Maxsstorleken

    def top(self):
        """
            Syfte: Ger v�rdet av det �versta elementet p� stacken
            Returv�rde: V�rdet �verst p� stacken
            Kommentarer: Ej definierad f�r tom stack
        """     
        if self.isempty():
            raise EmptyStackError("Error in top")
        return self._array[self._top]

    def push(self, obj):
        """
            Syfte: L�gger ett element med v�rdet v �verst p� stacken
            Returv�rde: -
            Kommentarer: In en arrayimplementation av stacken kan den bli full!            
        """     
        if self._top == self._size-1:
            raise FullStackError("Error in push")        
        self._top = self._top + 1
        self._array[self._top] = obj

    
    def pop(self):
        """
            Syfte: Tar bort �versta v�rdet fr�n stacken.
            Returv�rde: -
            Kommentarer: Ej definierad f�r tom stack
        """	    
        if self._top == -1:
            raise EmptyStackError("Error in pop")
        self._array[self._top] = None #Visar att värdet kan tas bort
        self._top = self._top - 1 #... och minska värdet på top med 1

    def isempty(self):
        """
            Syfte: Testar om stacken �r tom
            Returv�rde: Sant om stacken �r tom, annars falskt
            Kommentarer: 
        """         
        return self._top == -1 
