# -*- coding: latin-1 -*-

#Written by Lena Kallin Westin <kallin@cs.umu.se>.
#May be used in the course Datastrukturer och Algoritmer (Python) at Ume� University.
#Usage exept those listed above requires permission by the author.

"""
Datatypen HashTabell 

Variabler och funktioner som inleds med ett enkelt underscore "_" �r privata
f�r klassen och ska inte anv�ndas av de som anv�nder denna klass.

Denna klass implementerar en hashtabell med hj�lp av den inbyggda listan
"""
class HashTable: 
    
    def _internalHash(self,key):
        """
            Intern function, ej f�r externt bruk
        """
        return self._hashFcn(key) % self._size
    

    def _rehash(self):
        """
            Intern function, ej f�r externt bruk
        """
        temp = self._data
        oldsize = self._size
        self._data = []
        self._size = oldsize*2
        self._numElem = 0
        self._numInsertions=0
        for i in range(oldsize):
            if(temp[i]):
                hashtable_insert(self_table, temp[i])
  
    def __init__(self, size, hashFcn, cmpFcn):
        """
            Syfte: Skapar en tom hashtabell med hj�lp av den inbyggda listan
            Pararmetrar: 
                size -    startstorlek p� tabellen och ska vara ca 2*uppskattat 
                          antal element som ska stoppas in. Storleken �kar 
                          automatiskt men den operationen �r dyr.
                hashFcn - en funktion som ber�knar ett hashv�rde fr�n en 
                          nyckel. Returv�rdet fr�n funktionen ska vara ett 
                          positivt heltal. V�rdet kommer internt att omvandlas 
                          till omr�det [0, size]
                cmpFcn -  en funktion som j�mf�r tv� nycklar. Ska returnera 
                          False f�r nycklar som inte �r lika och annars True
            Returv�rde: 
            Kommentarer: 
        """ 
        self._cmpFcn = cmpFcn
        self._hashFcn = hashFcn
        self._size = size
        self._data = [None]*self._size
        self._numelem = 0
        self._numinsertions = 0
      
    def insert(self, key, obj):
        """
            Syfte: ut�kar eller omdefinierar tabellen s� att nyckeln key kopplas 
                   till v�rdet obj
            Returv�rde: -
            Kommentarer: -  
        """
        if(self._numinsertions >= self._size/2):
            self._rehash()
        index = self._internalHash(key)
        while (self._data[index] != None) and (self._data[index] != (None, None) and not self._cmpFcn(self._data[index][0],key)):
            index = (index + 1) % self._size
        if (self._data[index] == None):
            self._numelem = self._numelem + 1
            self._numinsertions = self._numinsertions + 1
        
        self._data[index] = (key, obj)
        
    def isempty(self):
        """
            Syfte: Testar om hashtabellen �r tom
            Returv�rde: Returnerar sant om tabellen �r tom, annars falsk
            Kommentarer: 
        """        
        return self._numelem == 0
        
    def lookup(self, key):
        """
            Syfte: Ser efter om hashtabellen inneh�ller nyckeln key och returnerar
                   i s� fall v�rdet som �r kopplat till nyckeln
            Parametrar: key - nyckeln
            Returv�rde: Returnerar en tuppel (True, obj) d�r obj �r v�rdet som 
                   �r kopplat till nyckeln om nyckeln finns och annars (false, None)
            Kommentarer: Om k�n �r tom returneras (False, None)
        """
        index = self._internalHash(key)
        while (self._data[index] != None) and (self._data[index] != (None, None) and not self._cmpFcn(self._data[index][0],key)):
               index = (index + 1) % self._size
        if self._data[index] != None:
            return (True, self._data[index][1])
        return (False, None)
        
    def remove(self, key):
        """
            Syfte: Tar bort nyckeln key och dess sammankopplade v�rde.
            Returv�rde: -
            Kommentarer: Om nyckeln inte finns s� h�nder inget med tabellen            
        """        
        index =self._internalHash(key)
        while (self._data[index] != None) and (self._data[index] != (None, None) and not self._cmpFcn(self._data[index][0],key)):
            index = (index + 1) % self._size
        if(self._data[index] != None):
            self._data[index] = (None, None)
            self._numelem = self._numelem - 1
    
  
