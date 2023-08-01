def solution(arr1: list, arr2: list)->list:
    answer = []
    for e in arr1:
        for e2 in arr2:
            if e == e2:
                answer.append(e)
    return list(reversed(answer))

print(solution([1,3,6,9,12], [2,4,6,8,10,12]))
