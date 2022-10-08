class Rectangle:
    def __init__(self, length=1, width=1):
        self.width = width
        self.length = length

    @property
    def length(self):
        return self.__length

    @property
    def width(self):
        return self.__width

    @length.setter
    def length(self, new_length):
        if self.check_value(new_length):
            self.__length = new_length

    @width.setter
    def width(self, new_width):
        if self.check_value(new_width):
            self.__width = new_width

    @staticmethod
    def check_value(num):
        if not isinstance(num, float | int):
            raise TypeError('Incorrect value!')
        elif num <= 0 or num > 20:
            raise ValueError('Values must belong (0;20)!')
        return True

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)


def main():
    try:
        rec = Rectangle()
        print('w=', rec.width, 'l=', rec.length)
        rec.width, rec.length = 12.0, 4.0
        print('w=', rec.width, 'l=', rec.length)
        print('S=', rec.area(), 'P=', rec.perimeter())
    except Exception as ex:
        print(ex)


main()
