# -*- coding: latin-1 -*-

#Written by Lena Kallin Westin <kallin@cs.umu.se>.
#May be used in the course Datastrukturer och Algoritmer (Python) at Ume� University.
#Usage exept those listed above requires permission by the author.

from ListTwoCell import ListTwoCell

class EmptyQueueError(Exception):
    pass

"""
Datatypen K� enligt definitionen p� sidan 155 i Lars-Erik Janlert,
Torbj�rn Wiberg Datatyper och algoritmer 2., [rev.] uppl.,Lund,
Studentlitteratur, 2000, x, 387 s. ISBN 91-44-01364-7

Variabler och funktioner som inleds med ett enkelt underscore "_" �r privata
f�r klassen och ska inte anv�ndas av de som anv�nder denna klass.

Denna klass implementerar k� med hj�lp av en lista (som �r implementerad med 
en 2-cell.
"""
class QueueList:

    def __init__(self):
        """
            Syfte: Skapar en tom k� med hj�lp av en lista
            Returv�rde: -
            Kommentarer: I boken heter denna funktion Empty. 
        """		
        self._list = ListTwoCell()

    def front(self):
        """
            Syfte: Ger v�rdet av det f�rsta elementet i k�n
            Returv�rde: V�rdet f�rst i k�n
            Kommentarer: Ej definierad f�r tom stack
        """	
        if self.isempty():
            raise EmptyQueueError("Error in front")  	
        return self._list.inspect(self._list.first())

    def enqueue(self, obj):
        """
            Syfte: L�gger ett element med v�rdet obj l�ngst bak i k�n
            Returv�rde: -
            Kommentarer: 
        """	
        self._list.insert(self._list.end(), obj)

    def dequeue(self):
        """
            Syfte: Tar bort f�rsta v�rdet i k�n
            Returv�rde: -
            Kommentarer: Ej definierad f�r tom k�
        """	
        if self.isempty():
            raise EmptyQueueError("Error in dequeue")  
        self._list.remove(self._list.first())

    def isempty(self):
        """
            Syfte: Testar om k�n �r tom
            Returv�rde: Sant om k�n �r tom, annars falskt
            Kommentarer: 
        """		
        return self._list.isempty()
