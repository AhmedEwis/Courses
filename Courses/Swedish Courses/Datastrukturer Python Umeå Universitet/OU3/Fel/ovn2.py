# -*- coding: latin-1 -*-
import random

seed = int(input("Skriv in en randseed (vilken som helst)")) 
random.seed(seed) 

# Skapa en buffert f�r alla slumptal
mybuffer = [[10] * 100 for i in range(100)] 
    
# Fyll mitt allokerade minne med slumptal 
for i in range(100):
   for j in range(10):
      mybuffer[i][j] = random.random()
        
# Nu kan vi prova att se om vi f�r samma slumptal 
# genom att se samma randseed en g�ng till 
random.seed(seed)   
failed = 0 
tested = 0 
for i in range(100):
   for j in range(10):
      if (mybuffer[i][j] != random.random()):
         print("Olika slumptal!!! (fel?)\n")
         tested = tested + 1
         failed = 1
   
# Kolla om allt gick som det skulle
   if (failed):
      print("Det h�r blev nog fel kanske.. \n") 
   else:
      print("Kollade %d tal och de var iaf korrekta\n" % tested)  