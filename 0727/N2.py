def solution(nums: list, n: int):
    answer = 0
    for e in nums:
        if e == n:
            return answer
        answer+=1
    return -1