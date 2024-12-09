# Demander à l'utilisateur de définir le nombre entier n
n = int(input("Veuillez entrer un nombre entier n : "))  # Conversion de l'entrée en entier

# Fonction pour calculer la factorielle avec une boucle for
def calculer_factorielle_avec_for(nombre):
    resultat = 1
    for i in range(1, nombre + 1):
        resultat *= i  # Multiplier le résultat par i
    return resultat

# Fonction pour calculer la factorielle avec une boucle while
def calculer_factorielle_avec_while(nombre):
    resultat = 1
    i = 1
    while i <= nombre:
        resultat *= i  # Multiplier le résultat par i
        i += 1  # Incrémenter i
    return resultat

# Calculer et afficher les résultats de la factorielle
factorielle_for = calculer_factorielle_avec_for(n)
factorielle_while = calculer_factorielle_avec_while(n)

print(f"La factorielle de {n} (calculée avec for) est : {factorielle_for}")
print(f"La factorielle de {n} (calculée avec while) est : {factorielle_while}")
