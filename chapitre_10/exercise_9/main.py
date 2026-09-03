from pathlib import Path
fichiers = ['dogs.txt', 'cats.txt']

for nom_fichier in fichiers:
    chemin = Path(nom_fichier)
    try:
        donnees = chemin.read_text(encoding='utf-8')
    except FileNotFoundError:
        pass
    else:
        print(f"\n--- Contenu de {nom_fichier} ---")
        print(donnees)