
print("Donne deux nombres, et je les additionnerai.")
print("Entrez 'q' pour quitter.")


nombre1 = input("Saisir votre premier nombre: ")
nombre2 = input("Saisir votre deuxième nombre: ")


while True:
    if nombre1 == 'q' or nombre2 == 'q':
        print("Vous avez choisi de quitter le programme.")
        break
    try:
        total = sum([int(nombre1), int(nombre2)])
        print("Le total est:", total)
    except ValueError:
        print("Veuillez entrer des nombres valides.")

        




