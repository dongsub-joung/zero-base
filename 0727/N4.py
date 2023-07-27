def solution(n):
    answer= 0
    idx= 1
    while 1:
        answer+= pow(2,idx)
        idx+=1
        if idx == n:
            break
    return answer+1 % 1000000007

