print("Entrez deux nombres à additionner (ou 'q' pour quitter).")

while True:
    premier = input("\nPremier nombre : ")
    if premier.lower() == 'q':
        break

    deuxieme = input("Deuxième nombre : ")
    if deuxieme.lower() == 'q':
        break

    try:
        total = int(premier) + int(deuxieme)
    except ValueError:
        print("Erreur : vous devez renseigner des nombres entiers valides.")
    else:
        print(f"Le résultat de {premier} + {deuxieme} est : {total}")