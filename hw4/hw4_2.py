import sys
import math
print("This is a python code for homework4-2: Arithmetic operations for rational numbers.")

def gcd(a, b):
    if a == b:
        return a
    elif a > b:
        return gcd(a-b, b)
    else:
        return gcd(a, b-a)


def reduce(n, d):
    temp = gcd(math.fabs(n), math.fabs(d))
    n = int(n / temp)
    d = int(d / temp)
    if d < 0:
        n = -n
        d = -d
    return [n, d]


def add(x, y):
    ansu = x[0]*y[1]+x[1]*y[0]
    ansd = x[1]*y[1]
    return reduce(ansu, ansd)


def sub(x, y):
    ansu = x[0] * y[1] - x[1] * y[0]
    ansd = x[1] * y[1]
    return reduce(ansu, ansd)


def mul(x, y):
    ansu = x[0] * y[0]
    ansd = x[1] * y[1]
    return reduce(ansu, ansd)


def div(x, y):
    ansu = x[0] * y[1]
    ansd = x[1] * y[0]
    return reduce(ansu, ansd)


def output(x):
    print(str(x[0])+'/'+str(x[1]))


def get_rational(fs):
    temps = list(fs)
    par1 = temps.index('(')
    par2 = temps.index('/')
    par3 = temps.index(')')
    if fs[par1 + 1] == '-':
        tempu = temps[par1 + 2:par2]
        numu = -int("".join(tempu))
    else:
        tempu = temps[par1 + 1:par2]
        numu = int("".join(tempu))
    if fs[par2 + 1] == '-':
        tempd = temps[par2 + 2:par3]
        numu = -numu
        numd = int("".join(tempd))
    else:
        tempd = temps[par2 + 1:par3]
        numd = int("".join(tempd))
    return [numu, numd]


if __name__ == '__main__':
    if len(sys.argv) == 1:
        print (__doc__)
    elif len(sys.argv) == 2 and sys.argv[1] == '-h':
        print (__doc__)
    elif len(sys.argv) == 2 and sys.argv[1] == 'test':
        test_all_functions()
    else:
        import argparse
        parser = argparse.ArgumentParser()
        parser.add_argument('--op', type=str)
        parser.add_argument('--x', type=str)
        parser.add_argument('--y', type=str)
        args = parser.parse_args()
        op = args.op
        x = get_rational(args.x); y = get_rational(args.y)
        f = {'add':add, 'sub':sub, 'mul':mul, 'div':div}
        output(f[op](x, y))
