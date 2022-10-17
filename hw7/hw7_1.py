import sys
import numpy as np
print("This is a python code for homework7-2: Triangle")


def usage():
    print("USAGE")


def main(argv):
    for arg in argv[1:]:
        if arg == '-h' or arg == '--help':
            usage()
            sys.exit()
        else:
            # print("Error: invalid parameters")
            sys.exit()


flag = False
args = sys.argv

if len(args) < 4:
    print("Error: invalid parameters: Number of variables is less than 3!")
    sys.exit()

if len(args) > 4:
    print("Error: invalid parameters: Number of variables is more than 3!")
    sys.exit()

a = args[1]
b = args[2]
c = args[3]

if type(eval(a)) != float:
    flag = True
    print("Error: invalid parameters: The first variable is not a float type!")
if type(eval(b)) != float:
    flag = True
    print("Error: invalid parameters: The second variable is not a float type!")
if type(eval(c)) != float:
    flag = True
    print("Error: invalid parameters: The third variable is not a float type!")
if flag:
    sys.exit()

ta = float(a)
tb = float(b)
tc = float(c)
temp = [ta, tb, tc]
temp.sort()
if temp[0] + temp[1] <= temp[2]:
    print("InvalidTriangleError: This triangle can not exists!")
    print("Error Information:", temp[0], "+", temp[1], "<=", temp[2], "!")
    sys.exit()

s = sum(temp)/2
area = np.sqrt(s*(s-ta)*(s-tb)*(s-tc))

print("The area of this triangle is:", area)

if __name__ == '__main__':
    main(sys.argv)
