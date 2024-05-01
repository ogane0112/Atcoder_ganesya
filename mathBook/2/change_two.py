#2進数に変換する関数
def change_two(num):
    ans = []
    while 1 <= num:
        temp = num%2
        #answer用のリストに格納する
        ans.append(temp)
        #2で割って更新
        num = num/2
    return ans[::-1]
        
ans = change_two(7)
print(ans)