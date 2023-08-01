def solution(arr: list, n: int)->int:
    answer = -1

    for e in arr:
        if n >= e:
            answer= e

    return answer
