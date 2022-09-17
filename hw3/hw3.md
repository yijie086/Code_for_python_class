# Homework 3

## Exercise 1

### 考拉兹猜想

#### 题目：

定义一个从给定正整数构建一个整数序列的过程如下。开始时序列只包含。如果序列的最后一个数$m$不为$1$则根据$m$的奇偶性向序列追加一个数。如果$m$是偶数，则追加$m/2$，否则追加$3×m+1$。考拉兹猜想（Collatz conjecture）认为从任意正整数构建的序列都会以$1$终止。编写程序读取用户输入的正整数$n$，然后在`while`循环中输出一个以$1$终止的整数序列。输出的序列显示在一行，相邻的数之间用空格分隔。

#### 源代码：

```python
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

```

#### 运行结果：

```
/usr/local/bin/python3.9 "/Users/wangyijie/Library/Mobile Documents/com~apple~CloudDocs/Study_in_USTC/杂事/python科学计算/hw3/hw3_1.py"

This is a python code for homework3-1: Collatz conjecture
Please enter a number
15
The answer is:
15 46 23 70 35 106 53 160 80 40 20 10 5 16 8 4 2 1 
Process finished with exit code 0
```

## Exercise 2

### 字符串加密

#### 题目：

编写程序实现基于偏移量的字符串加密。加密的过程是对原字符串中的每个字符对应的`Unicode`值加上一个偏移量，然后将得到的`Unicode`值映射到该字符对应的加密字符。用户输入一个不小于$-15$的非零整数和一个由大小写字母或数字组成的字符串，程序生成并输出加密得到的字符串。例如用户输入$10$和字符串`Attack at 1600` 得到的加密字符串是 `K~~kmu*k~*;@::`。

#### 源代码：

```python
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

```

#### 运行结果：

```
/usr/local/bin/python3.9 "/Users/wangyijie/Library/Mobile Documents/com~apple~CloudDocs/Study_in_USTC/杂事/python科学计算/hw3/hw3_2.py"

This is a python code for homework3-2: Character encryption
Please enter the string: Attack at 1600
Please enter the encryption number (should be an int no less than -15):
10
The cictext is: 
K~~kmu*k~*;@::
Process finished with exit code 0
```

## Exercise 3

### 推导式转换

#### 题目：

将程序3.14中所有推导式转换为for语句。

#### 源代码：

```python
print("This is a python code for homework3-3: Comprehension")
nums = {25, 18, 91, 365, 12, 78, 59}
temp = list(nums)
multiplier_of_s = []
square_of_odds_temp = []
for i in range(len(temp)):
    if temp[i] % 3 == 0:
        multiplier_of_s.append(temp[i])
print(multiplier_of_s)
for i in range(len(temp)):
    if temp[i]*temp[i] % 2 == 1:
        square_of_odds_temp.append(temp[i]*temp[i])
square_of_odds = set(square_of_odds_temp)
print(square_of_odds)
print()
s = [25, 18, 91, 365, 12, 78, 59, 18, 91]
sr = dict()
tr = dict()
for i in range(len(s)):
    sr[s[i]] = s[i] % 3
    if s[i] % 3 ==0:
        tr[s[i]] = s[i] % 3
print(sr)
print(tr)

```

#### 运行结果：

```
/usr/local/bin/python3.9 "/Users/wangyijie/Library/Mobile Documents/com~apple~CloudDocs/Study_in_USTC/杂事/python科学计算/hw3/hw3_3.py"

This is a python code for homework3-3: Comprehension
[18, 12, 78]
{8281, 3481, 133225, 625}

{25: 1, 18: 0, 91: 1, 365: 2, 12: 0, 78: 0, 59: 2}
{18: 0, 12: 0, 78: 0}

Process finished with exit code 0
```

