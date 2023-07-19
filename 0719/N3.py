import math

def solution(A):
    ans= 0
    for i in range(len(A)-1):
        ans= math.gcd(A[i], A[i+1])
    return ans;