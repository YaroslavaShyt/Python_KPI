class Product:
    def __init__(self, price=0, description='', dimention=''):
        self.__price = price
        self.__description = description
        self.__dimention = dimention

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, new_price):
        if new_price > 0:
            self.__price = new_price
        else:
            print('Incorrect value!')

    def show_product(self):
        return f'{self.__description} {self.__dimention} {self.__price}'


class Customer:
    def __init__(self, surn='', name='', patr='', phone=''):
        self.__surn = surn
        self.__name = name
        self.__patr = patr
        self.__phone = phone

    def __str__(self):
        return f'{self.__surn} {self.__name} {self.__patr} {self.__phone}'


class Order:
    def __init__(self, custom, **product):
        self.__custom = custom
        self.__product = product

    def show_order(self):
        print(self.__custom.__str__())
        for i in self.__product:
            print(self.__product[i].show_product())

    def total_cost(self):
        total = 0
        for i in self.__product:
            total += float(self.__product[i].price)
        return total


def main():
    c = Customer('Petrenko', 'Kateryna', 'Vitalivna', '098765432')
    g1 = Product(144, 'Book', '25x15')
    g2 = Product(123, 'Cactus', '20x10')
    g3 = Product(322, 'Rubbers', '2x3')
    o = Order(c, first_p=g1, second_p=g2, third_p=g3)
    o.show_order()
    print('Total:', o.total_cost())


main()
