class Student:
    def __init__(self, name='', surname='', studbook='', marks=None):
        self.name = name
        self.surname = surname
        self.studbook = studbook
        self.marks = marks

    def count_gpa(self):
        return sum(self.marks)

    def __str__(self):
        return f'{self.name} {self.surname}'


class Group:
    def __init__(self, **students):
        self.student_list = {}
        for i in students:
            self.set_list(students[i])

    def get_list(self):
        return self.student_list

    def set_list(self, new_student):
        if new_student.__str__() in self.student_list:
            raise ValueError('Students must be unique!')
        else:
            self.student_list.update({new_student.__str__(): new_student.count_gpa()})

    def get_best(self):
        return sorted(list(self.get_list().values()), reverse=True)[:5]


def show_best(group):
    for i in group.get_best():
        for j in group.student_list:
            if group.student_list[j] == i:
                print(j, i)


def main():
    try:
        s1 = Student('Mary', 'Smith', '0098', [4, 2, 5, 2, 3])
        s2 = Student('Kate', 'Williams', '0076', [2, 5, 4, 4, 3])
        s3 = Student('Bill', 'Abbie', '2874', [5, 5, 5, 5, 5])
        s4 = Student('Bob', 'Wazovsky', '2345', [3, 3, 4, 4])
        s5 = Student('Alex', 'White', '7624', [4, 4, 4, 5, 5])
        s6 = Student('Jake', 'Rawmen', '2635', [5, 5, 3, 2, 5])
        s7 = Student('Mike', 'Austin', '6666', [4, 3, 2, 2, 2])
        g = Group(st1=s1, st2=s2, st3=s3, st4=s4, st5=s5, st6=s6, st7=s7)
        show_best(g)
    except Exception as ex:
        print(ex)


main()
