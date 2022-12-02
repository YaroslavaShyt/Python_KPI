import pymysql.cursors
import re
import t1_abstract_classes as t


class Teacher(t.ITeacher):
    def __init__(self, curs, id, name=None, courses=None):
        self.cursor = curs
        self.id = id
        if name is None and courses is None:
            name = "SELECT NAME FROM ITEACHER WHERE ID = %s"
            self.cursor.execute(name, self.id)
            name = self.cursor.fetchall()[0]['NAME']
        elif name is not None and courses is not None:
            self.check_exists_id()
            n_teacher = "INSERT INTO ITEACHER VALUES(%s, %s)"
            self.cursor.execute(n_teacher, (self.id, self.name))
            self.set_course_to_teacher(courses)
        self.name = name
        self.courses_lst = self.download_teacher_course()

    def set_course_to_teacher(self, courses):
        for i in courses:
            query = "INSERT INTO ITEACH_TO_ICOURSE VALUES(%s, %s)"
            self.cursor.execute(query, (self.id, i))
            connection.commit()

    def check_exists_id(self):
        query = "SELECT ID FROM ITEACHER"
        self.cursor.execute(query)
        res = self.cursor.fetchall()
        for i in res:
            if self.id == i["ID"]:
                raise ValueError('This teacher id already exists!')

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, new_id):
        if not isinstance(new_id, int):
            raise TypeError('Incorrect type for teacher id!')
        elif not id:
            raise ValueError('Incorrect value for teacher id!')
        self.__id = new_id

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_n):
        if not isinstance(new_n, str):
            raise TypeError('Incorrect type for teacher name!')
        elif re.search('[^а-щА-ЩЬьЮюЯяЇїІіЄєҐґ\'-]', new_n):
            raise ValueError('Incorrect value for teacher name!')
        self.__name = new_n

    def download_teacher_course(self):
        courses_lst = []
        courses = "SELECT TITLE FROM ICOURSE \
                   INNER JOIN ITEACH_TO_ICOURSE ON ICOURSE.ID = ITEACH_TO_ICOURSE.ID_C \
                   INNER JOIN ITEACHER ON ITEACH_TO_ICOURSE.ID_T = ITEACHER.ID\
                   WHERE ITEACH_TO_ICOURSE.ID_T = %s"
        self.cursor.execute(courses, self.id)
        result = self.cursor.fetchall()
        for i in result:
            courses_lst.append(i['TITLE'])
        return courses_lst

    def __str__(self):
        return f'ID: {self.id} \n' \
               f'Name: {self.name}\n' \
               f'Courses: {", ".join(i for i in self.courses_lst)}\n'


class Course(t.ICourse):
    def __init__(self, curs, id, title=None, programme=None, teachers=None):
        self.cursor = curs
        self.course_id = id
        if title is None and programme is None and teachers is None:
            title = "SELECT TITLE FROM ICOURSE WHERE ID = %s"
            self.cursor.execute(title, self.course_id)
            title = self.cursor.fetchall()[0]["TITLE"]
        elif title is not None and programme is not None and teachers is not None:
            self.check_exists_id()
            self.set_programme_to_course(programme)
            self.set_teacher_to_course(teachers)
        self.course_name = title
        self.course_programme = self.download_programme()
        self.course_teachers = self.download_teachers()

    def check_exists_id(self):
        query = "SELECT ID FROM ICOURSE"
        self.cursor.execute(query)
        res = self.cursor.fetchall()
        for i in res:
            if self.course_id == i["ID"]:
                raise ValueError('This teacher id already exists!')

    def set_teacher_to_course(self, teachers):
        for i in teachers:
            query = "INSERT INTO ITEACH_TO_ICOURSE VALUES(%s, %s)"
            self.cursor.execute(query, (i, self.course_id))
            connection.commit()

    def set_programme_to_course(self, programme):
        for i in programme:
            query = "INSERT INTO TOPIC_TO_ICOURSE VALUES(%s, %s)"
            self.cursor.execute(query, (self.course_id, i))
            connection.commit()

    @property
    def course_id(self):
        return self.__course_id

    @course_id.setter
    def course_id(self, new_id):
        if not isinstance(new_id, int):
            raise TypeError('Неправильний тип даних для id курсу!')
        elif not new_id:
            raise ValueError('Некоректне значення для id курсу!')
        self.__course_id = new_id

    @property
    def course_name(self):
        return self.__course_name

    @course_name.setter
    def course_name(self, new_n):
        if not isinstance(new_n, str):
            raise TypeError('Incorrect type for course name!')
        elif re.search(r'[^a-zA-Zа-щА-ЩЬьЮюЯяЇїІіЄєҐґ\s\'-]', new_n):
            raise ValueError('Incorrect value for course name!')
        self.__course_name = new_n

    def download_programme(self):
        programme_lst = []
        programme = "SELECT TOPIC.TITLE FROM TOPIC \
                     INNER JOIN TOPIC_TO_ICOURSE ON TOPIC.ID = TOPIC_TO_ICOURSE.T_ID\
                     INNER JOIN ICOURSE ON ICOURSE.ID = TOPIC_TO_ICOURSE.C_ID\
                     WHERE C_ID = %s"
        self.cursor.execute(programme, self.course_id)
        result1 = self.cursor.fetchall()
        for i in result1:
            programme_lst.append(i['TITLE'])
        return programme_lst

    def download_teachers(self):
        teacher_lst = []
        teacher = "SELECT NAME FROM ITEACHER  \
                   INNER JOIN ITEACH_TO_ICOURSE ON ITEACH_TO_ICOURSE.ID_T = ITEACHER.ID  \
                   INNER JOIN ICOURSE on ITEACH_TO_ICOURSE.ID_C = ICOURSE.ID \
                   WHERE ICOURSE.ID = %s"
        self.cursor.execute(teacher, self.course_id)
        result1 = self.cursor.fetchall()
        for i in result1:
            teacher_lst.append(i['NAME'])
        return teacher_lst

    def __str__(self):
        return f'ID: {self.course_id}\n' \
               f'Title: {self.course_name}:\n' \
               f'Course programme: {", ".join(i for i in self.course_programme)}\n' \
               f'Course teachers: {", ".join(i for i in self.course_teachers)}\n'


