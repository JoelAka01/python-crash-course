# """Exercice 1 et 2 du chapitre 9 : Classe Restaurant"""

# class Restaurant:
#     def __init__(self, name, type):
#         self.name = name
#         self.type = type
    
#     def describe_restaurant(self):
#         print(f"Nom du restaurant : {self.name}")
#         print(f"Type de cuisine : {self.type}")

# restaurant1=Restaurant("Le Gourmet", "Française")
# restaurant2=Restaurant("Sushi World", "Jap")
# restaurant3=Restaurant("Pasta Paradise", "Italienne")


# restaurant1.describe_restaurant()
# restaurant2.describe_restaurant()
# restaurant3.describe_restaurant()

class Restaurant:
    def __init__(self, Restaurant_name, cuisine_type, number_served =0):
        self.Restaurant_name = Restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = number_served

    def describe_restaurant(self):
        print(f"Nom du Restaurant : {self.Restaurant_name} type de cuisine :{self.cuisine_type} ")
    def open_restaurant(self):
        print(f"Votre Restaurant {self.Restaurant_name} est ouvert")

    def set_number_served(self, number):
        self.number_served = number

    def increment_number_served(self, increment):
        self.number_served += increment

restaurant=Restaurant("Son des Marmite","Africaine")

