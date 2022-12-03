import pymysql.cursors
import re
import t1_abstract_classes as t


class Teacher(t.ITeacher):
    def __init__(self, id, name=None, courses=None):
        self.id = id
        self.name = name
        if name is None and courses is None:
            cur.execute("SELECT NAME FROM ITEACHER WHERE ID = %s", self.id)
            self.name = cur.fetchall()[0]['NAME']
        elif name is not None and courses is not None:
            self.check_exists_id()
            cur.execute("INSERT INTO ITEACHER VALUES(%s, %s)", (self.id, self.name))
            self.set_course_to_teacher(courses)
        self.courses_lst = self.download_teacher_course()

    def set_course_to_teacher(self, courses):
        if not isinstance(courses, list):
            raise TypeError('Incorrect type for list of courses\' id!')
        cur.execute("SELECT ID FROM ICOURSE")
        res = ' '.join(str(i['ID']) for i in cur.fetchall())
        for i in courses:
            if str(i) not in res:
                raise ValueError('Incorrect value for course id in list!')
            cur.execute("INSERT INTO ITEACH_TO_ICOURSE VALUES(%s, %s)", (self.id, i))
            connection.commit()

    def check_exists_id(self):
        cur.execute("SELECT ID FROM ITEACHER")
        res = cur.fetchall()
        if any(self.id == i["ID"] for i in res):
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
        if not isinstance(new_n, str | None):
            raise TypeError('Incorrect type for teacher name!')
        elif new_n is not None and re.search('[^а-щА-ЩЬьЮюЯяЇїІіЄєҐґ\'-]', new_n):
            raise ValueError('Incorrect value for teacher name!')
        self.__name = new_n

    def download_teacher_course(self):
        courses_lst = []
        courses = "SELECT TITLE FROM ICOURSE \
                   INNER JOIN ITEACH_TO_ICOURSE ON ICOURSE.ID = ITEACH_TO_ICOURSE.ID_C \
                   INNER JOIN ITEACHER ON ITEACH_TO_ICOURSE.ID_T = ITEACHER.ID\
                   WHERE ITEACH_TO_ICOURSE.ID_T = %s"
        cur.execute(courses, self.id)
        result = cur.fetchall()
        for i in result:
            courses_lst.append(i['TITLE'])
        return courses_lst

    def __str__(self):
        return f'ID: {self.id} \n' \
               f'Name: {self.name}\n' \
               f'Courses: {", ".join(i for i in self.courses_lst)}\n'


class Course(t.ICourse):
    def __init__(self, id, title=None, programme=None, teachers=None):
        self.course_id = id
        self.course_name = title
        if title is None and programme is None and teachers is None:
            cur.execute("SELECT TITLE FROM ICOURSE WHERE ID = %s", self.course_id)
            self.course_name = cur.fetchall()[0]["TITLE"]
        elif title is not None and programme is not None and teachers is not None:
            self.check_exists_id()
            cur.execute("INSERT INTO ICOURSE VALUES(%s,%s,NULL, NULL)", (self.course_id, self.course_name))
            self.set_programme_to_course(programme)
            self.set_teacher_to_course(teachers)
        self.course_programme = self.download_programme()
        self.course_teachers = self.download_teachers()

    def check_exists_id(self):
        cur.execute("SELECT ID FROM ICOURSE")
        res = cur.fetchall()
        if any(self.course_id == i["ID"] for i in res):
            raise ValueError('This course id already exists!')

    def set_teacher_to_course(self, teachers):
        if not isinstance(teachers, list):
            raise TypeError('Incorrect type for list of teacher\'s id!')
        cur.execute("SELECT ID FROM ITEACHER")
        res = ' '.join(str(i['ID']) for i in cur.fetchall())
        for i in teachers:
            if str(i) not in res:
                raise ValueError('Incorrect value in list of teacher\'s id!')
            cur.execute("INSERT INTO ITEACH_TO_ICOURSE VALUES(%s, %s)", (i, self.course_id))
            connection.commit()

    def set_programme_to_course(self, programme):
        if not isinstance(programme, list):
            raise TypeError('Incorrect type for list of programme\'s id!')
        cur.execute("SELECT ID FROM TOPIC")
        res = ' '.join(str(i['ID']) for i in cur.fetchall())
        for i in programme:
            if str(i) not in res:
                raise ValueError('Incorrect value in list of programme\'s id!')
            cur.execute("INSERT INTO TOPIC_TO_ICOURSE VALUES(%s, %s)", (self.course_id, i))
            connection.commit()

    @property
    def course_id(self):
        return self.__course_id

    @course_id.setter
    def course_id(self, new_id):
        if not isinstance(new_id, int):
            raise TypeError('Incorrect data type for course id!')
        elif not new_id:
            raise ValueError('Incorrect value for course id!')
        self.__course_id = new_id

    @property
    def course_name(self):
        return self.__course_name

    @course_name.setter
    def course_name(self, new_n):
        if not isinstance(new_n, str | None):
            raise TypeError('Incorrect type for course name!')
        elif new_n is not None and re.search(r'[^a-zA-Zа-щА-ЩЬьЮюЯяЇїІіЄєҐґ\s\'-]', new_n):
            raise ValueError('Incorrect value for course name!')
        self.__course_name = new_n

    def download_programme(self):
        programme_lst = []
        programme = "SELECT TOPIC.TITLE FROM TOPIC \
                     INNER JOIN TOPIC_TO_ICOURSE ON TOPIC.ID = TOPIC_TO_ICOURSE.T_ID\
                     INNER JOIN ICOURSE ON ICOURSE.ID = TOPIC_TO_ICOURSE.C_ID\
                     WHERE C_ID = %s"
        cur.execute(programme, self.course_id)
        result1 = cur.fetchall()
        for i in result1:
            programme_lst.append(i['TITLE'])
        return programme_lst

    def download_teachers(self):
        teacher_lst = []
        teacher = "SELECT NAME FROM ITEACHER  \
                   INNER JOIN ITEACH_TO_ICOURSE ON ITEACH_TO_ICOURSE.ID_T = ITEACHER.ID  \
                   INNER JOIN ICOURSE on ITEACH_TO_ICOURSE.ID_C = ICOURSE.ID \
                   WHERE ICOURSE.ID = %s"
        cur.execute(teacher, self.course_id)
        result1 = cur.fetchall()
        for i in result1:
            teacher_lst.append(i['NAME'])
        return teacher_lst

    def __str__(self):
        return f'ID: {self.course_id}\n' \
               f'Title: {self.course_name}:\n' \
               f'Course programme: {", ".join(i for i in self.course_programme)}\n' \
               f'Course teachers: {", ".join(i for i in self.course_teachers)}\n'


