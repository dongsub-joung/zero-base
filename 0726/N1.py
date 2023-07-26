def solution(s):
    dictionaly= {}
    answer= []
    for e in s:
        dictionaly[e]= s.count(e)
    
    sorting= sorted(dictionaly.items(), key= lambda x : x[1], reverse=True)
    for i,j in sorting:
        answer.append(int(i))
    
    for i in range(10):
        if answer.count(i) == 0:
            answer.append(i)
    answer= map(str, answer)
    result= " ".join(answer)
    return result

