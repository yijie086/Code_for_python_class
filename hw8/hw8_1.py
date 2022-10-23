print("This is a python code for homework8-1: 3-sum Problem")
s = [21, 73, 6, 67, 99, 60, 77, 5, 51, 32]
s.sort()


def binarySearch(arr, l, r, x):
    if r >= l:
        mid = int(l + (r - l) / 2)
        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            return binarySearch(arr, l, mid - 1, x)
        else:
            return binarySearch(arr, mid + 1, r, x)
    else:
        return -1


def sum_3_problem(s, x):
    n = len(s)
    postion_temp = 0
    for i in range(n-1):
        for j in range(i+1, n):
            b = s[i]
            c = s[j]
            temp = x - b - c
            if binarySearch(s, 0, len(s)-1, temp) != -1:
                temp1 = i
                temp2 = j
                postion_temp = binarySearch(s, 0, len(s)-1, temp)
    if postion_temp == -1 or postion_temp == 0:
        return -1
    else:
        if postion_temp == i or postion_temp == j:
            return -1
        else:
            return s[temp1], s[temp2], s[postion_temp]


x = 152
ans = sum_3_problem(s, x)

if ans == -1:
    print("There are no 3 numbers that sum of them is", x)
else:
    print(x, '= sum of ', sum_3_problem(s, x))
