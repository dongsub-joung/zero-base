def solution(A: list, K: int)->int:
    cnt= 0
    A.sort()
    for e in A:
        K-=e
        if K<0:
            break 
        cnt+=1
    return cnt
