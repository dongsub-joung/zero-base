def solution(arr):
    if arr[1] > arr[2] and arr[1] > arr[3]:
        return "NO"
    if arr[1] < arr[2] and arr[1] < arr[3]:
        return "YES"
    return "NO"