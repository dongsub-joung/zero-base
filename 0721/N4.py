def solution(n):
    ans= n**(1/2)
    for i in range(2, int(ans)+1):
        if ans%i != 0:
            return 0
    return ans
