def solution(arr1: list, arr2: list):
    ans= []
    for e in arr1:
        if arr2.count(e) >= 1:
            ans.append(e)
            ans.sort()
    return ans