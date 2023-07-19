def solution(S):
    cnt= 0
    s= int(S, 2)
    while(s != 0):
        if(s % 2 != 0):
            s-= 1
        else:
            s= s << 1
        cnt+=1
    return cnt

