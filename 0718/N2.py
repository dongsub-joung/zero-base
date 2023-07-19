# 모래 나누기 1,2,3 
def solution(num):
    while(num > 1):
        if num % 3 == 1:
            num-=3
        elif num % 2 == 1:
            num-=2
        else:
            num-=1

        if num == 1:
            return False
        else:
            return True

    return False
