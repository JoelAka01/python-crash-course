from pathlib import Path

try:
    path = Path('ebook.txt')
    content = path.read_text(encoding='utf-8')
except FileNotFoundError:
    print("Le fichier n'existe pas.")
else:
    the_count = content.lower().count('the')
    print(f"{the_count}")

