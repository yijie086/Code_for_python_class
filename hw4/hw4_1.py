import math
print("This is a python code for homework4-1: Binary search")


def is_sorted(fs):
    flag = True
    for j in range(len(fs)-1):
        if fs[j] > fs[j+1]:
            flag = False
    return flag


def qsort(fs):
    if len(fs) <= 1:
        return fs
    s1 = [i for i in fs if i < fs[0]]
    s2 = [i for i in fs if i > fs[0]]
    s0 = [i for i in fs if i == fs[0]]
    return qsort(s1) + s0 + qsort(s2)


def binary_search(f_s, f_low, f_high, f_k):
    if f_low > f_high:
        return -1
    f_mid = math.ceil(0.5*f_low+0.5*f_high)
    if f_s[f_mid] == f_k:
        return f_mid
    if f_s[f_mid] > f_k:
        if f_s[f_mid-1] == f_k:
            return f_mid-1
        elif f_mid - 1 == f_low:
            return -1
        return binary_search(f_s, f_low, f_mid-1, f_k)
    if f_s[f_mid] < f_k:
        return binary_search(f_s, f_mid, f_high, f_k)


s = [5, 6, 21, 32, 51, 60, 67, 73, 77, 99]
if not is_sorted(s):
    s = qsort(s)
print(binary_search(s, 0, len(s) - 1, 5))
print(binary_search(s, 0, len(s) - 1, 31))
print(binary_search(s, 0, len(s) - 1, 99))
print(binary_search(s, 0, len(s) - 1, 64))
print(binary_search(s, 0, len(s) - 1, 51))
