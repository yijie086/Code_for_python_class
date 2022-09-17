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
