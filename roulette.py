import random
import pickle

# Fonction pour obtenir un pseudo valide
def obtenir_pseudo():
    while True:
        pseudo = input("Entrez un pseudo (en minuscules, sans espaces) : ")
        if ' ' not in pseudo and pseudo.islower():
            return pseudo
        else:
            print("Pseudo invalide. Stp Réessayez.")

# Fonction pour obtenir l'intervalle de nombres
def obtenir_intervalle():
    while True:
        try:
            min_num = int(input("Entrez le nombre minimum de l'intervalle : "))
            max_num = int(input("Entrez le nombre maximum de l'intervalle : "))
            return min_num, max_num
        except ValueError:
            print("Veuillez entrer des nombres valides.")

# Fonction pour jouer une partie
def jouer_partie(min_num, max_num):
    nombre_secret = random.randint(min_num, max_num)
    nombre_essais = max_num - min_num + 1
    score = nombre_essais * 30

    print(f"Devinez un nombre entre {min_num} et {max_num}.")
    
    while nombre_essais > 0:
        try:
            devine = int(input(f"Il vous reste {nombre_essais} essais. Entrez votre choix : "))
            if min_num <= devine <= max_num:
                if devine == nombre_secret:
                    print("BRAVO ! Vous avez trouvé le nombre secret.")
                    return score
                elif devine < nombre_secret:
                    print("Le nombre secret est plus grand.")
                else:
                    print("Le nombre secret est plus petit.")
                nombre_essais -= 1
                score = nombre_essais * 30
            else:
                print("Nombre en dehors de l'intervalle. Réessayez.")
        except ValueError:
            print("Entrez un nombre valide.")

    print(f"Vous avez perdu. Le nombre secret était {nombre_secret}.")
    return 0

# Base de données pour stocker les scores
scores = {}

try:
    with open("scores.pkl", "rb") as fichier_scores:
        scores = pickle.load(fichier_scores)
except FileNotFoundError:
    pass

while True:
    pseudo = obtenir_pseudo()
    
    if pseudo in scores:
        print(f"Bienvenue de nouveau, {pseudo} ! Votre score actuel est {scores[pseudo]}.")
    else:
        print(f"Bienvenue, {pseudo} ! Vous n'avez pas encore de score enregistré.")

    min_num, max_num = obtenir_intervalle()
    score_partie = jouer_partie(min_num, max_num)

    if pseudo in scores:
        scores[pseudo] += score_partie
    else:
        scores[pseudo] = score_partie

    print(f"Votre score dans cette partie est {score_partie}. Votre score total est maintenant {scores[pseudo]}.")

    with open("scores.pkl", "wb") as fichier_scores:
        pickle.dump(scores, fichier_scores)

    continuer = input("Voulez-vous rejouer ? (Appuyez sur 'K' pour quitter) : ")
    if continuer.lower() != 'k':
        break
