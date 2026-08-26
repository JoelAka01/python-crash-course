class Restaurant:
    def __init__(self, Restaurant_name, cuisine_type):
        self.Restaurant_name = Restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print(f"Nom du Restaurant : {self.Restaurant_name} type de cuisine :{self.cuisine_type} le restaurant a servis",self.number_served)
    def open_restaurant(self):
        print(f"Votre Restaurant {self.Restaurant_name} est ouvert")

    def set_number_served(self):
        self.number_served = 15
        print("le restaurant a servis",self.number_served)
    def increment_number_served(self , add_customer_served):
        self.number_served += add_customer_served
        print(f"nous avons servis: {self.number_served }")


restaurant=Restaurant("Son des Marmite","Africaine")

restaurant.set_number_served()

