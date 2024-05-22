n = int(input())
maxValue = 1
for i in range(2,int(n**0.5)+1):
    power = i * i
    while power <= n:
        maxValue = max(maxValue,power)
        power *= i
print(maxValue)
