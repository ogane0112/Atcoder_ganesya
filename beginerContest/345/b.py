x = int(input())
float_x = x/10
if x%10 == 0:
    print(int(float_x))
elif x > 0:
    ans = int(int(float_x)+1)
    print(ans)
else:
    print(int(float_x))
