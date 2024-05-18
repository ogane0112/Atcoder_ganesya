s = (input())
s_list = list(s)

if "".join(sorted(s_list)) == "abc":
    print("Yes")
else:
    print("No")
    