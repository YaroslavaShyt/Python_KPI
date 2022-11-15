import re


class Person:
    def __init__(self, surname, name, patr, birth, sex):
        self.surname = surname
        self.name = name
        self.patr = patr
        self.birth = birth
        self.sex = sex

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_n):
        if not isinstance(new_n, str):
            raise TypeError('Incorrect type for name!')
        elif re.search('[^A-Za-z\'-]', new_n):
            raise ValueError('Incorrect character in name!')
        self.__name = new_n

    @property
    def surname(self):
        return self.surname

    @surname.setter
    def surname(self, new_s):
        if not isinstance(new_s, str):
            raise TypeError('Incorrect type for surname!')
        elif re.search('[^A-Za-z\'-]', new_s):
            raise ValueError('Incorrect character in surname!')
        self.__surname = new_s

    @property
    def patr(self):
        return self.__patr

    @patr.setter
    def patr(self, new_p):
        if not isinstance(new_p, str):
            raise TypeError('Incorrect type for patronymic!')
        elif re.search('[^A-Za-z\']', new_p):
            raise ValueError('Incorrect character in surname!')
        self.__patr = new_p

    @property
    def birth(self):
        return self.__birth

    @birth.setter
    def birth(self, new_b):
        if not isinstance(new_b, str):
            raise TypeError('Incorrect type for date of birth!')
        elif re.search('[^0-9.]', new_b):
            raise ValueError('Incorrect character in date of birth!')
        self.__birth = new_b

    @property
    def sex(self):
        return self.__sex

    @sex.setter
    def sex(self, new_s):
        if not isinstance(new_s, str):
            raise TypeError('Incorrect type for sex!')
        elif new_s not in ('female', 'male', 'f', 'm'):
            raise ValueError('Incorrect value for sex')
        self.__sex = new_s


class Employee(Person):
    def __init__(self,  surname, name, patr, birth, sex, organization, speciality, position, salary, experience):
        super().__init__(surname, name, patr, birth, sex)
        self.organization = organization
        self.speciality = speciality
        self.position = position
        self.salary = salary
        self.experience = experience


class Organization:
    def __init__(self,  value=5,):
        self.employees = []
        self.is_bigger = []
        self.value = value
        self.index = 0
        self.num = 0

    def __str__(self):
        return '\n'.join(map(lambda item: f'{item[0]} - {item[1]}', zip(self.employees, self.is_bigger)))

    def add_empl(self, new_e):
        self.employees.append(new_e)
        if new_e.experience > self.value:
            self.is_bigger.append('+')
        else:
            self.is_bigger.append('-')

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, new_v):
        if not isinstance(new_v, int):
            raise TypeError('Incorrect type for value!')
        elif new_v <= 0:
            raise ValueError('Incorrect value for value')
        self.__value = new_v

    def __iter__(self):
        self.index = 0
        return self

    def __next__(self):
        if self.index < len(self.employees):
            self.index += 1
            return self.employees[self.index - 1], self.is_bigger[self.index - 1]
        raise StopIteration()


lst = [Employee('Gonh', 'Kik', 'Lol', '12.02.1977', 'male', 'Abobas', 'Cheff', 'Cheff', 12000, 15),
       Employee('Gog', 'Van', 'Gogovich', '01.02.1988', 'male', 'Abobas', 'Painert', 'Painert', 300, 2),
       Employee('Assas', 'As', 'We', '08.10.1990', 'female', 'Abobas', 'Nothing', 'Nothing', 29000, 4)]

o = Organization()

for item in lst:
    o.add_empl(item)

for employee, condition in o:
    print(employee, condition)


