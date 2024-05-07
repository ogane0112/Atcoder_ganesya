n = int(input())
d_list = list(map(int,input().split()))
count = 0
for i in range(n):
    num = len(set(list(str(i))))
    if i+1 <= d_list[i] and  num == 1:
        count += 1
    if 11*(i+1) <= d_list[i] and num == 1:
        count += 1

print(count)