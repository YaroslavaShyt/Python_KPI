from abc import abstractmethod, ABC


class ITeacher(ABC):
    @property
    @abstractmethod
    def id(self):
        pass

    @id.setter
    @abstractmethod
    def id(self, new_id):
        pass

    @property
    @abstractmethod
    def name(self):
        pass

    @name.setter
    @abstractmethod
    def name(self, new_n):
        pass

    @abstractmethod
    def download_teacher_course(self):
        pass

    @abstractmethod
    def check_exists_id(self):
        pass

    @abstractmethod
    def set_course_to_teacher(self, courses):
        pass

    @abstractmethod
    def __str__(self):
        pass


class ICourse(ABC):
    @property
    @abstractmethod
    def course_name(self):
        pass

    @course_name.setter
    @abstractmethod
    def course_name(self, new_n):
        pass

    @property
    @abstractmethod
    def course_id(self):
        pass

    @course_id.setter
    @abstractmethod
    def course_id(self, new_id):
        pass

    @abstractmethod
    def download_programme(self):
        pass

    @abstractmethod
    def download_teachers(self):
        pass

    @abstractmethod
    def check_exists_id(self):
        pass

    @abstractmethod
    def set_teacher_to_course(self, teachers):
        pass

    @abstractmethod
    def set_programme_to_course(self, programme):
        pass

    @abstractmethod
    def __str__(self):
        pass


class ILocalCourse(ABC):
    @property
    @abstractmethod
    def lab(self):
        pass

    @lab.setter
    @abstractmethod
    def lab(self, value):
        pass


class IOffsiteCourse(ABC):
    @property
    @abstractmethod
    def address(self):
        pass

    @address.setter
    @abstractmethod
    def address(self, value):
        pass

    @abstractmethod
    def __str__(self):
        pass


class ICourseFactory(ABC):
    @staticmethod
    @abstractmethod
    def add_teacher(curs, id, name, courses):
        pass

    @staticmethod
    @abstractmethod
    def add_local_course(curs, id, lab, title, programme, teachers):
        pass

    @staticmethod
    @abstractmethod
    def add_offsite_course(curs, id, address, title, programme, teachers):
        pass

    @staticmethod
    @abstractmethod
    def see_all_teachers(curs):
        pass

    @staticmethod
    @abstractmethod
    def see_all_courses(curs):
        pass
