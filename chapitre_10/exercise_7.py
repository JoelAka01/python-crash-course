print("Entrez deux nombres à additionner (ou 'q' pour quitter).")
while True:
    number_1 = input("Entrez un premier nombre : ")
    if number_1 ==  "q":
        print("vous avez choisir de quitté")
        break
    number_2 = input("Entrez un deuxième nombre : ")
    if number_2 == "q":
        print("vous avez choisir de quitté")
        break
    try:
        somme = int(number_1) + int(number_2)
    except ValueError:
        print("veuillez entrer un nombre")
    else:
        print(f"la somme de vos nombres est {somme}")


