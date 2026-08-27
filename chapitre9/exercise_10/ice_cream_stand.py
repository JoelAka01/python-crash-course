from restaurant import Restaurant

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
