import math
import sys
n,l,r = map(int,input().split())
#質問回数
num = math.ceil((r-l+1)//2)

def query(i, j):
        print(f"? {i} {j}")
        sys.stdout.flush()
        return int(input().strip())
total_sum = 0
query_i = r

for i in range(num):
    
    
