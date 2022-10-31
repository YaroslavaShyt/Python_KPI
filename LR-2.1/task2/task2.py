import re
import json
import datetime


class Customer:
    def __init__(self, name, surname, phone):
        self.customer_name = name
        self.customer_surname = surname
        self.customer_phone = phone

    @property
    def customer_name(self):
        return self.__customer_name

    @customer_name.setter
    def customer_name(self, new_n):
        if not isinstance(new_n, str):
            raise TypeError('Incorrect type for name!')
        if re.search('[^A-Za-z\'-]', new_n):
            raise ValueError('Incorrect character in name!')
        self.__customer_name = new_n

    @property
    def customer_surname(self):
        return self.__customer_surname

    @customer_surname.setter
    def customer_surname(self, new_s):
        if not isinstance(new_s, str):
            raise TypeError('Incorrect type for surname!')
        if re.search('[^A-Za-z\'-]', new_s):
            raise ValueError('Incorrect character in surname!')
        self.__customer_surname = new_s

    @property
    def customer_phone(self):
        return self.__customer_phone

    @customer_phone.setter
    def customer_phone(self, new_ph):
        if not isinstance(new_ph, str):
            raise TypeError('Incorrect type for phone number!')
        if re.search('[^+0-9]', new_ph):
            raise ValueError('Incorrect character for phone number!')
        self.__customer_phone = new_ph

    def __str__(self):
        return f'--------CUSTOMER--------\n' \
               f'Name: {self.customer_name}\n' \
               f'Surname: {self.customer_surname}\n' \
               f'Phone number: {self.customer_phone}'


class MondayPizza:
    def __init__(self, day=0):
        with open('pizzas.json', 'r') as p:
            data = json.load(p)
        self.day = day
        self.pizza_name = data[str(self.day)]["name"]
        self.pizza_ingred = data[str(self.day)]["ingredients"]

    @property
    def day(self):
        return self.__day

    @day.setter
    def day(self, new_d):
        if not isinstance(new_d, int):
            raise TypeError("Incorrect day type!")
        if new_d < 0 or new_d > 6:
            raise ValueError("Incorrect value for day!")
        self.__day = new_d

    def __str__(self):
        return f'|Type|: {self.pizza_name}\n'\
               f'|Ingredients|: {str(self.pizza_ingred)[1:-1]}'


class TuesdayPizza(MondayPizza):
    def __init__(self, day=1):
        super().__init__(day)


class WednesdayPizza(MondayPizza):
    def __init__(self, day=2):
        super().__init__(day)


class ThursdayPizza(MondayPizza):
    def __init__(self, day=3):
        super().__init__(day)


class FridayPizza(MondayPizza):
    def __init__(self, day=4):
        super().__init__(day)


class SaturdayPizza(MondayPizza):
    def __init__(self, day=5):
        super().__init__(day)


class SundayPizza(MondayPizza):
    def __init__(self, day=6):
        super().__init__(day)


class Order:
    def __init__(self, customer):
        self.customer = customer
        self.ingredients_num = {}
        self.pizza_of_day = self.define_pizza()
        for i in self.pizza_of_day.pizza_ingred:
            self.ingredients_num[i] = 1

    @property
    def customer(self):
        return self.__customer

    @customer.setter
    def customer(self, new_c):
        if not isinstance(new_c, object):
            raise TypeError('Incorrect type for customer!')
        self.__customer = new_c

    @property
    def ingredients_num(self):
        return self.__ingredients_num

    @ingredients_num.setter
    def ingredients_num(self, new_i):
        if not isinstance(new_i, dict):
            raise TypeError('Incorrect type for ingredients dictionary!')
        self.__ingredients_num = new_i

    @property
    def pizza_of_day(self):
        return self.__pizza_of_day

    @pizza_of_day.setter
    def pizza_of_day(self, new_p):
        if not isinstance(new_p, object):
            raise TypeError('Incorrect type for pizza of the day!')
        self.__pizza_of_day = new_p

    @staticmethod
    def define_pizza():
        pizzas = {0: MondayPizza(), 1: TuesdayPizza(), 2: WednesdayPizza(), 3: ThursdayPizza(),
                  4: FridayPizza(), 5: SaturdayPizza(), 6: SundayPizza()}
        day = datetime.datetime.now().weekday()
        return pizzas[day]

    def make_order(self):
        print("Hello! Your pizza today:\n", self.pizza_of_day)
        while True:
            choice = input("Would you like add ingredients? -- Y(1)|N(0): ")
            if int(choice) == 1:
                self.add_ingredients()
            elif int(choice) == 0:
                break
            else:
                print('Wrong command!')
        return f"---Order---\n" \
               f"{self.pizza_of_day}\n" \
               f"{self.customer}\n" \
               f"---Total---\n"\
               f"{self.count_total()}"

    def add_ingredients(self):
        with open('pizzas.json', 'r') as p:
            data = json.load(p)
        self.show_ingredients(data)
        option = input("Choose the option: ")
        if option not in data["ingredients"] or list(data["ingredients"][option].keys())[0] not in self.ingredients_num:
            print('No such option.')
        else:
            self.ingredients_num[list(list(data["ingredients"].values())[int(option) - 1].keys())[0]] += 1

    def show_ingredients(self, data):
        for i in range(1, len(data["ingredients"]) + 1):
            if list(list(data["ingredients"].values())[i - 1].keys())[0] in list(self.ingredients_num.keys()):
                print(i, data["ingredients"][str(i)])

    def count_total(self):
        total = 0
        with open('pizzas.json', 'r') as p:
            data = json.load(p)
        for i in range(1, len(data["ingredients"])+1):
            product = list(list(data["ingredients"].values())[i-1].keys())[0]
            if product in list(self.ingredients_num.keys()):
                total += data["ingredients"][str(i)][product] * self.ingredients_num[product]
        return total


try:
    c = Customer('Mary', 'Smith', '0987654321')
    o = Order(c)
    print(o.make_order())
except Exception as ex:
    print(ex)
