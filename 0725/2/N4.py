def solution(arr: list):
    for e in arr:
        if arr.count(e) != 2:
            return e
    return 0