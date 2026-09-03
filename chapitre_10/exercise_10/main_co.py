from pathlib import Path
path = Path('ebook.txt')

try:
    content = path.read_text(encoding='utf-8')
except FileNotFoundError:
    print("Le fichier n'existe pas.")
else:
# Compte toutes les sous-chaînes contenant 'the'
    all_the = content.lower().count('the')
    # Approche plus précise : mot suivi d'une espace
    exact_the = content.lower().count('the ')

    print(f"Occurrences totales (inclut 'there', 'other', etc.) : {all_the}")
    print(f"Occurrences du mot 'the ' (approximatif) : {exact_the}")