class LocalCourse(Course, t.ILocalCourse):
    def __init__(self, curs, id, lab=None, title=None, programme=None, teachers=None):
        super().__init__(curs, id, title=None, programme=None, teachers=None)
        self.lab = lab
        if self.lab is None:
            lab = "SELECT LAB FROM ICOURSE WHERE ID = %s"
            self.cursor.execute(lab, self.course_id)
            self.lab = self.cursor.fetchall()[0]['LAB']
        elif lab is not None:
            query = "INSERT INTO ICOURSE VALUES(%s, %s, NULL, %s)"
            self.cursor.execute(query, self.course_id, self.course_name, self.lab)

    @property
    def lab(self):
        return self.__lab

    @lab.setter
    def lab(self, new_l):
        if not isinstance(new_l, str | None):
            raise TypeError('Неправильний тип даних для назви лабораторії!')
        elif new_l is not None and not new_l:
            raise ValueError('Назва лабораторії не може бути пустою!')
        self.__lab = new_l

    def __str__(self):
        return f'ID: {self.course_id}\n' \
               f'Title: {self.course_name}:\n' \
               f'Course programme: {", ".join(i for i in self.course_programme)}\n' \
               f'Course teachers: {", ".join(i for i in self.course_teachers)}\n' \
               f'Lab: {self.lab}\n'


class OffsiteCourse(Course, t.IOffsiteCourse):
    def __init__(self, curs, id, address=None, title=None, programme=None, teachers=None):
        super().__init__(curs, id, title=None, programme=None, teachers=None)
        self.address = address
        if self.address is None:
            address = "SELECT ADDRESS FROM ICOURSE WHERE ID = %s"
            self.cursor.execute(address, self.course_id)
            self.address = self.cursor.fetchall()[0]['ADDRESS']
        elif self.address is not None:
            query = "INSERT INTO ICOURSE VALUES(%s, %s, %s, NULL)"
            self.cursor.execute(query, self.course_id, self.course_name, self.address)

    @property
    def address(self):
        return self.__address

    @address.setter
    def address(self, new_a):
        if not isinstance(new_a, str | None):
            raise TypeError('Неправильний тип даних для адреси курсу!')
        elif new_a is not None and re.search(r'[^0-9\sа-щА-ЩЬьЮюЯяЇїІіЄєҐґ]', new_a):
            raise ValueError('Некоректне значення для адреси курсу!')
        self.__address = new_a

    def __str__(self):
        return f'ID: {self.course_id}\n' \
               f'Title: {self.course_name}:\n' \
               f'Course programme: {", ".join(i for i in self.course_programme)}\n' \
               f'Course teachers: {", ".join(i for i in self.course_teachers)}\n' \
               f'Address: {self.address}\n'


class CourseFactory(t.ICourseFactory):
    @staticmethod
    def add_teacher(curs, id, name, courses):
        return Teacher(curs, id, name, courses)

    @staticmethod
    def see_all_teachers(curs):
        query = "SELECT ID FROM ITEACHER"
        curs.execute(query)
        res = curs.fetchall()
        for i in res:
            print(Teacher(curs, i["ID"]))

    @staticmethod
    def add_local_course(curs, id, title, programme, teachers, lab):
        return LocalCourse(curs, id, title, programme, teachers, lab)

    @staticmethod
    def add_offsite_course(curs, id, address, title, programme, teachers):
        return OffsiteCourse(curs, id, address, title, programme, teachers)

    @staticmethod
    def see_all_courses(curs):
        query = "SELECT ID, LAB, ADDRESS FROM ICOURSE"
        curs.execute(query)
        res = curs.fetchall()
        for i in res:
            if i["ADDRESS"] == 'NULL':
                print(LocalCourse(curs, i["ID"]))
            else:
                print(OffsiteCourse(curs, i["ID"]))


# try:
connection = pymysql.connect(host='localhost',
                             user='root',
                             database='icourses',
                             password='16012004',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)
cur = connection.cursor()
f = CourseFactory()
f.see_all_courses(cur)
#f.see_all_teachers(cur)
# print(f.add_teacher(cur, 9, 'Марина', [1, 4]))
# print(t)
connection.close()
# except Exception as ex:
# print(ex)


