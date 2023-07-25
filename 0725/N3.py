def solution(p, s):
    count_arr= []
    count_arr2= []
    for e in p:
        count_arr.append(p.count(e))
    s_arr= list(s.split(" "))
    for e in s_arr:
        count_arr2.append(s_arr.count(e))
    if sum(count_arr) == 0 and sum(count_arr2) == 0:
        return True
    else:
        return False
