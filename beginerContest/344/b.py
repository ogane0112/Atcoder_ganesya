a_list = []
for i in range(100):
    try:
        a_list.append(int(input()))
    except:
        break
    
a_list_reverse = a_list[::-1]

for i in a_list_reverse:
    print(i)
    
    