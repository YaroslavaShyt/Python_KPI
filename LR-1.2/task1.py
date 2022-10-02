class Rectangle:
    def __init__(self, length=1.0, width=1.0):
        self._length = length
        self._width = width

    @property
    def length(self):
        return self._length

    @property
    def width(self):
        return self._width

    @length.setter
    def length(self, new_length):
        if self.check_value(new_length):
            self._length = new_length
        else:
            print('Wrong length value')

    @width.setter
    def width(self, new_width):
        if self.check_value(new_width):
            self._width = new_width
        else:
            print('Wrong width value')

    @staticmethod
    def check_value(num):
        if isinstance(num, float) and 0.0 < num <= 20.0:
            return True
        return False

    def area(self):
        return self._length * self._width

    def perimeter(self):
        return 2 * (self._length + self._width)


def main():
    rec = Rectangle()
    print('w=', rec.width, 'l=', rec.length)
    rec.width, rec.length = 12.0, 4.0
    print('w=', rec.width, 'l=', rec.length)
    rec.width, rec.length = '1', 'mom'
    print('w=', rec.width, 'l=', rec.length)
    print(rec.area(), rec.perimeter())


main()
