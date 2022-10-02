class Rational:
    def __init__(self, num=1, den=1):
        self.__num = num // self.evklid(num, den)
        self.__den = den // self.evklid(num, den)
        self.start = True  # fractions initialized

    @property
    def num(self):
        return self.__num

    @property
    def den(self):
        return self.__den

    @num.setter
    def num(self, new_num):
        if self.check_values(new_num):
            self.__num = new_num
        else:
            print('Incorrect numerator value')
            self.start = False  # fractions weren't initialized

    @den.setter
    def den(self, new_den):
        if self.check_values(new_den) and new_den:
            self.__den = new_den
        else:
            print('Incorrect denominator value')
            self.start = False  # fractions weren't initialized

    @staticmethod
    def check_values(val):
        if isinstance(val, int):
            return True
        return False

    @staticmethod
    def evklid(a, b):
        while b != 0:
            a, b = b, a % b
        return a

    def show_fraction(self):
        if self.__den == 1:
            return str(self.__num)
        return str(self.__num // self.evklid(self.__num, self.__den)) + \
               '/' + str(self.__den // self.evklid(self.__num, self.__den))

    def show_float(self):
        return self.__num / self.__den

    def plus_frc(self, frac):
        return Rational(self.__num * frac.__den + self.__den * frac.__num, self.__den * frac.__den)

    def minus_frc(self, frac):
        return Rational(self.__num * frac.__den - self.__den * frac.__num, self.__den * frac.__den)

    def multip_frc(self, frac):
        return Rational(self.__num * frac.__num, self.__den * frac.__den)

    def divide_frc(self, frac):
        return Rational(self.__num * frac.__den, self.__den * frac.__num)


def main():
    r1 = Rational()
    r1.num, r1.den = 2, 5
    r2 = Rational()
    r2.num, r2.den = 3, 6
    if r1.start and r2.start:  # fractions initialized
        print('Fraction1:', r1.show_fraction(), 'Fraction2:', r2.show_fraction())
        print('Float1:', r1.show_float(), 'Float2:', r2.show_float())
        p = r1.plus_frc(r2)
        minus = r1.minus_frc(r2)
        mul = r1.multip_frc(r2)
        d = r1.divide_frc(r2)
        print('Plus:', p.show_fraction())
        print('Minus:', minus.show_fraction())
        print('Multiply:', mul.show_fraction())
        print('Divide:', d.show_fraction())


main()
