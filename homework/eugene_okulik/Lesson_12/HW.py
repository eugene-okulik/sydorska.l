class Flowers:
    def __init__(self, freshness, color, lenght, price, live_days):
        self.freshness = freshness
        self.color = color
        self.lenght = lenght
        self.price = price
        self.live_days = live_days

class Roses(Flowers):
    def __init__(self, freshes, color, long, price):
        super().__init__(freshes, color, long, price, live_days=7)

class Tulips(Flowers):
    def __init__(self, freshes, color, long, price):
        super().__init__(freshes, color, long, price, live_days=4)

class Peonys(Flowers):
    def __init__(self, freshes, color, long, price):
        super().__init__(freshes, color, long, price, live_days=4)

class Bouquet:
    def __init__(self):
        self.flowers = []

    def add_flower(self, flower):
        self.flowers.append(flower)

    def total_price(self):
        return sum(flower.price for flower in self.flowers)

    def average_life_time(self):
        if not self.flowers:
            return 0
        return sum(f.live_days for f in self.flowers) / len(self.flowers)

    def sort_by_freshness(self):
        self.flowers.sort(key=lambda f: f.freshness)

    def sort_by_color(self):
        self.flowers.sort(key=lambda f: f.color)

    def sort_by_stem_length(self):
        self.flowers.sort(key=lambda f: f.stem_length)

    def sort_by_price(self):
        self.flowers.sort(key=lambda f: f.price)

    def find_by_life_days(self, min_days):
        result = []
        for f in self.flowers:
            if f.life_days >= min_days:
                result.append(f)
                return result

    
    def find_by_color(self, color):
        result = []
        for f in self.flowers:
            if f.color == color:
                result.append(f)
                return result


bouquet = Bouquet()

bouquet.add_flower(Roses(9, "red", 50, 12))
bouquet.add_flower(Tulips(7, "yellow", 40, 8))
bouquet.add_flower(Peonys(8, "pink", 45, 11))

print("Bouquet price:", bouquet.total_price())
print("Average life time:", bouquet.average_life_time())

bouquet.sort_by_price()

red_flowers = bouquet.find_by_color("red")
print("Red flowers:", len(red_flowers))
