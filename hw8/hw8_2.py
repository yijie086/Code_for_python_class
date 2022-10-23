import timeit
print("This is a python code for homework8-2: Time of sorting methods")


def insertion_sort(s):
    n = len(s)
    for i in range(1, n):
        value = s[i]
        pos = i
        while pos > 0 and value < s[pos - 1] :
            s[pos] = s[pos - 1]
            pos -= 1
        s[pos] = value
    return s


def merge_ordered_lists(s1, s2):
    t = []
    i = j = 0
    while i < len(s1) and j < len(s2):
        if s1[i] < s2[j]:
            t.append(s1[i]); i += 1
        else:
            t.append(s2[j]); j += 1
    t += s1[i:]
    t += s2[j:]
    return t


def merge_sort(s):
    if len(s) <= 1:
        return s
    mid = len(s) // 2
    left = merge_sort(s[:mid])
    right = merge_sort(s[mid:])
    return merge_ordered_lists(left, right)


def qsort(s):
    if len(s) <= 1: return s
    s1 = [i for i in s if i < s[0]]
    s2 = [i for i in s if i > s[0]]
    s0 = [i for i in s if i == s[0]]
    return qsort(s1) + s0 + qsort(s2)


import random
def random_int_list(start, stop, length):
    start, stop = (int(start), int(stop)) if start <= stop else (int(stop), int(start))
    length = int(abs(length)) if length else 0
    random_list = []
    for i in range(length):
        random_list.append(random.randint(start, stop))
    return random_list


s1 = random_int_list(1, 100, 100)
s2 = random_int_list(1, 100, 200)
s3 = random_int_list(1, 100, 300)
s4 = random_int_list(1, 100, 400)
s5 = random_int_list(1, 100, 500)
s6 = random_int_list(1, 100, 600)
s7 = random_int_list(1, 100, 700)
s8 = random_int_list(1, 100, 800)
s9 = random_int_list(1, 100, 900)
s10 = random_int_list(1, 100, 1000)

set_up = """
import random
def random_int_list(start, stop, length):
    start, stop = (int(start), int(stop)) if start <= stop else (int(stop), int(start))
    length = int(abs(length)) if length else 0
    random_list = []
    for i in range(length):
        random_list.append(random.randint(start, stop))
    return random_list


s1 = random_int_list(1, 100, 100)
s2 = random_int_list(1, 100, 200)
s3 = random_int_list(1, 100, 300)
s4 = random_int_list(1, 100, 400)
s5 = random_int_list(1, 100, 500)
s6 = random_int_list(1, 100, 600)
s7 = random_int_list(1, 100, 700)
s8 = random_int_list(1, 100, 800)
s9 = random_int_list(1, 100, 900)
s10 = random_int_list(1, 100, 1000)


def insertion_sort(s):
    n = len(s)
    for i in range(1, n):
        value = s[i]
        pos = i
        while pos > 0 and value < s[pos - 1] :
            s[pos] = s[pos - 1]
            pos -= 1
        s[pos] = value
    return s


def merge_ordered_lists(s1, s2):
    t = []
    i = j = 0
    while i < len(s1) and j < len(s2):
        if s1[i] < s2[j]:
            t.append(s1[i]); i += 1
        else:
            t.append(s2[j]); j += 1
    t += s1[i:]
    t += s2[j:]
    return t


def merge_sort(s):
    if len(s) <= 1:
        return s
    mid = len(s) // 2
    left = merge_sort(s[:mid])
    right = merge_sort(s[mid:])
    return merge_ordered_lists(left, right)


def qsort(s):
    if len(s) <= 1: return s
    s1 = [i for i in s if i < s[0]]
    s2 = [i for i in s if i > s[0]]
    s0 = [i for i in s if i == s[0]]
    return qsort(s1) + s0 + qsort(s2)
"""

