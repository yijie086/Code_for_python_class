# Homework 2

## Exercise 1

### float类型的计算

#### 题目：

等额本息是一种分期偿还贷款的方式，即借款人每月按相等的金额偿还贷款本息, 每月还款金额 $P$ 可 根据贷款总额 $A$ 、年利率 $r$ 和贷款月数 $n$ 计算得到, 公式为

$$
P=\frac{\frac{r}{12} A}{1-\left(1+\frac{r}{12}\right)^{-n}}
$$

计算当贷款金额为 1000000 , 贷款时间为 30 年, 年利率分别为 4%, 5% 和 6% 时的每月还款金额和还款总额。

#### 源代码：

```python
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

```

#### 运行结果：

```
/usr/local/bin/python3.9 "/Users/wangyijie/Library/Mobile Documents/com~apple~CloudDocs/Study_in_USTC/物理/python科学计算/hw2/hw2_1.py"

This is a python code for homework2-1: Calculate of float type
------------------Initial Setup------------------
The amount of loans is 1000000.
The loan cycle is 360.
---------------------Result----------------------
If the annual interest rate is 4.0%.
The monthly repayment amount is 4774.152954654538.
The total repayment amount is 1718695.0636756336.
If the annual interest rate is 5.0%.
The monthly repayment amount is 5368.216230121398.
The total repayment amount is 1932557.8428437035.
If the annual interest rate is 6.0%.
The monthly repayment amount is 5995.505251527569.
The total repayment amount is 2158381.890549925.

Process finished with exit code 0
```

## Exercise 2

### math模块的使用

#### 题目：

定义三个变量 “ $a=3 ; b=6 ; c=7$ ” 表示一个三角形的三个边的长度, 使用公式

$$
a^2=b^2+c^2-2 b c \cos \alpha
$$

$$
b^2=a^2+c^2-2 a c \cos \beta 
$$

$$
c^2=a^2+b^2-2 a b \cos \gamma
$$

分别计算三个内角 $(\alpha, \beta, \gamma)$ 的度数, 然后检验等式 $\alpha+\beta+\gamma=180$ 是否成立。

#### 源代码：

```python
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

```

#### 运行结果：

```
/usr/local/bin/python3.9 "/Users/wangyijie/Library/Mobile Documents/com~apple~CloudDocs/Study_in_USTC/物理/python科学计算/hw2/hw2_2.py"

This is a python code for homework2-2: Use of math module
--------------------------Initial Setup--------------------------
The side length of triangle is:
a=3
b=6
c=7
-----------------------------Result-----------------------------
Angle alpha is 0.4399759547909189 rad or 25.208765296758365 degree.
Angle beta is 1.019479357663014 rad or 58.41186449479884 degree.
Angle alpha is 1.6821373411358604 rad or 96.37937020844281 degree.
The sum of three angle is 180.0 degree.

Process finished with exit code 0
```

## Exercise 2

### list类型的计算

#### 题目：

定义两个列表 “ $\mathrm{s}=[2,4,0,1,3,9,5,8,6,7] ; \mathrm{t}=[2,6,8,4]$ ”, 对于表 $2.4$ 中的每种运算, 运行并记录输出结果。

#### 源代码：

