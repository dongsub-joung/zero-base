def solution(S: str):
    answer= 0.00
    operator= ["+", "-", "*", "/"]
    for e in S:
        if e in operator:
            if e == '*':
                answer*= e
            elif e == '/':
                answer/= e
            elif e == '+':
                answer+= e
            elif e == '-':
                answer-= e
        else:
            answer+= int(e)

print(solution("2*3+5/6*3+15"))
