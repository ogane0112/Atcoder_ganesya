n,k = map(int,input().split())
s = input()
s_list = list(s)
ans = []
# アルファベットのリストを作成する
alphabets = list(map(chr, range(97, 123)))
count = 0
# A...Zを探索する
for j in alphabets:
    for i in s_list:
        if len(ans) == k:
            break
        if i == j:
            ans.append(i)
            #探索した要素まで削除してリストを更新
            count += 1
            s = s[count:n]
            continue
        count += 1

print(*ans)       
for _ in ans:
    print(_,end="")

