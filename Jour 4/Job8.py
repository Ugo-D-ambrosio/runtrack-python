def lists():
    compteur=0
    L = [8,24,27,48,2,16,9,7,84,91]
    for element in L:
        if element%2 ==0:
            compteur+=1
    print(compteur)
    
lists()