# Compter le nombre de mots dans une phrchaine de mot inseree par l'utilisateur
chaine = input(str("Inserer une chaine de mots: "))


def count_word():
    mots = str(len(chaine.split()))
    print("Il y a" + mots + "mots dans votre chaine")


# Utilisation du "str" pour ajouter(+) le resultat du nombre(len) de suite de lettre coupee par une space (split())
count_word()
