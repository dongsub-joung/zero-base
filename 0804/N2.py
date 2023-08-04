def solution(A: list)->int:
    max_int, buff= 0, 0

    for e in A:
        buff+=e
        if max_int < buff:
            max_int= buff       
    if max_int< 0:
        return 0

    return max_int


# def solution(A: list)->int:
#     answer= []
#     for i in range(len(A)+1):
#         for j in range(len(A)+1):
#             buff= 0
#             for e in answer[i:j]:
#                 buff+=e
#             # answer.append(sum(answer[i:j])) --x
#             answer.append(buff)

#     answer= max(answer)
    
#     if answer< 0:
#         return 0

#     return answer