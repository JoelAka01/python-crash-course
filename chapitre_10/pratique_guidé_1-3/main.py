from pathlib import Path

contenu_pi = Path('produits_rappeles.txt').read_text()
code_produits = 'PROD-892'

if code_produits in contenu_pi:
    print(f'Le produit {code_produits} est rappelé.')
else:
    print(f'Le produit {code_produits} n\'est pas rappelé.')