```python
import math

print("This is a python code for homework2-3: Calculate of list type")
print("----------------------------Initial Setup-----------------------------")
s = [2, 4, 0, 1, 3, 9, 5, 8, 6, 7]
t = [2, 6, 8, 4]
print("s list = " + str(s))
print("t list = " + str(t))

print("-------------------------------Result---------------------------------")

print("++++++++++++++++++++++++++ s[i] = x result +++++++++++++++++++++++++++")
print("I assume x=8!!!")
x = 8
for i in range(len(s)):
    s = [2, 4, 0, 1, 3, 9, 5, 8, 6, 7]
    s[i] = x
    print("Answer of s[" + str(i) + "] = x: " + str(s))
print("+++++++++++++++++++++++++ s[i:j] = t result ++++++++++++++++++++++++++")
for i in range(len(s)-len(t)+1):
    s = [2, 4, 0, 1, 3, 9, 5, 8, 6, 7]
    s[i:i+len(t)] = t
    print("Answer of s[" + str(i) + ":" + str(i+4) + "] = t: " + str(s))
print("+++++++++++++++++++++++++ del s[i:j] result ++++++++++++++++++++++++++")
s = [2, 4, 0, 1, 3, 9, 5, 8, 6, 7]
for i in range(len(s)+1):
    for j in range(i+1, len(s)+1):
        del s[i:j]
        print("Answer of del s[" + str(i) + ":" + str(j) + "] : " + str(s))
        s = [2, 4, 0, 1, 3, 9, 5, 8, 6, 7]
print("++++++++++++++++++++++++ s[i:j:k] = t result +++++++++++++++++++++++++")
for k in range(1, math.floor(len(s)/(len(t)-1))+1):
    print("If k = " + str(k) + ":")
    s = [2, 4, 0, 1, 3, 9, 5, 8, 6, 7]
    for i in range(len(s)-k*len(t)+k):
        j = i+k*len(t)-k+1
        s[i:j:k] = t
        print("Answer of s[" + str(i) + ":" + str(j) + ":" + str(k) + "] = t : " + str(s))
        s = [2, 4, 0, 1, 3, 9, 5, 8, 6, 7]
print("++++++++++++++++++++++++ del s[i:j:k] result +++++++++++++++++++++++++")
for k in range(1, len(s)):
    print("If k = " + str(k) + ":")
    s = [2, 4, 0, 1, 3, 9, 5, 8, 6, 7]
    for i in range(len(s)):
        for j in range(i+k+1, len(s)+1):
            del s[i:j:k]
            print("Answer of del s[" + str(i) + ":" + str(j) + ":" + str(k) + "] : " + str(s))
            s = [2, 4, 0, 1, 3, 9, 5, 8, 6, 7]
print("++++++++++++++++++++++++ s.append(x) result +++++++++++++++++++++++++")
print("I assume x =8!!!")
s = [2, 4, 0, 1, 3, 9, 5, 8, 6, 7]
s.append(x)
print("Answer of del s.append(x): " + str(s))
print("+++++++++++++++++++++++++ s.clear() result ++++++++++++++++++++++++++")
s = [2, 4, 0, 1, 3, 9, 5, 8, 6, 7]
s.clear()
print("Answer of del s.clear(): " + str(s))
print("++++++++++++++++++++++++++ s.copy() result ++++++++++++++++++++++++++")
s = [2, 4, 0, 1, 3, 9, 5, 8, 6, 7]
print("Answer of del s.copy(): " + str(s.copy()))
print("+++++++++++++++++++++++++ s.extend(t) result ++++++++++++++++++++++++")
s = [2, 4, 0, 1, 3, 9, 5, 8, 6, 7]
s.extend(t)
print("Answer of del s.extend(t): " + str(s))
print("+++++++++++++++++++++++++++ s += t result +++++++++++++++++++++++++++")
s = [2, 4, 0, 1, 3, 9, 5, 8, 6, 7]
s += t
print("Answer of del s += t: " + str(s))
print("+++++++++++++++++++++++++++ s *= n result +++++++++++++++++++++++++++")
s = [2, 4, 0, 1, 3, 9, 5, 8, 6, 7]
print("I assume n = 2!!!")
s *= 2
print("Answer of del s *= 2: " + str(s))
print("++++++++++++++++++++++++ s.insert(i,x) result +++++++++++++++++++++++")
print("I assume x =8!!!")
s = [2, 4, 0, 1, 3, 9, 5, 8, 6, 7]
for i in range(len(s)+1):
    s.insert(i, x)
    print("Answer of s.insert(i,x): " + str(s))
    s = [2, 4, 0, 1, 3, 9, 5, 8, 6, 7]
print("++++++++++++++++++++++++++ s.pop(i) result ++++++++++++++++++++++++++")
s = [2, 4, 0, 1, 3, 9, 5, 8, 6, 7]
for i in range(len(s)):
    ans = s.pop(i)
    print("Answer of s.pop(" + str(i) + "): " + str(s) + " and return " + str(ans))
    s = [2, 4, 0, 1, 3, 9, 5, 8, 6, 7]
print("+++++++++++++++++++++++++ s.remove(i) result ++++++++++++++++++++++++")
s = [2, 4, 0, 1, 3, 9, 5, 8, 6, 7]
for i in range(max(s)):
    s.remove(i)
    print("Answer of s.remove(" + str(i) + "): " + str(s))
    s = [2, 4, 0, 1, 3, 9, 5, 8, 6, 7]
print("+++++++++++++++++++++++++ s.reverse() result ++++++++++++++++++++++++")
s = [2, 4, 0, 1, 3, 9, 5, 8, 6, 7]
s.reverse()
print("Answer of s.reverse(): " + str(s))
print("++++++++++++++++++++++++++ s.sort() result +++++++++++++++++++++++++")
s = [2, 4, 0, 1, 3, 9, 5, 8, 6, 7]
s.sort()
print("Answer of s.sort(): " + str(s))
print("++++++++++++++++++++++++++ s.sort(reverse=True) result +++++++++++++++++++++++++")
s = [2, 4, 0, 1, 3, 9, 5, 8, 6, 7]
s.sort(reverse=True)
print("Answer of s.sort(reverse=True): " + str(s))

```

#### 运行结果：

