def solution(arr: list)->int:
    answer= []
    cnt= 0
    for i in range(len(arr)):
        for j in range(1, len(arr)-1):
            if arr[i] == 1 and arr[j] == 1:
                cnt+= (arr[i] + arr[j])
    return cnt

print(solution([1,0,1,1,1,0]))