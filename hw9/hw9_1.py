import matplotlib.pyplot as plt
import numpy
import numpy as np
import math
print("This is a python code for homework9-1: Error Convergence")


class Integrator(object):
    def __init__(self, a, b, n):
        self.a, self.b, self.n = a, b, n
        self.points, self.weights = self.compute_points()

    def compute_points(self):
        raise NotImplementedError('no rule in class %s' \
                                   % self.__class__.__name__)
    def integrate(self, f):
        sum = 0
        for i in range(self.n+1):
            sum = sum + self.weights[i]*f(self.points[i])
        return sum


class Trapezoidal(Integrator):
    def compute_points(self):
        p = list()
        w = list()
        for i in range(self.n+1):
            h = (self.b-self.a)/(self.n)
            p.append(self.a+i*h)
            if i == 0:
                w.append(h / 2)
            elif i == self.n:
                w.append(h / 2)
            else:
                w.append(h)
        return p, w


class Simpson(Integrator):
    def compute_points(self):
        p = list()
        w = list()
        if self.n%2 == 1:
            self.n = self.n+1
        for i in range(self.n+1):
            h = (self.b-self.a)/(self.n)
            p.append(self.a+i*h)
            if i == 0:
                w.append(h / 3)
            elif i == self.n:
                w.append(h / 3)
            elif i%2 == 0:
                w.append(2*h/3)
            else:
                w.append(4 * h / 3)
        return p, w


class GaussLegendre(Integrator):
    def compute_points(self):
        p = list()
        w = list()
        if self.n%2 == 0:
            self.n = self.n+1
        for i in range(self.n+1):
            h = 2*(self.b-self.a)/(self.n+1)
            if i%2 == 0:
                p.append(self.a+(i+1)*h/2-math.sqrt(3)*h/6)
            else:
                p.append(self.a+i*h/2+math.sqrt(3)*h/6)
            w.append(h/2)
        return p, w

# A linear function will be exactly integrated by all
# the methods, so such an f is the candidate for testing
# the implementations


def f(x): return numpy.sin(x)


def F(x): return -numpy.cos(x)


a = 2; b = 10;
I_exact = F(b) - F(a)

I_T = []
error_T = []
I_S = []
error_S = []
I_G = []
error_G = []
nC = 1000
for n in range(2, nC):
    integrator = Trapezoidal(a, b, n)
    ans = integrator.integrate(f)
    I_T.append(ans)
    error_T.append(abs(ans-I_exact)/I_exact)
for n in range(2, nC):
    integrator = Simpson(a, b, n)
    ans = integrator.integrate(f)
    I_S.append(ans)
    error_S.append(abs(ans-I_exact)/I_exact)
for n in range(2, nC):
    integrator = GaussLegendre(a, b, n)
    ans = integrator.integrate(f)
    I_G.append(ans)
    error_G.append(abs(ans-I_exact)/I_exact)
nC = np.arange(2, 1000, 1)
error_T = np.array(error_T)
error_G = np.array(error_G)
error_S = np.array(error_S)
plt.loglog()
plt.plot(nC, error_T, color = 'red', label = 'Trapezoidal')
plt.plot(nC, error_S, color = 'blue', label = 'Simpson')
plt.plot(nC, error_G, color = 'skyblue', label = 'GaussLegendre')
plt.ylabel('relative error')
plt.xlabel('n')
plt.legend()
plt.savefig('hw9_1.jpg')