```
/usr/local/bin/python3.9 "/Users/wangyijie/Library/Mobile Documents/com~apple~CloudDocs/Study_in_USTC/物理/python科学计算/hw2/hw2_3.py"

This is a python code for homework2-3: Calculate of list type
----------------------------Initial Setup-----------------------------
s list = [2, 4, 0, 1, 3, 9, 5, 8, 6, 7]
t list = [2, 6, 8, 4]
-------------------------------Result---------------------------------
++++++++++++++++++++++++++ s[i] = x result +++++++++++++++++++++++++++
I assume x=8!!!
Answer of s[0] = x: [8, 4, 0, 1, 3, 9, 5, 8, 6, 7]
Answer of s[1] = x: [2, 8, 0, 1, 3, 9, 5, 8, 6, 7]
Answer of s[2] = x: [2, 4, 8, 1, 3, 9, 5, 8, 6, 7]
Answer of s[3] = x: [2, 4, 0, 8, 3, 9, 5, 8, 6, 7]
Answer of s[4] = x: [2, 4, 0, 1, 8, 9, 5, 8, 6, 7]
Answer of s[5] = x: [2, 4, 0, 1, 3, 8, 5, 8, 6, 7]
Answer of s[6] = x: [2, 4, 0, 1, 3, 9, 8, 8, 6, 7]
Answer of s[7] = x: [2, 4, 0, 1, 3, 9, 5, 8, 6, 7]
Answer of s[8] = x: [2, 4, 0, 1, 3, 9, 5, 8, 8, 7]
Answer of s[9] = x: [2, 4, 0, 1, 3, 9, 5, 8, 6, 8]
+++++++++++++++++++++++++ s[i:j] = t result ++++++++++++++++++++++++++
Answer of s[0:4] = t: [2, 6, 8, 4, 3, 9, 5, 8, 6, 7]
Answer of s[1:5] = t: [2, 2, 6, 8, 4, 9, 5, 8, 6, 7]
Answer of s[2:6] = t: [2, 4, 2, 6, 8, 4, 5, 8, 6, 7]
Answer of s[3:7] = t: [2, 4, 0, 2, 6, 8, 4, 8, 6, 7]
Answer of s[4:8] = t: [2, 4, 0, 1, 2, 6, 8, 4, 6, 7]
Answer of s[5:9] = t: [2, 4, 0, 1, 3, 2, 6, 8, 4, 7]
Answer of s[6:10] = t: [2, 4, 0, 1, 3, 9, 2, 6, 8, 4]
+++++++++++++++++++++++++ del s[i:j] result ++++++++++++++++++++++++++
Answer of del s[0:1] : [4, 0, 1, 3, 9, 5, 8, 6, 7]
Answer of del s[0:2] : [0, 1, 3, 9, 5, 8, 6, 7]
Answer of del s[0:3] : [1, 3, 9, 5, 8, 6, 7]
Answer of del s[0:4] : [3, 9, 5, 8, 6, 7]
Answer of del s[0:5] : [9, 5, 8, 6, 7]
Answer of del s[0:6] : [5, 8, 6, 7]
Answer of del s[0:7] : [8, 6, 7]
Answer of del s[0:8] : [6, 7]
Answer of del s[0:9] : [7]
Answer of del s[0:10] : []
Answer of del s[1:2] : [2, 0, 1, 3, 9, 5, 8, 6, 7]
Answer of del s[1:3] : [2, 1, 3, 9, 5, 8, 6, 7]
Answer of del s[1:4] : [2, 3, 9, 5, 8, 6, 7]
Answer of del s[1:5] : [2, 9, 5, 8, 6, 7]
Answer of del s[1:6] : [2, 5, 8, 6, 7]
Answer of del s[1:7] : [2, 8, 6, 7]
Answer of del s[1:8] : [2, 6, 7]
Answer of del s[1:9] : [2, 7]
Answer of del s[1:10] : [2]
Answer of del s[2:3] : [2, 4, 1, 3, 9, 5, 8, 6, 7]
Answer of del s[2:4] : [2, 4, 3, 9, 5, 8, 6, 7]
Answer of del s[2:5] : [2, 4, 9, 5, 8, 6, 7]
Answer of del s[2:6] : [2, 4, 5, 8, 6, 7]
Answer of del s[2:7] : [2, 4, 8, 6, 7]
Answer of del s[2:8] : [2, 4, 6, 7]
Answer of del s[2:9] : [2, 4, 7]
Answer of del s[2:10] : [2, 4]
Answer of del s[3:4] : [2, 4, 0, 3, 9, 5, 8, 6, 7]
Answer of del s[3:5] : [2, 4, 0, 9, 5, 8, 6, 7]
Answer of del s[3:6] : [2, 4, 0, 5, 8, 6, 7]
Answer of del s[3:7] : [2, 4, 0, 8, 6, 7]
Answer of del s[3:8] : [2, 4, 0, 6, 7]
Answer of del s[3:9] : [2, 4, 0, 7]
Answer of del s[3:10] : [2, 4, 0]
Answer of del s[4:5] : [2, 4, 0, 1, 9, 5, 8, 6, 7]
Answer of del s[4:6] : [2, 4, 0, 1, 5, 8, 6, 7]
Answer of del s[4:7] : [2, 4, 0, 1, 8, 6, 7]
Answer of del s[4:8] : [2, 4, 0, 1, 6, 7]
Answer of del s[4:9] : [2, 4, 0, 1, 7]
Answer of del s[4:10] : [2, 4, 0, 1]
Answer of del s[5:6] : [2, 4, 0, 1, 3, 5, 8, 6, 7]
Answer of del s[5:7] : [2, 4, 0, 1, 3, 8, 6, 7]
Answer of del s[5:8] : [2, 4, 0, 1, 3, 6, 7]
Answer of del s[5:9] : [2, 4, 0, 1, 3, 7]
Answer of del s[5:10] : [2, 4, 0, 1, 3]
Answer of del s[6:7] : [2, 4, 0, 1, 3, 9, 8, 6, 7]
Answer of del s[6:8] : [2, 4, 0, 1, 3, 9, 6, 7]
Answer of del s[6:9] : [2, 4, 0, 1, 3, 9, 7]
Answer of del s[6:10] : [2, 4, 0, 1, 3, 9]
Answer of del s[7:8] : [2, 4, 0, 1, 3, 9, 5, 6, 7]
Answer of del s[7:9] : [2, 4, 0, 1, 3, 9, 5, 7]
Answer of del s[7:10] : [2, 4, 0, 1, 3, 9, 5]
Answer of del s[8:9] : [2, 4, 0, 1, 3, 9, 5, 8, 7]
Answer of del s[8:10] : [2, 4, 0, 1, 3, 9, 5, 8]
Answer of del s[9:10] : [2, 4, 0, 1, 3, 9, 5, 8, 6]
++++++++++++++++++++++++ s[i:j:k] = t result +++++++++++++++++++++++++
If k = 1:
Answer of s[0:4:1] = t : [2, 6, 8, 4, 3, 9, 5, 8, 6, 7]
Answer of s[1:5:1] = t : [2, 2, 6, 8, 4, 9, 5, 8, 6, 7]
Answer of s[2:6:1] = t : [2, 4, 2, 6, 8, 4, 5, 8, 6, 7]
Answer of s[3:7:1] = t : [2, 4, 0, 2, 6, 8, 4, 8, 6, 7]
Answer of s[4:8:1] = t : [2, 4, 0, 1, 2, 6, 8, 4, 6, 7]
Answer of s[5:9:1] = t : [2, 4, 0, 1, 3, 2, 6, 8, 4, 7]
Answer of s[6:10:1] = t : [2, 4, 0, 1, 3, 9, 2, 6, 8, 4]
If k = 2:
Answer of s[0:7:2] = t : [2, 4, 6, 1, 8, 9, 4, 8, 6, 7]
Answer of s[1:8:2] = t : [2, 2, 0, 6, 3, 8, 5, 4, 6, 7]
Answer of s[2:9:2] = t : [2, 4, 2, 1, 6, 9, 8, 8, 4, 7]
Answer of s[3:10:2] = t : [2, 4, 0, 2, 3, 6, 5, 8, 6, 4]
If k = 3:
Answer of s[0:10:3] = t : [2, 4, 0, 6, 3, 9, 8, 8, 6, 4]
++++++++++++++++++++++++ del s[i:j:k] result +++++++++++++++++++++++++
If k = 1:
Answer of del s[0:2:1] : [0, 1, 3, 9, 5, 8, 6, 7]
Answer of del s[0:3:1] : [1, 3, 9, 5, 8, 6, 7]
Answer of del s[0:4:1] : [3, 9, 5, 8, 6, 7]
Answer of del s[0:5:1] : [9, 5, 8, 6, 7]
Answer of del s[0:6:1] : [5, 8, 6, 7]
Answer of del s[0:7:1] : [8, 6, 7]
Answer of del s[0:8:1] : [6, 7]
Answer of del s[0:9:1] : [7]
Answer of del s[0:10:1] : []
Answer of del s[1:3:1] : [2, 1, 3, 9, 5, 8, 6, 7]
Answer of del s[1:4:1] : [2, 3, 9, 5, 8, 6, 7]
Answer of del s[1:5:1] : [2, 9, 5, 8, 6, 7]
Answer of del s[1:6:1] : [2, 5, 8, 6, 7]
Answer of del s[1:7:1] : [2, 8, 6, 7]
Answer of del s[1:8:1] : [2, 6, 7]
Answer of del s[1:9:1] : [2, 7]
Answer of del s[1:10:1] : [2]
Answer of del s[2:4:1] : [2, 4, 3, 9, 5, 8, 6, 7]
Answer of del s[2:5:1] : [2, 4, 9, 5, 8, 6, 7]
Answer of del s[2:6:1] : [2, 4, 5, 8, 6, 7]
Answer of del s[2:7:1] : [2, 4, 8, 6, 7]
Answer of del s[2:8:1] : [2, 4, 6, 7]
Answer of del s[2:9:1] : [2, 4, 7]
Answer of del s[2:10:1] : [2, 4]
Answer of del s[3:5:1] : [2, 4, 0, 9, 5, 8, 6, 7]
Answer of del s[3:6:1] : [2, 4, 0, 5, 8, 6, 7]
Answer of del s[3:7:1] : [2, 4, 0, 8, 6, 7]
Answer of del s[3:8:1] : [2, 4, 0, 6, 7]
Answer of del s[3:9:1] : [2, 4, 0, 7]
Answer of del s[3:10:1] : [2, 4, 0]
Answer of del s[4:6:1] : [2, 4, 0, 1, 5, 8, 6, 7]
Answer of del s[4:7:1] : [2, 4, 0, 1, 8, 6, 7]
Answer of del s[4:8:1] : [2, 4, 0, 1, 6, 7]
Answer of del s[4:9:1] : [2, 4, 0, 1, 7]
Answer of del s[4:10:1] : [2, 4, 0, 1]
Answer of del s[5:7:1] : [2, 4, 0, 1, 3, 8, 6, 7]
Answer of del s[5:8:1] : [2, 4, 0, 1, 3, 6, 7]
Answer of del s[5:9:1] : [2, 4, 0, 1, 3, 7]
Answer of del s[5:10:1] : [2, 4, 0, 1, 3]
Answer of del s[6:8:1] : [2, 4, 0, 1, 3, 9, 6, 7]
Answer of del s[6:9:1] : [2, 4, 0, 1, 3, 9, 7]
Answer of del s[6:10:1] : [2, 4, 0, 1, 3, 9]
Answer of del s[7:9:1] : [2, 4, 0, 1, 3, 9, 5, 7]
Answer of del s[7:10:1] : [2, 4, 0, 1, 3, 9, 5]
Answer of del s[8:10:1] : [2, 4, 0, 1, 3, 9, 5, 8]
If k = 2:
Answer of del s[0:3:2] : [4, 1, 3, 9, 5, 8, 6, 7]
Answer of del s[0:4:2] : [4, 1, 3, 9, 5, 8, 6, 7]
Answer of del s[0:5:2] : [4, 1, 9, 5, 8, 6, 7]
Answer of del s[0:6:2] : [4, 1, 9, 5, 8, 6, 7]
Answer of del s[0:7:2] : [4, 1, 9, 8, 6, 7]
Answer of del s[0:8:2] : [4, 1, 9, 8, 6, 7]
Answer of del s[0:9:2] : [4, 1, 9, 8, 7]
Answer of del s[0:10:2] : [4, 1, 9, 8, 7]
Answer of del s[1:4:2] : [2, 0, 3, 9, 5, 8, 6, 7]
Answer of del s[1:5:2] : [2, 0, 3, 9, 5, 8, 6, 7]
Answer of del s[1:6:2] : [2, 0, 3, 5, 8, 6, 7]
Answer of del s[1:7:2] : [2, 0, 3, 5, 8, 6, 7]
Answer of del s[1:8:2] : [2, 0, 3, 5, 6, 7]
Answer of del s[1:9:2] : [2, 0, 3, 5, 6, 7]
Answer of del s[1:10:2] : [2, 0, 3, 5, 6]
Answer of del s[2:5:2] : [2, 4, 1, 9, 5, 8, 6, 7]
Answer of del s[2:6:2] : [2, 4, 1, 9, 5, 8, 6, 7]
Answer of del s[2:7:2] : [2, 4, 1, 9, 8, 6, 7]
Answer of del s[2:8:2] : [2, 4, 1, 9, 8, 6, 7]
Answer of del s[2:9:2] : [2, 4, 1, 9, 8, 7]
Answer of del s[2:10:2] : [2, 4, 1, 9, 8, 7]
Answer of del s[3:6:2] : [2, 4, 0, 3, 5, 8, 6, 7]
Answer of del s[3:7:2] : [2, 4, 0, 3, 5, 8, 6, 7]
Answer of del s[3:8:2] : [2, 4, 0, 3, 5, 6, 7]
Answer of del s[3:9:2] : [2, 4, 0, 3, 5, 6, 7]
Answer of del s[3:10:2] : [2, 4, 0, 3, 5, 6]
Answer of del s[4:7:2] : [2, 4, 0, 1, 9, 8, 6, 7]
Answer of del s[4:8:2] : [2, 4, 0, 1, 9, 8, 6, 7]
Answer of del s[4:9:2] : [2, 4, 0, 1, 9, 8, 7]
Answer of del s[4:10:2] : [2, 4, 0, 1, 9, 8, 7]
Answer of del s[5:8:2] : [2, 4, 0, 1, 3, 5, 6, 7]
Answer of del s[5:9:2] : [2, 4, 0, 1, 3, 5, 6, 7]
Answer of del s[5:10:2] : [2, 4, 0, 1, 3, 5, 6]
Answer of del s[6:9:2] : [2, 4, 0, 1, 3, 9, 8, 7]
Answer of del s[6:10:2] : [2, 4, 0, 1, 3, 9, 8, 7]
Answer of del s[7:10:2] : [2, 4, 0, 1, 3, 9, 5, 6]
If k = 3:
Answer of del s[0:4:3] : [4, 0, 3, 9, 5, 8, 6, 7]
Answer of del s[0:5:3] : [4, 0, 3, 9, 5, 8, 6, 7]
Answer of del s[0:6:3] : [4, 0, 3, 9, 5, 8, 6, 7]
Answer of del s[0:7:3] : [4, 0, 3, 9, 8, 6, 7]
Answer of del s[0:8:3] : [4, 0, 3, 9, 8, 6, 7]
Answer of del s[0:9:3] : [4, 0, 3, 9, 8, 6, 7]
Answer of del s[0:10:3] : [4, 0, 3, 9, 8, 6]
Answer of del s[1:5:3] : [2, 0, 1, 9, 5, 8, 6, 7]
Answer of del s[1:6:3] : [2, 0, 1, 9, 5, 8, 6, 7]
Answer of del s[1:7:3] : [2, 0, 1, 9, 5, 8, 6, 7]
Answer of del s[1:8:3] : [2, 0, 1, 9, 5, 6, 7]
Answer of del s[1:9:3] : [2, 0, 1, 9, 5, 6, 7]
Answer of del s[1:10:3] : [2, 0, 1, 9, 5, 6, 7]
Answer of del s[2:6:3] : [2, 4, 1, 3, 5, 8, 6, 7]
Answer of del s[2:7:3] : [2, 4, 1, 3, 5, 8, 6, 7]
Answer of del s[2:8:3] : [2, 4, 1, 3, 5, 8, 6, 7]
Answer of del s[2:9:3] : [2, 4, 1, 3, 5, 8, 7]
Answer of del s[2:10:3] : [2, 4, 1, 3, 5, 8, 7]
Answer of del s[3:7:3] : [2, 4, 0, 3, 9, 8, 6, 7]
Answer of del s[3:8:3] : [2, 4, 0, 3, 9, 8, 6, 7]
Answer of del s[3:9:3] : [2, 4, 0, 3, 9, 8, 6, 7]
Answer of del s[3:10:3] : [2, 4, 0, 3, 9, 8, 6]
Answer of del s[4:8:3] : [2, 4, 0, 1, 9, 5, 6, 7]
Answer of del s[4:9:3] : [2, 4, 0, 1, 9, 5, 6, 7]
Answer of del s[4:10:3] : [2, 4, 0, 1, 9, 5, 6, 7]
Answer of del s[5:9:3] : [2, 4, 0, 1, 3, 5, 8, 7]
Answer of del s[5:10:3] : [2, 4, 0, 1, 3, 5, 8, 7]
Answer of del s[6:10:3] : [2, 4, 0, 1, 3, 9, 8, 6]
If k = 4:
Answer of del s[0:5:4] : [4, 0, 1, 9, 5, 8, 6, 7]
Answer of del s[0:6:4] : [4, 0, 1, 9, 5, 8, 6, 7]
Answer of del s[0:7:4] : [4, 0, 1, 9, 5, 8, 6, 7]
Answer of del s[0:8:4] : [4, 0, 1, 9, 5, 8, 6, 7]
Answer of del s[0:9:4] : [4, 0, 1, 9, 5, 8, 7]
Answer of del s[0:10:4] : [4, 0, 1, 9, 5, 8, 7]
Answer of del s[1:6:4] : [2, 0, 1, 3, 5, 8, 6, 7]
Answer of del s[1:7:4] : [2, 0, 1, 3, 5, 8, 6, 7]
Answer of del s[1:8:4] : [2, 0, 1, 3, 5, 8, 6, 7]
Answer of del s[1:9:4] : [2, 0, 1, 3, 5, 8, 6, 7]
Answer of del s[1:10:4] : [2, 0, 1, 3, 5, 8, 6]
Answer of del s[2:7:4] : [2, 4, 1, 3, 9, 8, 6, 7]
Answer of del s[2:8:4] : [2, 4, 1, 3, 9, 8, 6, 7]
Answer of del s[2:9:4] : [2, 4, 1, 3, 9, 8, 6, 7]
Answer of del s[2:10:4] : [2, 4, 1, 3, 9, 8, 6, 7]
Answer of del s[3:8:4] : [2, 4, 0, 3, 9, 5, 6, 7]
Answer of del s[3:9:4] : [2, 4, 0, 3, 9, 5, 6, 7]
Answer of del s[3:10:4] : [2, 4, 0, 3, 9, 5, 6, 7]
Answer of del s[4:9:4] : [2, 4, 0, 1, 9, 5, 8, 7]
Answer of del s[4:10:4] : [2, 4, 0, 1, 9, 5, 8, 7]
Answer of del s[5:10:4] : [2, 4, 0, 1, 3, 5, 8, 6]
If k = 5:
Answer of del s[0:6:5] : [4, 0, 1, 3, 5, 8, 6, 7]
Answer of del s[0:7:5] : [4, 0, 1, 3, 5, 8, 6, 7]
Answer of del s[0:8:5] : [4, 0, 1, 3, 5, 8, 6, 7]
Answer of del s[0:9:5] : [4, 0, 1, 3, 5, 8, 6, 7]
Answer of del s[0:10:5] : [4, 0, 1, 3, 5, 8, 6, 7]
Answer of del s[1:7:5] : [2, 0, 1, 3, 9, 8, 6, 7]
Answer of del s[1:8:5] : [2, 0, 1, 3, 9, 8, 6, 7]
Answer of del s[1:9:5] : [2, 0, 1, 3, 9, 8, 6, 7]
Answer of del s[1:10:5] : [2, 0, 1, 3, 9, 8, 6, 7]
Answer of del s[2:8:5] : [2, 4, 1, 3, 9, 5, 6, 7]
Answer of del s[2:9:5] : [2, 4, 1, 3, 9, 5, 6, 7]
Answer of del s[2:10:5] : [2, 4, 1, 3, 9, 5, 6, 7]
Answer of del s[3:9:5] : [2, 4, 0, 3, 9, 5, 8, 7]
Answer of del s[3:10:5] : [2, 4, 0, 3, 9, 5, 8, 7]
Answer of del s[4:10:5] : [2, 4, 0, 1, 9, 5, 8, 6]
If k = 6:
Answer of del s[0:7:6] : [4, 0, 1, 3, 9, 8, 6, 7]
Answer of del s[0:8:6] : [4, 0, 1, 3, 9, 8, 6, 7]
Answer of del s[0:9:6] : [4, 0, 1, 3, 9, 8, 6, 7]
Answer of del s[0:10:6] : [4, 0, 1, 3, 9, 8, 6, 7]
Answer of del s[1:8:6] : [2, 0, 1, 3, 9, 5, 6, 7]
Answer of del s[1:9:6] : [2, 0, 1, 3, 9, 5, 6, 7]
Answer of del s[1:10:6] : [2, 0, 1, 3, 9, 5, 6, 7]
Answer of del s[2:9:6] : [2, 4, 1, 3, 9, 5, 8, 7]
Answer of del s[2:10:6] : [2, 4, 1, 3, 9, 5, 8, 7]
Answer of del s[3:10:6] : [2, 4, 0, 3, 9, 5, 8, 6]
If k = 7:
Answer of del s[0:8:7] : [4, 0, 1, 3, 9, 5, 6, 7]
Answer of del s[0:9:7] : [4, 0, 1, 3, 9, 5, 6, 7]
Answer of del s[0:10:7] : [4, 0, 1, 3, 9, 5, 6, 7]
Answer of del s[1:9:7] : [2, 0, 1, 3, 9, 5, 8, 7]
Answer of del s[1:10:7] : [2, 0, 1, 3, 9, 5, 8, 7]
Answer of del s[2:10:7] : [2, 4, 1, 3, 9, 5, 8, 6]
If k = 8:
Answer of del s[0:9:8] : [4, 0, 1, 3, 9, 5, 8, 7]
Answer of del s[0:10:8] : [4, 0, 1, 3, 9, 5, 8, 7]
Answer of del s[1:10:8] : [2, 0, 1, 3, 9, 5, 8, 6]
If k = 9:
Answer of del s[0:10:9] : [4, 0, 1, 3, 9, 5, 8, 6]
++++++++++++++++++++++++ s.append(x) result +++++++++++++++++++++++++
I assume x =8!!!
Answer of del s.append(x): [2, 4, 0, 1, 3, 9, 5, 8, 6, 7, 8]
+++++++++++++++++++++++++ s.clear() result ++++++++++++++++++++++++++
Answer of del s.clear(): []
++++++++++++++++++++++++++ s.copy() result ++++++++++++++++++++++++++
Answer of del s.copy(): [2, 4, 0, 1, 3, 9, 5, 8, 6, 7]
+++++++++++++++++++++++++ s.extend(t) result ++++++++++++++++++++++++
Answer of del s.extend(t): [2, 4, 0, 1, 3, 9, 5, 8, 6, 7, 2, 6, 8, 4]
+++++++++++++++++++++++++++ s += t result +++++++++++++++++++++++++++
Answer of del s += t: [2, 4, 0, 1, 3, 9, 5, 8, 6, 7, 2, 6, 8, 4]
+++++++++++++++++++++++++++ s *= n result +++++++++++++++++++++++++++
I assume n = 2!!!
Answer of del s *= 2: [2, 4, 0, 1, 3, 9, 5, 8, 6, 7, 2, 4, 0, 1, 3, 9, 5, 8, 6, 7]
++++++++++++++++++++++++ s.insert(i,x) result +++++++++++++++++++++++
I assume x =8!!!
Answer of s.insert(i,x): [8, 2, 4, 0, 1, 3, 9, 5, 8, 6, 7]
Answer of s.insert(i,x): [2, 8, 4, 0, 1, 3, 9, 5, 8, 6, 7]
Answer of s.insert(i,x): [2, 4, 8, 0, 1, 3, 9, 5, 8, 6, 7]
Answer of s.insert(i,x): [2, 4, 0, 8, 1, 3, 9, 5, 8, 6, 7]
Answer of s.insert(i,x): [2, 4, 0, 1, 8, 3, 9, 5, 8, 6, 7]
Answer of s.insert(i,x): [2, 4, 0, 1, 3, 8, 9, 5, 8, 6, 7]
Answer of s.insert(i,x): [2, 4, 0, 1, 3, 9, 8, 5, 8, 6, 7]
Answer of s.insert(i,x): [2, 4, 0, 1, 3, 9, 5, 8, 8, 6, 7]
Answer of s.insert(i,x): [2, 4, 0, 1, 3, 9, 5, 8, 8, 6, 7]
Answer of s.insert(i,x): [2, 4, 0, 1, 3, 9, 5, 8, 6, 8, 7]
Answer of s.insert(i,x): [2, 4, 0, 1, 3, 9, 5, 8, 6, 7, 8]
++++++++++++++++++++++++++ s.pop(i) result ++++++++++++++++++++++++++
Answer of s.pop(0): [4, 0, 1, 3, 9, 5, 8, 6, 7] and return 2
Answer of s.pop(1): [2, 0, 1, 3, 9, 5, 8, 6, 7] and return 4
Answer of s.pop(2): [2, 4, 1, 3, 9, 5, 8, 6, 7] and return 0
Answer of s.pop(3): [2, 4, 0, 3, 9, 5, 8, 6, 7] and return 1
Answer of s.pop(4): [2, 4, 0, 1, 9, 5, 8, 6, 7] and return 3
Answer of s.pop(5): [2, 4, 0, 1, 3, 5, 8, 6, 7] and return 9
Answer of s.pop(6): [2, 4, 0, 1, 3, 9, 8, 6, 7] and return 5
Answer of s.pop(7): [2, 4, 0, 1, 3, 9, 5, 6, 7] and return 8
Answer of s.pop(8): [2, 4, 0, 1, 3, 9, 5, 8, 7] and return 6
Answer of s.pop(9): [2, 4, 0, 1, 3, 9, 5, 8, 6] and return 7
+++++++++++++++++++++++++ s.remove(i) result ++++++++++++++++++++++++
Answer of s.remove(0): [2, 4, 1, 3, 9, 5, 8, 6, 7]
Answer of s.remove(1): [2, 4, 0, 3, 9, 5, 8, 6, 7]
Answer of s.remove(2): [4, 0, 1, 3, 9, 5, 8, 6, 7]
Answer of s.remove(3): [2, 4, 0, 1, 9, 5, 8, 6, 7]
Answer of s.remove(4): [2, 0, 1, 3, 9, 5, 8, 6, 7]
Answer of s.remove(5): [2, 4, 0, 1, 3, 9, 8, 6, 7]
Answer of s.remove(6): [2, 4, 0, 1, 3, 9, 5, 8, 7]
Answer of s.remove(7): [2, 4, 0, 1, 3, 9, 5, 8, 6]
Answer of s.remove(8): [2, 4, 0, 1, 3, 9, 5, 6, 7]
+++++++++++++++++++++++++ s.reverse() result ++++++++++++++++++++++++
Answer of s.reverse(): [7, 6, 8, 5, 9, 3, 1, 0, 4, 2]
++++++++++++++++++++++++++ s.sort() result +++++++++++++++++++++++++
Answer of s.sort(): [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
++++++++++++++++++++++++++ s.sort(reverse=True) result +++++++++++++++++++++++++
Answer of s.sort(reverse=True): [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]

Process finished with exit code 0
```

