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
