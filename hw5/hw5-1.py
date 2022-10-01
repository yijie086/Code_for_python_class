print("This is a python code for homework5-1: Rational Number Class")
def gcd(a, b):
    if a == b:
        return a
    elif a > b:
        return gcd(a-b, b)
    else:
        return gcd(a, b-a)


class Rational:
    def __init__(self, n=0, d=1):
        if n != 0:
            fgcd = gcd(abs(n), abs(d))
        else:
            fgcd = 1
        n = n/fgcd
        d = d/fgcd
        if d < 0:
            n = -n
            d = -d
        if n == 0:
            d = 1
        _nu = n
        _de = d
        self.__dict__['nu'] = _nu
        self.__dict__['de'] = _de

    def __setattr__(self, name, value):
        raise TypeError('Error: Rational objects anu demuntable')

    def __str__(self):
        return '%d/%d' % (self.nu, self.de)

    def __add__(self, other):
        return Rational(self.nu*other.de+other.nu*self.de, self.de*other.de)

    def __sub__(self, other):
        return Rational(self.nu*other.de-other.nu*self.de, self.de*other.de)

    def __mul__(self, other):
        return Rational(self.nu*other.nu, self.de*other.de)

    def __truediv__(self, other):
        return Rational(self.nu*other.de, self.de*other.nu)

    def __eq__(self, other):
        temp = self - other
        if temp.nu == 0:
            return True
        else:
            return False

    def __ne__(self, other):
        temp = self - other
        if temp.nu != 0:
            return True
        else:
            return False

    def __gt__(self, other):
        temp = self - other
        if temp.nu > 0:
            return True
        else:
            return False

    def __lt__(self, other):
        temp = self - other
        if temp.nu < 0:
            return True
        else:
            return False

    def __ge__(self, other):
        temp = self - other
        if temp.nu >= 0:
            return True
        else:
            return False

    def __le__(self, other):
        temp = self - other
        if temp.nu <= 0:
            return True
        else:
            return False

def test():
    testsuite = [
        ('Rational(2, 3) + Rational(-70, 40)', Rational(-13, 12)),
        ('Rational(-20, 3) - Rational(120, 470)', Rational(-976, 141)),
        ('Rational(-6, 19) * Rational(-114, 18)', Rational(2, 1)),
        ('Rational(-6, 19) / Rational(-114, -28)', Rational(-28, 361)),

        ('Rational(-6, 19) == Rational(-14, 41)', False),
        ('Rational(-6, 19) != Rational(-14, 41)', True),
        ('Rational(6, -19) > Rational(14, -41)', True),
        ('Rational(-6, 19) < Rational(-14, 41)', False),
        ('Rational(-6, 19) >= Rational(-14, 41)', True),
        ('Rational(6, -19) <= Rational(14, -41)', False),
        ('Rational(-15, 8) == Rational(120, -64)', True),
    ]
    for t in testsuite:
        try:
            result = eval(t[0])
        except:
            print('Error in evaluating ' + t[0]); continue

        if result != t[1]:
            print('Error:  %s != %s' % (t[0], t[1]))

if __name__ == '__main__':
    test()
