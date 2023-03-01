class Bar:
    def __init__(self, name, location, quantity, amount):
        self.name = name
        self.location = location
        self.__quantity = quantity
        self.amount = amount

    def serve_beer(self, price_litre):
        self.amount = float(self.__quantity * price_litre)
        return self.amount


new_bar = Bar("Three lions", "Birmingham", 2, 5)
print(new_bar.serve_beer(7.5))
