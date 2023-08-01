def solution(arr: list):
    cnt_list= []
    
    seted= set(arr)
    
    for e in seted:
        cnt_list.append(arr.count(e))

    cnt_list.sort()
    pre= -1
    for i in cnt_list[::-1]:
        if pre == i:
            return False
        pre= cnt_list.pop()
    return True
