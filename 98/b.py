n = int(input())
s = input()
s_list = list(s)
max_unique = 0
for i in range(n):
  unique = 0
  
  left = s_list[:i]
  right = s_list[i:]
  for i in list(set(left)):
    for j in list(set(right)):
      if i == j:
        unique += 1
  max_unique = max(max_unique,unique)
print(max_unique)