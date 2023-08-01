def solution(s: str, n: int)->int:
    cnt= 0
    n_str= str(n)
    
    for c in s:
        if c == n_str:
            cnt+=1
    return cnt
