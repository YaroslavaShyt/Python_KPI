import math


class Rational:
    def __init__(self, num=1, den=1):
        self.__num = self.set_num(num) // math.gcd(num, den)
        self.__den = self.set_den(den) // math.gcd(num, den)

    def get_num(self):
        return self.__num

    def get_den(self):
        return self.__den

    def set_num(self, new_num):
        if isinstance(new_num, int):
            self.__num = new_num
            return self.__num
        raise TypeError('Incorrect value for numerator!')

    def set_den(self, new_den):
        if new_den == 0:
            raise ZeroDivisionError('Denominator cannot be 0!')
        elif isinstance(new_den, int):
            self.__den = new_den
            return self.__den
        else:
            raise TypeError('Incorrect value for denominator!')

    def __str__(self):
        if self.__den == 1:
            return f'{self.__num}'
        return f'{self.__num}/{self.__den}'

    def get_float(self):
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
    try:
        r1 = Rational()
        r1.set_num(2)
        r1.set_den(5)
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
