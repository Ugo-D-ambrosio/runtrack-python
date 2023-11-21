
def chaine():
    resultat = ""
    save=0
    chaines= "abcdefghijklmnopqrstuvwxyz"
    for lignes in range(1,30):
        for index in range(lignes):
            resultat+=chaines[save]
            save+=1
            if save ==26:
                save=0
        print(resultat)
        resultat = ""

chaine()    

    