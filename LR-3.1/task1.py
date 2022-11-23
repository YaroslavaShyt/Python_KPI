import math
import operator


class Rational:
    def __init__(self, num=1, den=1):
        self.num = num
        self.den = den

    @property
    def num(self):
        return self.__num // math.gcd(self.__num, self.__den)

    @property
    def den(self):
        return self.__den // math.gcd(self.__num, self.__den)

    @num.setter
    def num(self, new_num):
        if not isinstance(new_num, int):
            raise TypeError('Incorrect value for numerator!')
        self.__num = new_num

    @den.setter
    def den(self, new_den):
        if not isinstance(new_den, int):
            raise TypeError('Incorrect value for denominator!')
        elif new_den == 0:
            raise ZeroDivisionError('Denominator cannot be 0!')
        self.__den = new_den

    def __str__(self):
        if self.__den == 1:
            return f'{self.num}'
        return f'{self.num}/{self.den}'

    def __float__(self):
        return self.num / self.den

    def __add__(self, frac):
        if isinstance(frac, float):
            return float(self) + frac
        elif isinstance(frac, int):
            frac = Rational(frac)
        elif not isinstance(frac, Rational):
            return NotImplemented
        return Rational(self.num * frac.den + self.den * frac.num, self.den * frac.den)

    def __sub__(self, frac):
        return self + -frac

    def __neg__(self):
        return Rational(-self.num, self.den)

    def __mul__(self, frac):
        if isinstance(frac, float):
            return float(self) * frac
        elif isinstance(frac, int):
            frac = Rational(frac)
        elif not isinstance(frac, Rational):
            return NotImplemented
        return Rational(self.num * frac.num, self.den * frac.den)

    def __truediv__(self, frac):
        if isinstance(frac, float):
            return float(self) / frac
        elif isinstance(frac, int):
            frac = Rational(frac)
        elif not isinstance(frac, Rational):
            return NotImplemented
        return Rational(self.num * frac.den, self.den * frac.num)

    def comparison(self, frac, operation):
        if isinstance(frac, float):
            raise TypeError('Float comparison cannot give correct result due to computer rules')
        elif isinstance(frac, int):
            frac = Rational(frac)
        elif not isinstance(frac, Rational):
            return NotImplemented
        return operation(self.num * frac.den, self.den * frac.num)

    def __lt__(self, frac):
        return self.comparison(frac, operator.lt)

    def __le__(self, frac):
        return self.comparison(frac, operator.le)

    def __gt__(self, frac):
        return self.comparison(frac, operator.gt)

    def __ge__(self, frac):
        return self.comparison(frac, operator.ge)

    def __eq__(self, frac):
        return self.comparison(frac, operator.eq)

    def __ne__(self, frac):
        return self.comparison(frac, operator.ne)


try:
    r1 = Rational(2, 5)
    r2 = Rational(3, 6)
    print(f'Fractions: {r1} {r2}\n'
          f'Floats   : {float(r1)}  | {float(r2)}\n'
          f'Plus     : {r1 + r2} | {r1 + float(r2)}\n'
          f'Minus    : {r1 - r2} \n'
          f'Multiply : {r1 * r2} | {r1 * 2}\n'
          f'Divide   : {r1 / r2} \n'
          f'Less   |Less or equal   : {r1 < r2}  | {r1 <= r2}\n'
          f'Greater|Greater or equal: {r1 > r2} | {r1 >= r2}\n'
          f'Equal  |Not equal       : {r1 == r2} | {r1!=r2}')
except Exception as ex:
    print(ex)
