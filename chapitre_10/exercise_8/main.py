from pathlib import Path
fichiers = ['dogs.txt', 'cats.txt']

for nom_fichier in fichiers:
    chemin = Path(nom_fichier)
    try :
        donnees = chemin.read_text(encoding='utf-8')
    except FileNotFoundError:
        print(f"Alerte : Le fichier '{nom_fichier}' est manquant. Étape ignorée.")
    else:
        print(f"\n--- Contenu de {nom_fichier} ---")
        print(donnees)