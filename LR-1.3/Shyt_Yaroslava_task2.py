class Time:
    def __init__(self, hour, minute, second):
        self.hour = hour
        self.minute = minute
        self.second = second

    @property
    def hour(self):
        return self.__hour

    @hour.setter
    def hour(self, new_hour):
        if not isinstance(new_hour, int):
            raise TypeError('Incorrect type')
        elif new_hour < 0 or new_hour > 23:
            raise ValueError('Incorrect value!')
        self.__hour = new_hour

    @property
    def minute(self):
        return self.__minute

    @minute.setter
    def minute(self, new_min):
        if not isinstance(new_min, int):
            raise TypeError('Incorrect type')
        elif new_min < 0 or new_min > 60:
            raise ValueError('Incorrect value!')
        self.__minute = new_min

    @property
    def second(self):
        return self.__second

    @second.setter
    def second(self, new_sec):
        if not isinstance(new_sec, int):
            raise TypeError('Incorrect type')
        elif new_sec < 0 or new_sec > 60:
            raise ValueError('Incorrect value!')
        self.__second = new_sec

    def __str__(self):
        return f'{self.hour}:{self.minute}:{self.second}'

    def add_hour(self):
        if self.hour == 23:
            self.hour = 0
        else:
            self.hour += 1

    def add_minute(self):
        if self.minute == 60:
            self.minute = 0
        else:
            self.minute += 1

    def add_second(self):
        if self.second == 60:
            self.second = 0
        else:
            self.second += 1

    def clock(self):
        while 1:
            while self.second < 60:
                self.add_second()
                print(self.__str__())
            self.add_minute()
            self.add_second()
            print(self.__str__())
            if self.minute == 60:
                self.add_hour()
                print(self.__str__())


try:
    t = Time(0, 0, 0)
    t.clock()
except Exception as ex:
    print(ex)
