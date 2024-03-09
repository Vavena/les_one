class House:
    disc = 10
    def __init__(self, area, price ):
        self._area = area
        self._price = price
    def final_price(self):
        return self._price*2

class SmallHouse(House):
    def __init__(self, area, price):
        super().__init__(area, price)
        self.area = 40


class Human(House):
    default_name = "Человек"
    default_age = "20"

    def __init__(self, area, price, name=default_name, age=default_age):
        super().__init__(area, price)
        self.name = name
        self.age = age
        self.__money = 0
        self.__house = None

    def info(self):
        print(self.name, ' ', self.age, ' ', self.__house, ' ', self.__money)

    def default_info(self):
        print(self.default_name, self.default_age)

    def make_deal(self, house:House,result_cost):
        self.__money = self.__money - int(result_cost)
        self.__house=house

    def earn_money(self):
        self.__money+=2500

    def buy_house(self, house: House):
        result_cost = house.final_price(self)
        if (self.__money>=int(result_cost)):
            self.make_deal(house,result_cost)
        else:
            print("УУУ, мало деняг, иди работать.")


a = Human("Пупкин", "10")
b=House(20, 100)
a.default_info()
a.info()
a.buy_house(House)
a.earn_money()
a.buy_house(House)
a.info()