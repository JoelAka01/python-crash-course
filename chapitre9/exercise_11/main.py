from user import Admin

# Instanciation propre d'un compte administrateur
admin = Admin("Ada", "Lovelace")

# Validation des fonctionnalités
admin.describe_user()
admin.privileges.show_privileges()