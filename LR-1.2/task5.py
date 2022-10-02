class Student:
    def __init__(self, name='', surname='', studbook='', marks=''):
        self.__name = name
        self.__surname = surname
        self.__studbook = studbook
        self.__marks = marks

    def count_gpa(self):
        suma = 0
        mark_list = self.__marks.split(' ')
        for i in mark_list:
            suma += int(i)
        return suma

    def __str__(self):
        return f'{self.__name} {self.__surname}'


class Group:
    def __init__(self):
        self.__student_list = {}

    @property
    def student_list(self):
        return self.__student_list

    @student_list.setter
    def student_list(self, new_student):
        if new_student.__str__() in self.__student_list:
            print(new_student.__str__(), ' - Have one already')
        else:
            self.__student_list.update({new_student.__str__(): new_student.count_gpa()})

    def show_best(self):
        new_list = sorted(list(self.student_list.values()), reverse=True)[:5]
        for i in new_list:
            for j in self.student_list:
                if self.student_list[j] == i:
                    print(j, i)


def main():
    s1 = Student('Mary', 'Smith', '0098', '4 2 5 2 3')
    s2 = Student('Kate', 'Williams', '0076', '2 5 4 4 3')
    s3 = Student('Bill', 'Abbie', '2874', '5 5 5 5 5')
    s4 = Student('Bob', 'Wazovsky', '2345', '3 3 4 4')
    s5 = Student('Alex', 'White', '7624', '4 4 4 5 5')
    s6 = Student('Jake', 'Rawmen', '2635', '5 5 3 2 5')
    s7 = Student('Mike', 'Austin', '6666', '4 3 2 2 2')
    g = Group()
    g.student_list = s1   # check if the student in list
    g.student_list = s2
    g.student_list = s3
    g.student_list = s4
    g.student_list = s5
    g.student_list = s6
    g.student_list = s7
    g.show_best()


main()
