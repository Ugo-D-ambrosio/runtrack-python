def arrondir_notes(liste_notes):
    notes_arrondies = []

    for note in liste_notes:
        if note < 40:
            # Étudiant échoue, pas d'arrondi
            notes_arrondies.append(note)
        else:
            # Étudiant réussit, vérification des critères d'arrondi
            multiple_de_5_sup = (note // 5 + 1) * 5  # Prochain multiple de 5 supérieur
            difference = multiple_de_5_sup - note

            if difference < 3:
                # Arrondir à ce multiple de 5
                notes_arrondies.append(multiple_de_5_sup)
            else:
                # Pas besoin d'arrondir
                notes_arrondies.append(note)

    return notes_arrondies

# Exemple d'utilisation
liste_notes = [83, 72, 55, 41, 39, 68]
notes_arrondies = arrondir_notes(liste_notes)

# Affichage des résultats
print(f"Notes initiales : {liste_notes}")
print(f"Notes arrondies : {notes_arrondies}")
