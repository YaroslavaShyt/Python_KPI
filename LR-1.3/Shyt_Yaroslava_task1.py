class Person:
    def __init__(self, surname='', initials='', family=None, date=''):
        self.surname = surname
        self.initials = initials
        self.family = family
        self.date = date

    def get_date(self):
        return self.date

    def __str__(self):
        return f'{self.surname} {self.initials}'


class Queue:
    def __init__(self, people=None):
        self.number = 1
        self.people = people
        self.data = {}
        for i in people:
            self.add(i)

    def add(self, new_person):
        if new_person.__str__() in self.data:
            raise ValueError('This person already exists!')
        self.data[self.number] = new_person.__str__()
        self.number += 1

    def delete(self):
        if not len(self.data):
            raise ValueError('No data!')
        self.number -= 1
        del self.data[self.number]

    def show(self):
        print(self.data)

    def num_search(self, num):
        if num not in self.data.keys():
            raise ValueError('No person with this number!')
        return self.data[num]

    def surname_search(self, surn):
        for i in self.people:
            if i.surname == surn:
                print(surn, i.initials)

    def data_search(self, date):
        for i in self.people:
            if i.date == date:
                print(i.date, i.surname, i.initials)


try:
    p = [Person('Petrenko', 'K. L.', ['mom', 'dad'], '18.10'),
         Person('Alibaba', 'J. D.', ['wife', 'child1', 'child2'], '17.10'),
         Person('Shreck', 'P.M.', ['wife'], '19.10'),
         Person('Squidward', 'R. G.', ['-'], '19.10')]
    q = Queue(p)
    q.show()
    q.delete()
    q.show()
    print(q.num_search(2))
    q.surname_search('Alibaba')
    q.data_search('19.10')
except Exception as ex:
    print(ex)


