#### Imports et définition des variables globales
"""
    imporer les fichiers csv
"""
import csv

FILENAME = "listes.csv"

#### Fonctions secondaires

def read_data(filename):
    """retourne le contenu du fichier <filename>

    Args:
        filename (str): nom du fichier à lire

    Returns:
        list: le contenu du fichier (1 list par ligne)
    """
    with open(filename, 'r', encoding='utf-8') as f:
        # Lire les données du fichier ligne par ligne
        reader = csv.reader(f, delimiter=';')
        # Convertir chaque ligne en une liste d'entiers
        data = [[int(value) for value in row] for row in reader]
    return data

def get_list_k(data, k):
    """
        retourn la liste d'indice k
    """
    if k<0 or k>= len(data) :
        print("indice hors limite")
        return None
    return data[k]
def get_first(l):
    """
        première valeur de la liste
    """
    return l[0] if l else None
def get_last(l):
    """
        dernière valeur de la liste
    """
    return l[-1] if l else None
def get_max(l):
    """
        valeur max de la liste en arg
    """
    return max(l) if l else None
def get_min(l):
    """
        valeur minimum de la liste
    """
    return min(l) if l else None

def get_sum(l):
    """
        somme des termes de la liste
    """
    m = 0
    for i in l :
        m += i
    return m if l else None
#### Fonction principale


def main():

    """Fonction principale pour tester les fonctions secondaires."""
    # Nom du fichier contenant les données
    filename = "listes.csv"

    try:
        # Lire les données depuis le fichier
        data = read_data(filename)
        print("Données lues depuis le fichier :")
        print(data)

        # Tester la fonction get_list_k
        k = 1  # Exemple d'indice
        kth_list = get_list_k(data, k)
        print(f"Liste à l'indice {k} : {kth_list}")

        # Tester les autres fonctions sur une liste donnée
        example_list = kth_list
        print(f"Première valeur de la liste : {get_first(example_list)}")
        print(f"Dernière valeur de la liste : {get_last(example_list)}")
        print(f"Valeur maximale de la liste : {get_max(example_list)}")
        print(f"Valeur minimale de la liste : {get_min(example_list)}")
        print(f"Somme des valeurs de la liste : {get_sum(example_list)}")

    except FileNotFoundError:
        print(f"Erreur : Le fichier '{filename}' est introuvable.")
    except ValueError as ve:
        print(f"Erreur de conversion en entier : {ve}")
    except csv.Error as ce:
        print(f"Erreur lors du traitement du fichier CSV : {ce}")
    except IndexError:
        print("Erreur : Indice hors limites pour get_list_k.")

if __name__ == "__main__":
    main()
