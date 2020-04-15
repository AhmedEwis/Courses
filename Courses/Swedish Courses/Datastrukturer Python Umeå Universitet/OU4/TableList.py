# -*- coding: utf-8 -*-

#Written by Lena Kallin Westin <kallin@cs.umu.se>.
#Bug fixed 2012-08-24 by Johan Eliasson
#May be used in the course Datastrukturer och Algoritmer (Python)
#at Umeå University.
#Usage exept those listed above requires permission by the author.

from DirectedList import DirectedList


# Datatypen Tabell enligt definitionen på sidan 117 i Lars-Erik Janlert,
# Torbjörn Wiberg Datatyper och algoritmer 2., [rev.] uppl.,Lund,
# Studentlitteratur, 2000, x, 387 s. ISBN 91-44-01364-7
#
# Variabler och funktioner som inleds med ett enkelt underscore "_" är privata
# för klassen och ska inte användas av de som använder denna klass.
#
# Denna klass implementerar tabell med hjälp av en riktad lista

class TableList:

    def __init__(self):

        # Syfte: Skapar en tom tabell med hjälp av en riktad lista
        # Returvärde: -
        # Kommentarer: I boken heter denna funktion Empty.


        self._table = DirectedList()
      
    def insert(self, key, obj):

        # Syfte: utökar eller omdefinierar tabellen så att nyckeln key kopplas
        #        till värdet obj
        # Returvärde: -
        # Kommentarer: Det krävs att key är en typ som kan jämföras med
        #         likhet. Om det är en egen klass måste man överladda
        #         funktionen __eq__

        if self.isempty():
            self._table.insert(self._table.first(), (key, obj))
        else:
            found = False
            pos = self._table.first()
            while (not found) and (not self._table.isEnd(pos)):
                (newKey, newObj) = self._table.inspect(pos)
                if newKey == key:
                    found = True
                    pos = self._table.remove(pos)
                    pos = self._table.insert(self._table.first(), (key, obj))
                pos = self._table.next(pos)
            if not found:
                self._table.insert(self._table.first(), (key, obj))
        
    def isempty(self):

        # Syfte: Testar om tabellen är tom
        # Returvärde: Returnerar sant om tabellen är tom, annars falsk
        # Kommentarer:

        return self._table.isempty()

    def lookup(self, key):

        # Syfte: Ser efter om tabellen innehåller nyckeln key och returnerar
        #        i så fall värdet som är kopplat till nyckeln
        # Returvärde: Returnerar en tuppel (true, obj) där obj är värdet som
        #        är kopplat till nyckeln om nyckeln finns och annars (false, None)
        # Kommentarer: Om kön är tom returneras (false, None)

        pos = self._table.first()
        while not self._table.isEnd(pos):
            (newKey, newObj) = self._table.inspect(pos)
            if newKey == key:
                return (True, newObj)
            pos = self._table.next(pos)
        return (False, None)
        
    def remove(self, key):

        # Syfte: Tar bort nyckeln key och dess sammankopplade värde.
        # Returvärde: -
        # Kommentarer: Om nyckeln inte finns så händer inget med tabellen

        if not self.isempty():
            found = False
            pos = self._table.first()
            while (not found) and (not self._table.isEnd(pos)):
                (newKey, newObj) = self._table.inspect(pos)
                if newKey == key:
                    found = True
                    pos = self._table.remove(pos)
                else:
                    pos = self._table.next(pos)   
