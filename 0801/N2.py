def solution(arr:list):
    cnt= 0
    avg= sum(arr)//len(arr)
   
    if avg == 0:
        return len(arr)

    for e in arr:
        if avg<=e:
            cnt+=1

    return cnt
