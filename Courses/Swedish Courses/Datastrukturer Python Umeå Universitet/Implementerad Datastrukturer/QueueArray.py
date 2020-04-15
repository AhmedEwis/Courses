# -*- coding: latin-1 -*-

#Written by Lena Kallin Westin <kallin@cs.umu.se>.
#May be used in the course Datastrukturer och Algoritmer (Python) at Ume� University.
#Usage exept those listed above requires permission by the author.

from Array import Array

class EmptyQueueError(Exception):
    pass

class FullQueueError(Exception):
    pass

"""
Datatypen K� enligt definitionen p� sidan 155 i Lars-Erik Janlert,
Torbj�rn Wiberg Datatyper och algoritmer 2., [rev.] uppl.,Lund,
Studentlitteratur, 2000, x, 387 s. ISBN 91-44-01364-7

Variabler och funktioner som inleds med ett enkelt underscore "_" �r privata
f�r klassen och ska inte anv�ndas av de som anv�nder denna klass.

Denna klass implementerar k� med hj�lp av en array
"""
class QueueArray:

    def __init__(self):
        """
            Syfte: Skapar en tom k� med hj�lp av en Array
            Returv�rde: -
            Kommentarer: I boken heter denna funktion Empty. 

        """	        
        self._MAX = 20
        self._array = [ None for i in range(self._MAX)] 
        self._head = 0
        self._tail = self._MAX - 1
        self._count= 0
       

    def front(self):
        """
            Syfte: Ger v�rdet av det f�rsta elementet i k�n
            Returv�rde: V�rdet f�rst i k�n
            Kommentarer: Ej definierad f�r tom stack
        """	        
        if self.isempty():
            raise EmptyQueueError("Error in front")  
        return self._array[self._head]

    def enqueue(self, obj):
        """
            Syfte: L�gger ett element med v�rdet obj l�ngst bak i k�n
            Returv�rde: -
            Kommentarer: N�r k�n �r implementerad som en array kan den bli full
        """        
        if self._count == self._MAX:
            raise FullQueueError("Error in enqueue")
        self._tail = self._tail + 1
        if self._tail == self._MAX:
            self._tail = 0
        self._array[self._tail] = obj
        self._count += 1

    def dequeue(self):
        """
            Syfte: Tar bort f�rsta v�rdet i k�n
            Returv�rde: -
            Kommentarer: Ej definierad f�r tom k�
        """	        
        if self.isempty():
            raise EmptyQueueError("Error in dequeue")  
        result = self._array[self._head]
        self._array[self._head] = None
        self._head = self._head + 1
        if self._head == self._MAX:
            self._head = 0
        self._count -= 1
        return result

    def isempty(self):
        """
            Syfte: Testar om k�n �r tom
            Returv�rde: Sant om k�n �r tom, annars falskt
            Kommentarer: 
        """        
        return self._count == 0

