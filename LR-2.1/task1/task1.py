import re


class Customer:
    def __int__(self, surn, name, phone, email):
        self.surname = surn
        self.name = name
        self.phone = phone
        self.email = email

    @property
    def surname(self):
        return self.__surname

    @surname.setter
    def surname(self, new_surn):
        if not isinstance(new_surn, str):
            raise TypeError('Incorrect type for surname!')
        if not new_surn:
            raise ValueError('Surname cannot be empty!')
        self.__surname = new_surn

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        if not isinstance(new_name, str):
            raise TypeError('Incorrect type for surname!')
        if not new_name:
            raise ValueError('Surname cannot be empty!')
        self.__name = new_name

    @property
    def phone(self):
        return self.__phone
# переробити
    @phone.setter
    def phone(self, new_phone):
        for i in new_phone:
            if not isinstance(i, int):
                raise TypeError('Incorrect type for telephone number!')
        self.__phone = new_phone

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, new_email):
        if not re.search(r'\S+@\S+.\S+'):
            raise ValueError('Incorrect email address!')
        self.__email = new_email

    def __str__(self):
        return f'Surname:{self.surname}\nName:{self.name}\nTelephone number:{self.phone}\nEmail:{self.email}'


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


