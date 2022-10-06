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
    def __init__(self, students=None, max_student=20):
        self.student_list = {}
        if len(students) > max_student:
            raise ValueError('Entered more students than required')
        elif not students:
            raise ValueError('Empty value!')
        for i in students:
            self.set_list(i)

    def get_list(self):
        return self.student_list

    def set_list(self, new_student):
        if new_student.__str__() in self.student_list:
            raise ValueError('Students must be unique!')
        self.student_list.update({new_student.__str__(): new_student.count_gpa()})

    def get_best(self):
        return sorted(list(self.get_list().values()), reverse=True)[:5]

    def show_best(self):
        for i in self.get_best():
            for j in self.student_list:
                if self.student_list[j] == i:
                    print(j, i)


def main():
    try:
        students = [Student('Mary', 'Smith', '0098', [4, 2, 5, 2, 3]),
                    Student('Kate', 'Williams', '0076', [2, 5, 4, 4, 3]),
                    Student('Bill', 'Abbie', '2874', [5, 5, 5, 5, 5]),
                    Student('Bob', 'Wazovsky', '2345', [3, 3, 4, 4]),
                    Student('Alex', 'White', '7624', [4, 4, 4, 5, 5]),
                    Student('Jake', 'Rawmen', '2635', [5, 5, 3, 2, 5]),
                    Student('Mike', 'Austin', '6666', [4, 3, 2, 2, 2])]
        g = Group(students)
        g.show_best()
    except Exception as ex:
        print(ex)


main()
