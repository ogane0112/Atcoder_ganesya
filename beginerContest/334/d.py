n,q = map(int,input().split())
r_list = list(map(int,input().split()))
sort_list = sorted(r_list)
#クエリ毎に処理する
#貪欲法で実装してみる
def search(list,target):
    count = 0
    a = 0
    for i in list:     
        a += i
        if a > target:
            break
        count += 1
    return count
        
for i in range(q):
    x = int(input())
    count = search(sort_list,x)
    print(count)
    
    