import math as math
print("This is a python code for homework2-2: Use of math module")


def find_angle(fa, fb, fc):
    fans = math.acos((fa*fa + fb*fb - fc*fc)/(2*fa*fb))
    return fans


print("--------------------------Initial Setup--------------------------")
a = 3
b = 6
c = 7
print("The side length of triangle is:")
print("a=" + str(a))
print("b=" + str(b))
print("c=" + str(c))
print("-----------------------------Result-----------------------------")
alpha = find_angle(b, c, a)
beta = find_angle(a, c, b)
gamma = find_angle(a, b, c)
print("Angle alpha is " + str(alpha)+ " rad or " + str(alpha*180/math.pi) + " degree.")
print("Angle beta is " + str(beta)+ " rad or " + str(beta*180/math.pi) + " degree.")
print("Angle alpha is " + str(gamma)+ " rad or " + str(gamma*180/math.pi) + " degree.")
print("The sum of three angle is " + str((alpha+beta+gamma)*180/math.pi) + " degree.")
