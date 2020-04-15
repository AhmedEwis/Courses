# -*- coding: latin-1 -*-
import random

dicenames = ["ettor", "tv�or", "treor", "fyror", "femmor", "sexor"] 
random.seed()
    
print("Detta program kastar t�rning tills vi f�tt tre i rad") 
count = 0 
unfinished = 1 
lastdice = 0 
throws = 0 

while (unfinished):

    # Simulera ett kast 
    throws = throws + 1
    dice = random.randint(1, 6)
    print("Kast %d gav %d prickar" % (throws, dice))

    # J�mf�r med senaste
    if (dice == lastdice):
        count = count + 1
    else: 
        count = 0 
    lastdice = dice 
    unfinished = count !=  2
    
print("Vi fick tre stycken %s efter %d kast" % (dicenames[dice-1], throws))
    
