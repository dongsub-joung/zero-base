def solution(arr):
    arr.sort()
    arr.pop(0)
    arr.pop()
    return sum(arr) // len(arr)