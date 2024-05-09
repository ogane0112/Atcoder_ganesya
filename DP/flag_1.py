n = int(input())
a_list = list(map(int,input().split()))

#dp用の配列を宣言する
dp = [0]*1000000

for i in range(n):
    #例題での1から1への移動を表現している
    if i == 0:
        dp[0] = 0
    #out of rangesになるので下の処理がいる
    elif i == 1:
        dp[1] = abs(a_list[1]-a_list[0])
        
    else:
        v1 = dp[i-1]+abs(a_list[i-1]-a_list[i])
        v2 = dp[i-2]+abs(a_list[i-2]-a_list[i])
        dp[i] = min(v1,v2)
        
print(dp[n-1])