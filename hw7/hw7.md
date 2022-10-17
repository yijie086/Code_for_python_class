# Homework 7

## Exercise 2

### 异常处理

#### 题目：

编写程序读入用户在命令行输入的三个`float`类型的数值, 判断它们是否能构成一个三角形的三条边。 若可以, 则使用以下公式计算并输出三角形的面积。公式中的 $a, b, c$ 为三角形的三条边的长度。

$$
\text { area }=\sqrt{s(s-a)(s-b)(s-c)}, s=\frac{a+b+c}{2}
$$

程序应处理以下类型的错误并输出出错信息:
- 用户在命令行输入的参数小于三个;
- 用户在命令行输入的三个参数不全是`float`类型;
- 用户在命令行输入的三个`float`类型的数值不能构成一个三角形的三条边, 这里需要自定义异常 类`InvalidTriangleError`。

#### 源代码：

```python
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
    
```

#### 运行结果：

```terminal
wangyijie@wangyijiedeMacBook-Pro-10 ~/L/M/c/S/杂/p/hw7> python3 hw7_1.py 4.0 3.0 5.0
This is a python code for homework7-2: Triangle
The area of this triangle is: 6.0

wangyijie@wangyijiedeMacBook-Pro-10 ~/L/M/c/S/杂/p/hw7> python3 hw7_1.py 4.0 3.0 a
This is a python code for homework7-2: Triangle
Error: invalid parameters: The third variable is not a float type!

wangyijie@wangyijiedeMacBook-Pro-10 ~/L/M/c/S/杂/p/hw7> python3 hw7_1.py 4.0 3.0
This is a python code for homework7-2: Triangle
Error: invalid parameters: Number of variables is less than 3!

wangyijie@wangyijiedeMacBook-Pro-10 ~/L/M/c/S/杂/p/hw7> python3 hw7_1.py 4.0 3.0 114.514
This is a python code for homework7-2: Triangle
InvalidTriangleError: This triangle can not exists!
Error Information: 3.0 + 4.0 <= 114.514 !

wangyijie@wangyijiedeMacBook-Pro-10 ~/L/M/c/S/杂/p/hw7> python3 hw7_1.py 13.0 5.0 12.0
This is a python code for homework7-2: Triangle
The area of this triangle is: 30.0
```

可见，程序运行正确。

## Exercise 3

#### 文件读写

#### 题目：

编写程序读入一个存储了程序 7.21 的文本文件, 从中提取用户输入的代码然后输出到一个文本文件中。输出的文件的内容应为:

```python
import numpy as np; a = np.arange(1, 16, 2)**2; a
b = a.reshape(2, 4); b
np.savetxt('D:/Python/dat/b.txt', b)
c = np.loadtxt('D:/Python/dat/b.txt'); c
np.save('D:/Python/dat/b.npy', b)
c = np.load('D:/Python/dat/b.npy'); c
np.savez('D:/Python/dat/ab.npz', a, b)
......
```

#### 源代码：

```python
print("This is a python code for homework7-2: Read and Write")
f = open("hw7_2_READ_DAT.txt", encoding="utf-8")
temp = f.read()
f.close()

f = open("hw7_2_WRITE_DAT.txt", mode="w", encoding="utf-8")
f.write(temp)
f.close()
```

#### 运行结果：

输入文件为`hw7_2_READ_DAT.txt`，运行程序：

```terminal
wangyijie@wangyijiedeMacBook-Pro-10 ~/L/M/c/S/杂/p/hw7 [1]> python3 hw7_2.py
This is a python code for homework7-2: Read and Write
```

得到输出文件`hw7_2_WRITE_DAT.txt`，其内容为：

```python
import numpy as np; a = np.arange(1, 16, 2)**2; a
b = a.reshape(2, 4); b
np.savetxt('D:/Python/dat/b.txt', b)
c = np.loadtxt('D:/Python/dat/b.txt'); c
np.save('D:/Python/dat/b.npy', b)
c = np.load('D:/Python/dat/b.npy'); c
np.savez('D:/Python/dat/ab.npz', a, b)
......
```

可见，程序运行正确。
