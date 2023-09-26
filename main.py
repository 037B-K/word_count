## Compter le nombre de mots dans une phrchaine de mot inseree par l'utilisateur
def count_word(chaine):
    #Compter le nombre de chaine de lettres coupee par un espace
    mots = int(len(chaine.split()))
    #Retourner le resultat dans la console
    print("il y a ", mots, " mots dans la chaine")

    return
# la fonction et le string a compter les nombres
count_word("Plusieur mots dans cette phrase")
