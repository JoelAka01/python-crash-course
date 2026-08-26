"""
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price
        self.stock = 0

    def add_stock(self, quantity):
        self.stock += quantity
    def get_total_price(self, tax_rate):
        print(self.price * (1 + tax_rate) )


product1 = Product("Clavier Mécanique", 80.0 )
product1.add_stock(15)
product1.get_total_price(0.2)

2. Rappel Actif 
1. else est generique et traite les valeur inatendu
2. == recherche en tenant compte de la case trop generique 
3. Cas Pratique Métier 
1."Stock insuffisant"

"""


class User:
    """Modélise un utilisateur de la plateforme."""
    
    def __init__(self, first_name, last_name, login_attempts=0):
        """Initialise les attributs de nom et prénom."""
        # self.first_name devient un attribut de l'instance
        self.first_name = first_name
        self.last_name = last_name
        self.login_attempts = login_attempts

    def increment_login_attempts(self):
        """Incrémente le nombre de tentatives de connexion de l'utilisateur."""
        self.login_attempts += 1

    def reset_login_attempts(self):
        """Réinitialise le nombre de tentatives de connexion à zéro."""
        self.login_attempts = 0

    def describe_user(self):
        """Affiche un résumé des informations de l'utilisateur."""
        print(f"Profil Utilisateur : {self.first_name.title()} {self.last_name.title()}")

# Instanciation d'un nouvel utilisateur
new_user = User('jean', 'dupont')
new_user.increment_login_attempts()
print(f"Nombre de tentatives de connexion : {new_user.login_attempts}")
new_user.increment_login_attempts()
print(f"Nombre de tentatives de connexion : {new_user.login_attempts}")

new_user.increment_login_attempts()
print(f"Nombre de tentatives de connexion : {new_user.login_attempts}")

new_user.increment_login_attempts()
print(f"Nombre de tentatives de connexion : {new_user.login_attempts}")

new_user.reset_login_attempts()
print(f"Nombre de tentatives de connexion : {new_user.login_attempts}")

new_user.increment_login_attempts()
print(f"Nombre de tentatives de connexion : {new_user.login_attempts}")