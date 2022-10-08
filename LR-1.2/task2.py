import math


class Rational:
    def __init__(self, num=1, den=1):
        self.num = num
        self.den = den

    @property
    def num(self):
        return self.__num

    @property
    def den(self):
        return self.__den

    @num.setter
    def num(self, new_num):
        if not isinstance(new_num, int):
            raise TypeError('Incorrect value for numerator!')
        self.__num = new_num

    @den.setter
    def den(self, new_den):
        if new_den == 0:
            raise ZeroDivisionError('Denominator cannot be 0!')
        elif not isinstance(new_den, int):
            raise TypeError('Incorrect value for denominator!')
        self.__den = new_den

    def __str__(self):
        if self.__den == 1:
            return f'{self.num}'
        return f'{self.num//math.gcd(self.num, self.den)}/{self.den//math.gcd(self.num, self.den)}'

    def get_float(self):
        return self.num / self.den

    def plus_frc(self, frac):
        return Rational(self.num * frac.den + self.den * frac.num, self.den * frac.den)

    def minus_frc(self, frac):
        return Rational(self.num * frac.den - self.den * frac.num, self.den * frac.den)

    def multip_frc(self, frac):
        return Rational(self.num * frac.num, self.den * frac.den)

    def divide_frc(self, frac):
        return Rational(self.num * frac.den, self.den * frac.num)


def main():
    try:
        r1 = Rational()
        r1.num, r1.den = 2, 5
        r2 = Rational(3, 6)
        print('Fraction_1:', r1.__str__(), '\nFraction_2:', r2.__str__())
        print('Float_1:', r1.get_float(), '\nFloat_2:', r2.get_float())
        p = r1.plus_frc(r2)
        minus = r1.minus_frc(r2)
        mul = r1.multip_frc(r2)
        d = r1.divide_frc(r2)
        print('Plus:', p.__str__())
        print('Minus:', minus.__str__())
        print('Multiply:', mul.__str__())
        print('Divide:', d.__str__())
    except Exception as ex:
        print(ex)


main()
