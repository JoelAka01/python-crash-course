from pathlib import Path

name = input("Enter your name: ")
date = input("Enter the date (YYYY-MM-DD): ")
status = "En cours de livraison"

content = f"Nom: {name}\nDate: {date}\nStatut: {status}\n"

path = Path('bordereau.txt')

path.write_text(content)


