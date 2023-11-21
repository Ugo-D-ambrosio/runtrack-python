print('\n'.join([' ' * (25 - abs(12 - i)) + ''.join(chr((j % 26) + 97) for j in range(abs(12 - i) * 2 + 1)) for i in range(25)]))
