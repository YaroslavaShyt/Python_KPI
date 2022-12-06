import pymysql.cursors
import re
import t1_abstract_classes as t


class Teacher(t.ITeacher):
    def __init__(self, id, name=None):
        self.id = id
        # got only id -> download teacher data from database
        if name is None:
            cur.execute("SELECT NAME FROM ITEACHER WHERE ID = %s", self.id)
            self.name = cur.fetchall()[0]['NAME']
        # got new teacher data -> insert it in database
        elif name is not None:
            self.check_exists_id()
            self.name = name
            cur.execute("INSERT INTO ITEACHER VALUES(%s, %s)", (self.id, self.name))

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

    def __str__(self):
        return f'ID: {self.id} \n' \
               f'Name: {self.name}\n'


class Course(t.ICourse):
    def __init__(self, id, title=None):
        self.course_id = id
        # got only course id -> download course from database
        if title is None:
            cur.execute("SELECT TITLE FROM ICOURSE WHERE ID = %s", self.course_id)
            self.course_name = cur.fetchall()[0]["TITLE"]
            self.course_programme = self.download_programme()
        # got new course data -> insert it in database
        elif title is not None:
            self.check_exists_id()
            self.course_name = title
            cur.execute("INSERT INTO ICOURSE VALUES(%s,%s,NULL, NULL)", (self.course_id, self.course_name))

    def check_exists_id(self):
        cur.execute("SELECT ID FROM ICOURSE")
        res = cur.fetchall()
        if any(self.course_id == i["ID"] for i in res):
            raise ValueError('This course id already exists!')

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

    def __str__(self):
        return f'ID: {self.course_id}\n' \
               f'Title: {self.course_name}:\n' \
               f'Course programme: {", ".join(i for i in self.course_programme)}\n'


class LocalCourse(Course, t.ILocalCourse):
    def __init__(self, id, title=None, lab=None,):
        super().__init__(id, title)
        # got course id -> download course lab data from db
        if lab is None:
            cur.execute("SELECT LAB FROM ICOURSE WHERE ID = %s", self.course_id)
            self.lab = cur.fetchall()[0]['LAB']
        # got course lab -> update course table in db
        elif lab is not None:
            self.lab = lab
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
               f'Lab: {self.lab}\n'


class OffsiteCourse(Course, t.IOffsiteCourse):
    def __init__(self, id, title=None, address=None):
        super().__init__(id, title)
        self.address = address
        # got course id -> download course address from db
        if self.address is None:
            cur.execute("SELECT ADDRESS FROM ICOURSE WHERE ID = %s", self.course_id)
            self.address = cur.fetchall()[0]['ADDRESS']
        # got course address -> update course table in db
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
               f'Address: {self.address}\n'


class CourseFactory(t.ICourseFactory):
    @staticmethod
    def add_teacher(id, name):
        return Teacher(id, name)

    @staticmethod
    def add_local_course(id, title, lab):
        return LocalCourse(id, title, lab)

    @staticmethod
    def add_offsite_course(id, address, title):
        return OffsiteCourse(id, address, title)

    @staticmethod
    def set_teacher_to_course(course_id, teacher_id):
        cur.execute("SELECT ID FROM ICOURSE")
        res = ' '.join(str(i['ID']) for i in cur.fetchall())
        if str(course_id) not in res:
            raise ValueError('Incorrect value for course id in list!')
        cur.execute("INSERT INTO ITEACH_TO_ICOURSE VALUES(%s, %s)", (teacher_id, course_id))
        connection.commit()

    @staticmethod
    def set_programme_to_course(course_id, programme):
        cur.execute("SELECT ID FROM TOPIC")
        res = ' '.join(str(i['ID']) for i in cur.fetchall())
        for i in programme:
            if str(i) not in res:
                raise ValueError('Incorrect value in list of programme\'s id!')
            cur.execute("INSERT INTO TOPIC_TO_ICOURSE VALUES(%s, %s)", (course_id, i))
            connection.commit()


try:
    connection = pymysql.connect(host='localhost',
                                 user='root',
                                 database='icourses',
                                 password='16012004',
                                 charset='utf8mb4',
                                 cursorclass=pymysql.cursors.DictCursor)
    cur = connection.cursor()
    f = CourseFactory()
    print(f.add_teacher(10, 'Павло'))
    print(f.add_local_course(7, 'Пайтон для роботи з WEB-технологіями', '#406'))
    f.set_programme_to_course(7, [1, 3, 5])
    f.set_teacher_to_course(7, 10)
    print(f.add_offsite_course(8, 'C', 'Австрія'))
    connection.close()
except Exception as ex:
    print(ex)
