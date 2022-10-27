import re


class Customer:
    def __init__(self, name, surname, phone, email):
        self.name = name
        self.surname = surname
        self.phone = phone
        self.email = email

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

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, new_e):
        if not isinstance(new_e, str):
            raise TypeError("Incorrect type for email!")
        if not re.search(r'[\S+@a-z.a-z]', new_e):
            raise ValueError("Invalid email!")
        self.__email = new_e

    def __str__(self):
        return f'--------CUSTOMER--------\n' \
               f'Name: {self.name}\n' \
               f'Surname: {self.surname}\n' \
               f'Phone number: {self.phone}\n' \
               f'Email: {self.email}'


class RegularTicket:
    def __init__(self, num, price):
        self.data = {}
        self.number = num
        self.price = price


class AdvancedTicket(RegularTicket):
    def get_price(self):
        return self.price * 0.6


class StudentTicket(RegularTicket):
    def get_price(self):
        return self.price * 1.1


class LateTicket(RegularTicket):
    def get_price(self):
        return self.price / 2


try:
    c = Customer('Petro', 'Petrenko', '098765432', 'petpet@gmail.com')
except Exception as ex:
    print(ex)
