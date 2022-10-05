class Product:
    def __init__(self, price=0, description='', dimention=''):
        self.price = self.set_price(price)
        self.description = description
        self.dimention = dimention

    def get_price(self):
        return self.price

    def set_price(self, new_price):
        if isinstance(new_price, int) and new_price > 0:
            self.price = new_price
            return self.price
        else:
            raise TypeError('Incorrect value for price!')

    def show_product(self):
        return f'{self.description} size:{self.dimention} price:{self.price}'


class Customer:
    def __init__(self, surn='', name='', patr='', phone=''):
        self.surn = surn
        self.name = name
        self.patr = patr
        self.phone = phone

    def __str__(self):
        return f'{self.surn} {self.name} {self.patr} {self.phone}'


class Order:
    def __init__(self, **product):
        self.products = {}
        for i in product:
            self.add_product(product[i])

    def add_product(self, new_product):
        if new_product.show_product() in self.products:
            self.products[new_product.show_product()][0] += 1
            self.products[new_product.show_product()][1] += new_product.get_price()
        else:
            self.products.update({new_product.show_product(): [1, new_product.get_price()]})

    def count_total(self):
        total = 0
        for i in self.products:
            total += self.products[i][1]
        return total


def show_order(c, o):
    print('Customer:', c.__str__())
    for i in o.products:
        print(i, '*', o.products[i][0], '=', o.products[i][1])


def main():
    try:
        c = Customer('Petrenko', 'Kateryna', 'Vitalivna', '098765432')
        g1 = Product(144, 'Book', '25x15')
        g2 = Product(123, 'Cactus', '20x10')
        g3 = Product(322, 'Rubbers', '2x3')
        g4 = Product(322, 'Rubbers', '2x3')
        o = Order(first_p=g1, second_p=g2, third_p=g3, fourth_p=g4)
        show_order(c, o)
        print('Total:', o.count_total())
    except Exception as ex:
        print(ex)


main()
