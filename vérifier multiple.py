# Demander à l'utilisateur de définir la plage pour vérifier les multiples
max_range = int(input("Veuillez entrer un nombre entier pour vérifier les multiples de 1 à ce nombre : "))

# Fonction pour vérifier les entiers de 1 à max_range et afficher des messages appropriés
def verifier_multiples(max_range):
    for i in range(1, max_range + 1):
        if i % 3 == 0 and i % 5 == 0:
            print(f"{i} : Mon nom et prénom")  # Afficher si multiple de 3 et 5
        elif i % 3 == 0:
            print(f"{i} : Mon nom")  # Afficher si multiple de 3
        elif i % 5 == 0:
            print(f"{i} : Mon prénom")  # Afficher si multiple de 5

# Lancer la vérification des multiples
if __name__ == "__main__":
    verifier_multiples(max_range)
