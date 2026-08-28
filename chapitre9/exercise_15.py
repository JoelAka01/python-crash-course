#Lotery 

from random import  choice

liste_nombre = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
liste_lettre = ['a', 'b', 'c', 'd', 'e']
my_ticket = []

for i in range(2):
    my_ticket.append(choice(liste_nombre))
    my_ticket.append(choice(liste_lettre))
print("the winning 4 numbers or letters are: ")

print(my_ticket)