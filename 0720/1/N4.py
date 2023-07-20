# 두자리 숫자 처리를 못함
# def solution(s):
#     operators= []
#     numbers= []

#     for char in s:
#         if char == '+' or char == '-':
#             operators.append(char)
#         else:
#             numbers.append(int(char))


def solution(s):
    operators= []
    numbers= []
    buf= ""

    for e in s:
        if e == '-' or e == '+':
            pass
        else:
            buf+=e;

solution("-3+26-7") 