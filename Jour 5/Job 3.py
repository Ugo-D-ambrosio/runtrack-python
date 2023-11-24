def draw_triangle(height):
    for i in range(height):
        spaces = ' ' * (height - i - 1)
        if i == 0:
            # Première ligne du triangle
            print(spaces + '_')
        elif i == height - 1:
            # Dernière ligne du triangle
            print('/' + '_' * (2 * i - 1) + '\\')
        else:
            # Lignes internes du triangle
            print(spaces + '/' + ' ' * (2 * i - 1) + '\\')

# Exemple d'utilisation avec une hauteur de 5
draw_triangle(7)
