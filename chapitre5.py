#Tu disposes d'une liste d'utilisateurs souhaitant s'inscrire sur une application mobile. Certains font partie d'une liste noire. Écris un code qui parcourt les nouvelles inscriptions et affiche "Inscription refusée" si l'utilisateur est banni, sinon "Bienvenue [Nom] !".

"""

class User:
    def __init__(self, nom_utilisateur,statut):
        self.nom_utilisateur = nom_utilisateur
        self.statut = statut

    def afficher_nom(self):
        print(f"Nom d'utilisateur : {self.nom_utilisateur}" + f", Statut : {self.statut}")

utilisateurs_bannis = [User('hacker99', 'banni'), User('bot_spam', 'banni')]
nouvelles_inscriptions = [User('alice_dev', 'actif'), User('hacker99', 'actif'), User('bob_tech', 'actif')]

for user in nouvelles_inscriptions:
    if any(user.nom_utilisateur == banned_user.nom_utilisateur for banned_user in utilisateurs_bannis):
        print(f"Inscription refusée pour {user.nom_utilisateur}.")
    else:   
        print(f"Bienvenue {user.nom_utilisateur} !")
"""

#TP2 OTP/SMS
class AccountVerification:
    def __init__(self, phone_number):
        self.phone_number = phone_number
        self.otp = None
        self.attempts_left = 3
        self.is_verified = False

    def verify_code ( self , code_saisi, code_correct ):
        if self.attempts_left <= 0:
            print("Nombre de tentatives dépassé. Veuillez réessayer plus tard.")
            return False
        if code_saisi == code_correct:
            print("Vérification réussie !")
            self.is_verified = True
            return True
        else:
            self.attempts_left -= 1
            print(f"Code incorrect. Veuillez réessayer. Tentatives restantes : {self.attempts_left}")
            return False


AccountVerification1 = AccountVerification("1234567890")

AccountVerification1.verify_code("1234", "5678")  # Code incorrect
AccountVerification1.verify_code("5678", "5678")  # Code correct