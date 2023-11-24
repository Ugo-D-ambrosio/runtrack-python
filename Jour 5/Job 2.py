def draw_rectangle(width, height):
    for i in range(height):
        if i == 0 or i == height - 1:
            # Première et dernière ligne du rectangle
            print('-' * width)
        else:
            # Lignes internes du rectangle
            print('|' + ' ' * (width - 2) + '|')

# Exemple d'utilisation avec une largeur de 10 et une hauteur de 3
draw_rectangle(18, 7)
