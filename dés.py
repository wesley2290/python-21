from itertools import product

def count_ways_to_sum(target_sum, num_dice, num_faces):
    # Créer toutes les combinaisons possibles de lancers de dés
    all_rolls = product(range(1, num_faces + 1), repeat=num_dice)
    # Compter les combinaisons qui donnent la somme cible
    valid_combinations = [roll for roll in all_rolls if sum(roll) == target_sum]
    return len(valid_combinations)

def main():
    # Interaction avec l'utilisateur
    try:
        num_dice = int(input("Entrez le nombre de dés (par défaut 5) : ") or 5)
        target_sum = int(input("Entrez la somme cible (par défaut 20) : ") or 20)
        num_faces = 6  # Nombre de faces d'un dé à six faces

        print(f"Calcul des façons d'obtenir une somme de {target_sum} avec {num_dice} dés à {num_faces} faces.")
        ways = count_ways_to_sum(target_sum, num_dice, num_faces)
        print(f"Il y a {ways} façons différentes d'obtenir la somme de {target_sum}.")
    except ValueError:
        print("Veuillez entrer des nombres valides.")

if __name__ == "__main__":
    main()
