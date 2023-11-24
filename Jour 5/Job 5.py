def chiffrement_cesar(message, decalage):
    resultat = ''
    for caractere in message:
        if caractere.isalpha():  # Vérifie si le caractère est une lettre
            decalage = decalage % 26  # Assure que le décalage reste dans la plage d'une longueur d'alphabet

            if caractere.isupper():
                nouveau_code = (ord(caractere) - ord('A') + decalage) % 26 + ord('A')
                resultat += chr(nouveau_code)
            else:
                nouveau_code = (ord(caractere) - ord('a') + decalage) % 26 + ord('a')
                resultat += chr(nouveau_code)
        else:
            resultat += caractere

    return resultat

# Exemple d'utilisation
message_original = "SAT Meilleur que la team la detail"
decalage = 3
message_chiffre = chiffrement_cesar(message_original, decalage)
print(f"Message original: {message_original}")
print(f"Message chiffré : {message_chiffre}")