class LocalCourse(Course, t.ILocalCourse):
    def __init__(self, id, title=None, programme=None, teachers=None, lab=None,):
        super().__init__(id, title, programme, teachers)
        self.lab = lab
        if self.lab is None:
            cur.execute("SELECT LAB FROM ICOURSE WHERE ID = %s", self.course_id)
            self.lab = cur.fetchall()[0]['LAB']
        elif self.lab is not None:
            cur.execute("UPDATE ICOURSE SET LAB = %s WHERE ID = %s", (self.lab, self.course_id))
            connection.commit()

    @property
    def lab(self):
        return self.__lab

    @lab.setter
    def lab(self, new_l):
        if not isinstance(new_l, str | None):
            raise TypeError('Incorrect data type for lab')
        elif new_l is not None and not new_l:
            raise ValueError('Incorrect value for lab')
        self.__lab = new_l

    def __str__(self):
        return f'ID: {self.course_id}\n' \
               f'Title: {self.course_name}:\n' \
               f'Course programme: {", ".join(i for i in self.course_programme)}\n' \
               f'Course teachers: {", ".join(i for i in self.course_teachers)}\n' \
               f'Lab: {self.lab}\n'


class OffsiteCourse(Course, t.IOffsiteCourse):
    def __init__(self, id, title=None, programme=None, teachers=None, address=None):
        super().__init__(id, title, programme, teachers)
        self.address = address
        if self.address is None:
            cur.execute("SELECT ADDRESS FROM ICOURSE WHERE ID = %s", self.course_id)
            self.address = cur.fetchall()[0]['ADDRESS']
        elif self.address is not None:
            cur.execute("UPDATE ICOURSE SET ADDRESS = %s WHERE ID = %s",  (self.address, self.course_id))
            connection.commit()

    @property
    def address(self):
        return self.__address

    @address.setter
    def address(self, new_a):
        if not isinstance(new_a, str | None):
            raise TypeError('Incorrect data type for address!')
        elif new_a is not None and re.search(r'[^0-9\sа-щА-ЩЬьЮюЯяЇїІіЄєҐґ]', new_a):
            raise ValueError('Incorrect value for address!!')
        self.__address = new_a

    def __str__(self):
        return f'ID: {self.course_id}\n' \
               f'Title: {self.course_name}:\n' \
               f'Course programme: {", ".join(i for i in self.course_programme)}\n' \
               f'Course teachers: {", ".join(i for i in self.course_teachers)}\n' \
               f'Address: {self.address}\n'


class CourseFactory(t.ICourseFactory):
    @staticmethod
    def add_teacher(id, name, courses):
        return Teacher(id, name, courses)

    @staticmethod
    def see_all_teachers():
        cur.execute("SELECT ID FROM ITEACHER")
        res = cur.fetchall()
        for i in res:
            print(Teacher(i["ID"]))

    @staticmethod
    def add_local_course(id, title, programme, teachers, lab):
        return LocalCourse(id, title, programme, teachers, lab)

    @staticmethod
    def add_offsite_course(id, address, title, programme, teachers):
        return OffsiteCourse(id, address, title, programme, teachers)

    @staticmethod
    def see_all_courses():
        query = "SELECT ID, LAB, ADDRESS FROM ICOURSE"
        cur.execute(query)
        res = cur.fetchall()
        for i in res:
            if i["ADDRESS"] == 'NULL':
                print(LocalCourse(i["ID"]))
            else:
                print(OffsiteCourse(i["ID"]))


try:
    connection = pymysql.connect(host='localhost',
                                 user='root',
                                 database='icourses',
                                 password='16012004',
                                 charset='utf8mb4',
                                 cursorclass=pymysql.cursors.DictCursor)
    cur = connection.cursor()
    f = CourseFactory()
    f.see_all_courses()
    f.see_all_teachers()
    print(f.add_teacher(9, 'Марина', [1, 4]))
    print(f.add_local_course(5, 'Основи програмування на Java', [1], [3, 6], '#404'))
    print(f.add_offsite_course(6, 'Python and SQL for beginners', [1, 3, 5, 9, 10], [2, 5], 'Німеччина'))
    connection.close()
except Exception as ex:
    print(ex)
