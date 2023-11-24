def my_sort(liste):
    n = len(liste)
    coups = 0  # Compteur pour le nombre total de coups

    # La variable 'trié' est utilisée pour vérifier si la liste est déjà triée
    trié = False
    
    while not trié:
        trié = True  # On suppose que la liste est triée au début de chaque itération
        for i in range(n - 1):
            if liste[i] > liste[i + 1]:
                # Échange d'éléments adjacents
                liste[i], liste[i + 1] = liste[i + 1], liste[i]
                trié = False  # La liste n'est pas encore triée, on continue le tri
                coups += 1  # Incrémente le nombre total de coups

    # Affiche le nombre total de coups
    print(f"Nombre total de coups nécessaires pour trier la liste : {coups}")

    return liste

# Exemple d'utilisation
ma_liste = [5, 2, 9, 1, 5, 6]
liste_triee = my_sort(ma_liste)

# Affichage des résultats
print(f"Liste initiale : {ma_liste}")
print(f"Liste triée : {liste_triee}")

