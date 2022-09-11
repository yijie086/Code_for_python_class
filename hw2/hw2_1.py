import numpy as np
print("This is a python code for homework2-1: Calculate of float type")


def p_function(fa, fr, fn):
    fp = (fa*fr/12.0)/(1.0-np.power(1.0+fr/12.0, -fn))
    return fp


print("------------------Initial Setup------------------")
num_of_month = 30*12
a = 1000000
r = [0.04, 0.05, 0.06]
p = [0.0, 0.0, 0.0]
tp = [0.0, 0.0, 0.0]
print("The amount of loans is " + str(a) + ".")
print("The loan cycle is " + str(num_of_month) + ".")
print("---------------------Result----------------------")
for i in range(3):
    p[i] = p_function(a, r[i], num_of_month)
    tp[i] = num_of_month*p[i]
    print("If the annual interest rate is " + str(100*r[i]) + "%.")
    print("The monthly repayment amount is " + str(p[i])+".")
    print("The total repayment amount is " + str(tp[i])+".")
