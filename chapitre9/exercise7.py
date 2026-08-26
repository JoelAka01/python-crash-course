class User:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def describe_user(self):
        print(f"Nom Complet: {self.first_name} {self.last_name}")
    def  greet_user(self):
        print(f"Bonjour {self.first_name} {self.last_name} !")

class Admin (User):
    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)
        self.privileges = ["can add post", "can delete post", "can ban user"]

    def show_privileges(self):
        print(f"Les privilèges de l'administrateur {self.first_name} {self.last_name} sont :")
        for privilege in self.privileges:
            print(f"{privilege}")

                
user1 =  Admin("Alice", "Admin")
user2 =  User("Bob", "Admin")

user1.show_privileges()
