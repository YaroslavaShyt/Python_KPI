import re


class Item:
    def __init__(self, code, name, price, quantity):
        self.code = code
        self.name = name
        self.price = price
        self.quantity = quantity

    @property
    def code(self):
        return self.__code

    @code.setter
    def code(self, new_c):
        if not isinstance(new_c, str):
            raise TypeError('Incorrect type for item code!')
        if not re.search('[0-9]+', new_c):
            raise ValueError('Incorrect value for item code!')
        self.__code = new_c

    @property
    def name(self):
        return self.__name

    @property
    def price(self):
        return self.__price

    @name.setter
    def name(self, new_n):
        if not isinstance(new_n, str):
            raise TypeError('Incorrect type for item name!')
        elif re.search(r'[^\'A-Za-z\s-]', new_n):
            raise ValueError('Incorrect character in item name!')
        self.__name = new_n

    @price.setter
    def price(self, new_p):
        if not isinstance(new_p, int | float):
            raise TypeError('Incorrect type for item price!')
        if new_p < 0:
            raise ValueError('Item price cannot be less 0')
        self.__price = new_p

    def __str__(self):
        return f'{self.name}'


lst_of_goods = [Item('9999', "Soap with strawberries", 12, 100),
                Item('1234', "Mint toothpaste", 20, 50),
                Item('3241', "Shampoo with chocolate", 60, 150)]


class Composition:

    def __init__(self):
        self.goods = []
        self.index = 0

    def add_item(self, i):
        self.goods = self.goods + [i]

    def __iter__(self):
        self.index = 0
        return self

    def __next__(self):
        if self.index < len(self.goods):
            self.index += 1
            return self.index, self.goods[self.index - 1]
        raise StopIteration

    def __setitem__(self, index, value):
        self.goods[index] = value

    def __getitem__(self, index):
        return self.goods[index]

    def __len__(self):
        return len(self.goods)


class Menu:

    def show_menu(self, items):
        while True:
            ch = input(f'Choose menu option or exit(e):\n'
                       f'1. Add info\n'
                       f'2. Get info\n'
                       f'3. Form report all-left\n')
            if ch == '1':
                self.add_info(items)
            elif ch == '2':
                self.get_info(items)
            elif ch == '3':
                self.form_report(items)
            elif ch == 'e':
                break
            else:
                print('Wrong command!')

    def add_info(self, items):
        self.get_info(items)
        while True:
            choice = input('Enter the number of item you want to change or exit (e): ')
            if choice != 'e':
                if int(choice) <= len(items):
                    option = input('Enter option you want to change (1-name, 2-price, 3-quantity, e-exit): ')
                    if option == '1':
                        name = input('Enter new name: ')
                        items[int(choice)-1].name = name
                    elif option == '2':
                        price = input('Enter new price: ')
                        items[int(choice) - 1].price = float(price)
                    elif option == '3':
                        quantity = input('Enter new quantity: ')
                        items[int(choice) - 1].quantity = int(quantity)
                    elif option == 'e':
                        break
                    else:
                        print('Unknown command!')
                else:
                    print('This item does not exist!')
            else:
                break

    @staticmethod
    def get_info(items):
        for num, i in items:
            print(num, i)

    @staticmethod
    def search_item(items, code):
        for num, obj in items:
            if obj.code == code:
                return obj
        return 0

    @staticmethod
    def form_report(items):
        while True:
            choice = input('Enter code of item you want to get report on or exit(e): ')
            if choice == 'e':
                break
            elif int(choice) <= len(items):
                print(f'Title: {items[int(choice) - 1]} \nPrice: {items[int(choice) - 1].price}'
                      f'\nAll-left: {items[int(choice) - 1].quantity}')
            else:
                print('No such item.')


try:
    ItemsBase = Composition()
    for i in lst_of_goods:
        ItemsBase.add_item(i)
    m = Menu()
    m.show_menu(ItemsBase)
except Exception as ex:
    print(ex)

