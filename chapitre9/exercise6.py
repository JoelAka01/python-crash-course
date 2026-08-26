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


class IceCreamStand(Restaurant):
    def __init__(self, Restaurant_name, cuisine_type, number_served =0):
        
        super().__init__( Restaurant_name, cuisine_type, number_served)
        self.Restaurant_name = Restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = number_served
        self.flavors = ["vanille", "pistache", "Lemon"]
        
    def displays_flavors(self):
        print("Les saveurs disponibles sont :")
        for flavor in self.flavors:
            print(f"{flavor}")
        
icestand = IceCreamStand("Walletbleu","Europeene",10)

icestand.displays_flavors()
