import math
import sys
print("This is a python code for homework3-2: Character encryption")
lstr = input("Please enter the string: ")
n_str = input("Please enter the encryption number (should be an int no less than -15):\n")
nch = float(n_str)
if nch != math.ceil(nch):
    print("WRONG number!")
    sys.exit()
if nch < -15:
    print("WRONG number!")
    sys.exit()
n = int(n_str)
str_list = list(lstr)
print("The cictext is: ")
for i in range(len(str_list)):
    print(chr(n+ord(str_list[i])), end="")
