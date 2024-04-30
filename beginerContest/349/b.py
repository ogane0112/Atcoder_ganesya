n = input()
flag = True
count_dict = {i:0 for i in range(1, 101)}
unique = set(n)

for i in unique:
  count_str = n.count(i)
  count_dict[count_str] +=1

for key,value in count_dict.items():
    if value != 2 and value != 0:
        flag = False
       
        break

if flag:
    print("Yes")
else:
    print("No")
    