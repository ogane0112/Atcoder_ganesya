s = input()
list_s = list(s)
set_s = list(set(s))
num = len(set_s)
set_s = sorted(set_s)
max = 0
ans = 0
for i in range(num):
    count = list_s.count(set_s[i])
    if max < count:
        ans = i
        max = count
print(set_s[ans])


