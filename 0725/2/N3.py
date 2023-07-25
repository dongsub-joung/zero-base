def solution(n: int):
    idx= 1
    while 1:
        triple= pow(idx, 3)
        if triple > n:
            return pow(idx-1, 3)
        idx+=1