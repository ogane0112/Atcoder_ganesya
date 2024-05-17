from collections import defaultdict
s = defaultdict(int)
n = int(input())

for i in range(n):
    temp = input()
    s[temp] += 1 
m = int(input())
for i  in range(m):
    temp = input()
    s[temp] -= 1

print(max(s.values()))
