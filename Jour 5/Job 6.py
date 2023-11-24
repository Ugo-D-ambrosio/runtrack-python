def distance_totale_semaine(nombre_marches, hauteur_marche_cm):
    hauteur_marche_m = hauteur_marche_cm / 100  # Conversion en mètres
    distance_journaliere = (2 * nombre_marches - 1) * hauteur_marche_m
    distance_semaine = distance_journaliere * 7
    return distance_semaine

# Exemple d'utilisation
nombre_marches = 10
hauteur_marche_cm = 20

distance_semaine = distance_totale_semaine(nombre_marches, hauteur_marche_cm)

# Affichage des résultats
print(f"Pour {nombre_marches} marches de {hauteur_marche_cm} cm, le gardien parcourt {distance_semaine:.2f} m par semaine.")
