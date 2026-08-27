from user import User



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