t1q = """
qsort(s1)
"""
t2q = """
qsort(s2)
"""
t3q = """
qsort(s3)
"""
t4q = """
qsort(s4)
"""
t5q = """
qsort(s5)
"""
t6q = """
qsort(s6)
"""
t7q = """
qsort(s7)
"""
t8q = """
qsort(s8)
"""
t9q = """
qsort(s9)
"""
t10q = """
qsort(s10)
"""
t1i = """
insertion_sort(s1)
"""
t2i = """
insertion_sort(s2)
"""
t3i = """
insertion_sort(s3)
"""
t4i = """
insertion_sort(s4)
"""
t5i = """
insertion_sort(s5)
"""
t6i = """
insertion_sort(s6)
"""
t7i = """
insertion_sort(s7)
"""
t8i = """
insertion_sort(s8)
"""
t9i = """
insertion_sort(s9)
"""
t10i = """
insertion_sort(s10)
"""
t1m = """
merge_sort(s1)
"""
t2m = """
merge_sort(s2)
"""
t3m = """
merge_sort(s3)
"""
t4m = """
merge_sort(s4)
"""
t5m = """
merge_sort(s5)
"""
t6m = """
merge_sort(s6)
"""
t7m = """
merge_sort(s7)
"""
t8m = """
merge_sort(s8)
"""
t9m = """
merge_sort(s9)
"""
t10m = """
merge_sort(s10)
"""
N = 10
print("**************************** Insertion sort **********************************")
print("Time for Insertion sort with array (100 elements):", timeit.timeit(stmt=t1i, setup=set_up, number=N)/N)
print("Time for Insertion sort with array (200 elements):", timeit.timeit(stmt=t2i, setup=set_up, number=N)/N)
print("Time for Insertion sort with array (300 elements):", timeit.timeit(stmt=t3i, setup=set_up, number=N)/N)
print("Time for Insertion sort with array (400 elements):", timeit.timeit(stmt=t4i, setup=set_up, number=N)/N)
print("Time for Insertion sort with array (500 elements):", timeit.timeit(stmt=t5i, setup=set_up, number=N)/N)
print("Time for Insertion sort with array (600 elements):", timeit.timeit(stmt=t6i, setup=set_up, number=N)/N)
print("Time for Insertion sort with array (700 elements):", timeit.timeit(stmt=t7i, setup=set_up, number=N)/N)
print("Time for Insertion sort with array (800 elements):", timeit.timeit(stmt=t8i, setup=set_up, number=N)/N)
print("Time for Insertion sort with array (900 elements):", timeit.timeit(stmt=t9i, setup=set_up, number=N)/N)
print("Time for Insertion sort with array (1000 elements):", timeit.timeit(stmt=t10i, setup=set_up, number=N)/N)
print("****************************** Merge sort ************************************")
print("Time for Merge sort with array (100 elements):", timeit.timeit(stmt=t1m, setup=set_up, number=N)/N)
print("Time for Merge sort with array (200 elements):", timeit.timeit(stmt=t2m, setup=set_up, number=N)/N)
print("Time for Merge sort with array (300 elements):", timeit.timeit(stmt=t3m, setup=set_up, number=N)/N)
print("Time for Merge sort with array (400 elements):", timeit.timeit(stmt=t4m, setup=set_up, number=N)/N)
print("Time for Merge sort with array (500 elements):", timeit.timeit(stmt=t5m, setup=set_up, number=N)/N)
print("Time for Merge sort with array (600 elements):", timeit.timeit(stmt=t6m, setup=set_up, number=N)/N)
print("Time for Merge sort with array (700 elements):", timeit.timeit(stmt=t7m, setup=set_up, number=N)/N)
print("Time for Merge sort with array (800 elements):", timeit.timeit(stmt=t8m, setup=set_up, number=N)/N)
print("Time for Merge sort with array (900 elements):", timeit.timeit(stmt=t9m, setup=set_up, number=N)/N)
print("Time for Merge sort with array (1000 elements):", timeit.timeit(stmt=t10m, setup=set_up, number=N)/N)
print("****************************** Quick sort ************************************")
print("Time for quick sort with array (100 elements):", timeit.timeit(stmt=t1q, setup=set_up, number=N)/N)
print("Time for quick sort with array (200 elements):", timeit.timeit(stmt=t2q, setup=set_up, number=N)/N)
print("Time for quick sort with array (300 elements):", timeit.timeit(stmt=t3q, setup=set_up, number=N)/N)
print("Time for quick sort with array (400 elements):", timeit.timeit(stmt=t4q, setup=set_up, number=N)/N)
print("Time for quick sort with array (500 elements):", timeit.timeit(stmt=t5q, setup=set_up, number=N)/N)
print("Time for quick sort with array (600 elements):", timeit.timeit(stmt=t6q, setup=set_up, number=N)/N)
print("Time for quick sort with array (700 elements):", timeit.timeit(stmt=t7q, setup=set_up, number=N)/N)
print("Time for quick sort with array (800 elements):", timeit.timeit(stmt=t8q, setup=set_up, number=N)/N)
print("Time for quick sort with array (900 elements):", timeit.timeit(stmt=t9q, setup=set_up, number=N)/N)
print("Time for quick sort with array (1000 elements):", timeit.timeit(stmt=t10q, setup=set_up, number=N)/N)
