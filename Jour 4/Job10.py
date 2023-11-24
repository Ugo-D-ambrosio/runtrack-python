def lists():
    produit=1
    L = [8,24,27,48,2,16,9,102,7,84,91]
    for element in L:
        if element >25 and element <90 :
            produit = produit * element
        
    print(produit)
            
lists()