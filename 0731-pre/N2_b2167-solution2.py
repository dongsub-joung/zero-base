import sys

input= sys.stdin.readline

left, right= 0, 1
cnt= 0

N,M= map(int, input().split())
nums= list(map(int, input().split()))

while right <= N and left <= right:
    sum_nums= nums[left:right]
    total= sum(sum_nums)

    if total == M:
        cnt+=1 
        right+=1
    elif total < M:
        right+=1
    else:
        left+=1

print(cnt)
