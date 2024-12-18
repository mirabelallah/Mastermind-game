import random


def generation_combinaison():
    return [random.randint(0, 6) for _ in range(4)]


def comparaion_combinaisons(secret, joueur):
    bonne_po = 0
    mauvaise_po = 0

    secret_copy = secret[:]
    joueur_copy = joueur[:]

    for i in range(4):
        if joueur[i] == secret[i]:
            bonne_po += 1
            secret_copy[i] = joueur_copy[i] = None

    for i in range(4):
        if joueur_copy[i] and joueur_copy[i] in secret_copy:
            mauvaise_po += 1
            secret_copy[secret_copy.index(joueur_copy[i])] = None

    return bonne_po, mauvaise_po


def jeu_mastermind():
    print("Nouvelle partie! Devine la combinaison secrete a 4 chiffre entre 0 et 6 et gagne la partie")
    combinaison_secrete = generation_combinaison()
    nbre_tentatives = 10

    while nbre_tentatives > 0:
        try:
            entree = input(f"\nTentative ({nbre_tentatives} restantes)")
            joueur = [int(x) for x in entree if x.isdigit()]
            if len(joueur) != 4:
                raise (ValueError(
                    "Saisie incorrecte. Tu dois entrer un code à 4 chiffres exactement!!"))
        except ValueError as e:
            print(e)
            continue

    bonne_po, mauvaise_po = comparaion_combinaisons(
        combinaison_secrete, joueur)
    print(f"Résultat : {bonne_po} bien placé(s), {mauvaise_po} mal placé(s)")

    if bonne_po == 4:
        print("Félicitations ! Tu as trouvé la combinaison secrète !")
    return
 
    nbre_tentatives -= 1

    print(f"\nDommage! la combinaison secrete est: {combinaison_secrete}.")


if __name__ == "__main__":
    jeu_mastermind()