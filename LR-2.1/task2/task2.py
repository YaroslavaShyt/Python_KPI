import re
import json
import datetime


class Customer:
    def __init__(self, name, surname, phone):
        self.name = name
        self.surname = surname
        self.phone = phone

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_n):
        if not isinstance(new_n, str):
            raise TypeError('Incorrect type for name!')
        if re.search('[^A-Za-z\'-]', new_n):
            raise ValueError('Incorrect character in name!')
        self.__name = new_n

    @property
    def surname(self):
        return self.__surname

    @surname.setter
    def surname(self, new_s):
        if not isinstance(new_s, str):
            raise TypeError('Incorrect type for surname!')
        if re.search('[^A-Za-z\'-]', new_s):
            raise ValueError('Incorrect character in surname!')
        self.__surname = new_s

    @property
    def phone(self):
        return self.__phone

    @phone.setter
    def phone(self, new_ph):
        if not isinstance(new_ph, str):
            raise TypeError('Incorrect type for phone number!')
        if re.search('[^+0-9]', new_ph):
            raise ValueError('Incorrect character for phone number!')
        self.__phone = new_ph

    def __str__(self):
        return f'--------CUSTOMER--------\n' \
               f'Name: {self.name}\n' \
               f'Surname: {self.surname}\n' \
               f'Phone number: {self.phone}'


class MondayPizza:
    def __init__(self, day=0):
        with open('pizzas.json', 'r') as p:
            data = json.load(p)
        self.day = day
        self.pizzaname = data[str(self.day)]["name"]
        self.pizzaingred = data[str(self.day)]["ingredients"]

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
        return f'|Type|: {self.pizzaname}\n'\
               f'|Ingredients|: {str(self.pizzaingred)[1:-1]}'


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
    def __init__(self, custom):
        self.custom = custom
        self.price = 0
        self.choice = 1
        self.pizzas = {0: MondayPizza(), 1: TuesdayPizza(), 2: WednesdayPizza(), 3: ThursdayPizza(),
                       4: FridayPizza(), 5: SaturdayPizza(), 6: SundayPizza}
        self.day = datetime.datetime.now().weekday()
        self.p = self.pizzas[self.day]
        self.food = {}
        for i in self.p.pizzaingred:
            self.food[i] = 1

    def make_order(self):
        print("Hello! Your pizza today:\n", self.p)
        print("Would you like add ingredients? -- Y(1)|N(0)")
        self.choice = int(input())
        if self.choice:
            self.add_ingredients()
        return f"---Total---\n"\
               f"{self.count_total()}"

    def add_ingredients(self):
        with open('pizzas.json', 'r') as p:
            data = json.load(p)
        print("Choose the option: ")
        for i in range(1, len(data["ingredients"]) + 1):
            if list(list(data["ingredients"].values())[i - 1].keys())[0] in list(self.food.keys()):
                print(i, data["ingredients"][str(i)])
        while self.choice:
            option = int(input())
            self.food[list(list(data["ingredients"].values())[option-1].keys())[0]] += 1
            print("Add something more? -- Y(1)|N(0)")
            self.choice = int(input())

    def count_total(self):
        total = 0
        with open('pizzas.json', 'r') as p:
            data = json.load(p)
        for i in range(1, len(data["ingredients"])+1):
            l = list(list(data["ingredients"].values())[i-1].keys())[0]
            if l in list(self.food.keys()):
                total += data["ingredients"][str(i)][l] * self.food[l]
        return total


"""if __name__ == "__main__":
    try:"""
c = Customer('Mary', 'Smith', '0987654321')
o = Order(c)
print(o.make_order())
"""    except Exception as ex:
        print(ex)"""

