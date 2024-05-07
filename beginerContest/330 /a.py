n,l = map(int,input().split())
a_list = list(map(int,input().split()))
count = 0

for i in a_list:
    if i > l:
        count += 1

print(count)