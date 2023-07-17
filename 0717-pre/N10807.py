# https://www.acmicpc.net/problem/10807
# 개수 세기

n= int(input())
arr= list(map(int, input().split()))
v= int(input())
cnt= 0

for e in arr:
    if e == v:
        cnt+=1

print(cnt)
