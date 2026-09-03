number_1 = input("Entrez un premier nombre : ")
number_2 = input("Entrez un deuxième nombre : ")

try:
    somme = int(number_1) + int(number_2)
except ValueError:
    print("veuillez entrer un nombre")
else:
    print(f"la somme de vos nombres est {somme}")
     
