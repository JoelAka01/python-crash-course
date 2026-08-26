class User:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def describe_user(self):
        print(f"Nom Complet: {self.first_name} {self.last_name}")
    def  greet_user(self):
        print(f"Bonjour {self.first_name} {self.last_name} !")

class Privileges:
    def __init__(self):
        self.privileges = ["can add post", "can delete post", "can ban user"]

    def show_privileges(self):
        print("Les privilèges de l'administrateur sont :")
        for privilege in self.privileges:
            print(f"{privilege}")


class Admin (User):
    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)
        self.privileges= Privileges()
        
user1 =  Admin("Alice", "Admin")
user1.privileges.show_privileges()




