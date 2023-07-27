# 1 런타임 에러
def solution(n: list):
    n.sort()
    while 1:
        a= n.pop()
        b= n.pop()
        if a>b:
            n.append(a-b)
        elif a<b:
            n.append(b-a)
        n.sort()
        if len(n) == 0:
            return 0
        if len(n) <= 1:
            break

    return n.pop()