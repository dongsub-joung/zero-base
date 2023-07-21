def solution(s):
    ans= []
    answer = ''
    max= 0

    for e in s:
        ans.append((e, s.count(e)))
    
    for k,v in ans:
        if v > max:
            max= v
            answer= k
        
    return answer
# solution("google")