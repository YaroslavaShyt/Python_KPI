import re


class Composition:
    def __init__(self, item_name, item_price, quantity):
        self.item_name = item_name
        self.item_price = item_price
        self.quantity = quantity

    @property
    def item_name(self):
        return self.__item_name

    @property
    def item_price(self):
        return self.__item_price

    @item_name.setter
    def item_name(self, new_n):
        if not isinstance(new_n, str):
            raise TypeError('Incorrect type for item name!')
        elif re.search(r'[^\'A-Za-z\s-]', new_n):
            raise ValueError('Incorrect character in item name!')
        self.__item_name = new_n

    @item_price.setter
    def item_price(self, new_p):
        if not isinstance(new_p, int | float):
            raise TypeError('Incorrect type for item price!')
        if new_p < 0:
            raise ValueError('Item price cannot be less 0')
        self.__item_price = new_p

    def __gt__(self, other):
        if isinstance(other, (int, float)):
            return self.item_price > other
        elif isinstance(other, Composition):
            return self.item_price > other.item_price
        return NotImplemented

    def __lt__(self, other):
        if isinstance(other, (int, float)):
            return self.item_price < other
        elif isinstance(other, Composition):
            return self.item_price < other.item_price
        return NotImplemented

    def __eq__(self, other):
        if isinstance(other, (int, float)):
            return self.item_price == other
        elif isinstance(other, Composition):
            return self.item_price == other.item_price
        return NotImplemented

    def __str__(self):
        return f'{self.item_name}'


class ItemOperations:

    def __init__(self):
        self.goods = []
        self.index = 0

    def add_item(self, item):
        self.goods.append(item)

    def __add__(self, item):
        if not isinstance(item, ItemOperations):
            raise TypeError('Incorrect type for item you add to list.')
        for id, i_name in item:
            self.goods.append(i_name)

    def __sub__(self, item):
        if not isinstance(item, ItemOperations):
            raise TypeError('Incorrect type for item you take off the list.')
        for id, i_name in item:
            self.goods.remove(i_name)

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


lst_of_goods_1 = [Composition("Soap with strawberries", 12, 100),
                  Composition("Mint toothpaste", 20, 50),
                  Composition("Shampoo with chocolate", 60, 150)]
lst_of_goods_2 = [Composition("Pink toothbrush", 100, 200),
                  Composition("Hair mask with vitamins", 88, 50),
                  Composition("Black face mask", 2000, 10)]
try:
    ItemsBase1 = ItemOperations()
    ItemsBase2 = ItemOperations()
    for i in lst_of_goods_1:
        ItemsBase1.add_item(i)
    for i in lst_of_goods_2:
        ItemsBase2.add_item(i)
    # combine two lists of items
    ItemsBase1 + ItemsBase2
    for num, name in ItemsBase1:
        print(num, name)
    print()
    # remove items from the first list
    ItemsBase1 - ItemsBase2
    for i, name in ItemsBase1:
        print(i, name)
    print()
    # get item using index
    print(ItemsBase1[0], '\n')
    # change item using index
    ItemsBase1[0] = Composition("Banana face gel", 200, 35)
    print(ItemsBase1[0], '\n')
    # compare item's prices
    print(ItemsBase1[0] < ItemsBase1[1])
    print(ItemsBase1[2] > 10)
    print(ItemsBase2[2] == 2000)
except Exception as ex:
    print(ex)
