#約数列挙を実装していく
a,b,c = map(int,input().split())
num  = int(c**0.5)+1
check_list = []
count = 0

for i in range(1,num+1):
    if c%i != 0:
        continue
    if c%i == 0:
        check_list.append(i)
        if c//i != i:
            check_list.append(c//i)
check_list = list(set(check_list))
for i in check_list:
    if a <= i <=b:
        count += 1     
print(count)