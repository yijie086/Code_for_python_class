import math
print("This is a python code for homework3-1: Collatz conjecture")


def c_function(fn):
    if (fn / 2) == math.ceil(fn / 2):
        return fn / 2
    else:
        return 3 * fn + 1


n_str = input("Please enter a number\n")
n = int(n_str)
s = [n]
while n != 1:
    n = int(c_function(n))
    s.append(n)
print("The answer is:")
for i in range(len(s)):
    print(s[i], end=" ")
