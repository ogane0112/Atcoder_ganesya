n,t = map(str,input().split())
n = int(n)
s_list = []
ans = []
t_list = list(t)

for i in range(n):
    s = input()
    s_list.append(s)

for i in range(n):
    for j in range(len(s_list[i])):
        if s_list[i] == t:
            ans.append(i+1)
        elif t_list[i] == s_list[i][j]:
            
