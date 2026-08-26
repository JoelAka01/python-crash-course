class User:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.login_attempts = 0

    def increment_login_attempts(self):
        self.login_attempts += 1
        print(f"votre limite est de : {self.login_attempts} ")

    def  reset_login_attempts(self):
        self.login_attempts = 0
        print(f"votre limite est de : {self.login_attempts} ")

user1= User("Joel" ,"Aka")


user1.increment_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()
user1.reset_login_attempts()
user1.increment_login_attempts()
