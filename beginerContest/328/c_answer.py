#!/usr/bin/env python3
# from typing import *


# def solve(N: int, Q: int, S: str, l: List[int], r: List[int]) -> List[str]:
def solve(N, Q, S):
    bit_ary = [] 
    sum_ary = []
    for i in range(N -1):
        if S[i+1] == S[i]:
            bit_ary.append(1)
        else:
            bit_ary.append(0)

    for i in range(N):
        if i == 0:
            sum_ary.append(0)
        else:
            sum_ary.append(sum_ary[i-1] + bit_ary[i-1])

    for q in range(Q):
        l, r = map(int, input().split())
        cnt = sum_ary[r-1] - sum_ary[l -1]
        print(cnt)

    return None



# generated by oj-template v4.8.1 (https://github.com/online-judge-tools/template-generator)
def main():
    N, Q = map(int, input().split())
    S = input()
    a = solve(N, Q, S)


if __name__ == '__main__':
    main()