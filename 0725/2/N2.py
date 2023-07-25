def solution(arr: list):
    answer= []
    size= len(arr)
    for e in arr:
        answer.append(e)
        if e % 2 != 0:
            answer.append(e)
    
    while 1:
        answer.pop()
        if size == len(answer):
            break
              
    return answer