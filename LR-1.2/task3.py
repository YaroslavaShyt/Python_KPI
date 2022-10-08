class Product:
    def __init__(self, price=0, description='', dimention=''):
        self.price = price
        self.description = description
        self.dimention = dimention

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, new_price):
        if not isinstance(new_price, (int, float)):
            raise TypeError('Incorrect value for price!')
        elif new_price <= 0:
            raise ValueError('Price must be above 0!')
        self.__price = new_price

    def show_product(self):
        return f'{self.description} - price: {self.price}'


class Customer:
    def __init__(self, surn='', name='', patr='', phone=''):
        self.surn = surn
        self.name = name
        self.patr = patr
        self.phone = phone

    def __str__(self):
        return f'{self.surn} {self.name} {self.patr} {self.phone}'


class Order:
    def __init__(self, product=None):
        self.products = {}
        self.total = 0
        for i in product:
            self.add_product(i)

    def add_product(self, new_product):
        if new_product.show_product() in self.products:
            self.products[new_product.show_product()][0] += 1
            self.products[new_product.show_product()][1] += new_product.get_price()
        else:
            self.products.update({new_product.show_product(): [1, new_product.get_price()]})

    def count_total(self):
        for i in self.products:
            self.total += self.products[i][1]
        return self.total

    def show_order(self, customer):
        print('Customer:', customer.__str__())
        for i in self.products:
            print(i, '*', self.products[i][0], '=', self.products[i][1])
        print('Total', self.count_total())


def main():
    try:
        c = Customer('Petrenko', 'Kateryna', 'Vitalivna', '098765432')
        goods = [Product(144, 'Book', '25x15'),
                 Product(123, 'Cactus', '20x10'),
                 Product(322, 'Rubbers', '2x3'),
                 Product(322, 'Rubbers', '2x3')]
        o = Order(goods)
        o.show_order(c)
    except Exception as ex:
        print(ex)


main()
