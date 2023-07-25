# 4, 5 실패 > 뭔지 모름

def solution(num: int):
    if -100000 >= num  and num >= 100000:
        return 0
    flag= False
    if num < 0:
        flag= True
        num*= -1
    
    reversed= str(num)[::-1]
    
    if flag:
        return -1 * int(reversed)
    else:
        return int(reversed)
