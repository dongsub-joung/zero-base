def solution(arr):
    answer = 0
    for i in range(len(arr)):
        for j in range(1, len(arr)):
            answer= bin(int(arr[i]), 2) ^ bin(int(arr[j], 2))
    return int(answer, 2)

solution({"10110", "1010", "11110"})