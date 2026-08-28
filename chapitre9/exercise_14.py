#Lotery 

from random import  choice

liste_nombre = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
liste_lettre = ['a', 'b', 'c', 'd', 'e']

print("the winning 4 numbers and letters are: ")

print(choice(liste_nombre), choice(liste_lettre))

print(choice(liste_nombre), choice(liste_lettre))
print(choice(liste_nombre), choice(liste_lettre))
print(choice(liste_nombre), choice(liste_lettre))
print(choice(liste_nombre), choice(liste_lettre))