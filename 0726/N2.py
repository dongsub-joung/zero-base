def solution(nums: list):
    answer= []
    for i in range(1, len(nums)+1):
        if nums.count(i) == 0:
            answer.append(i)

    return answer