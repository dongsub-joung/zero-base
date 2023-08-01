# https://velog.io/@heyksw/Python-%EB%B0%B1%EC%A4%80-silver-1890%EB%B2%88-%EC%A0%90%ED%94%84

import sys

input= sys.stdin.readline
sys.setrecursionlimit(10**6)

N= int(input())
graph= []

for _ in range(N):
    graph.append(list(map(int, input().split())))

direction= [(1,0), (0,1)]
dp= [[0 for _ in range(N+1)] for _ in range(N)]
dp[0][0]= 1

for x in range(N):
    for y in range(N):
        if x == y == N-1:
            print(dp[x][y])
            exit(0)
        
        dist= graph[x][y]

        if x + dist < N:
            dp[x + dist][y]+= dp[x][y]

        if y + dist < N:
            dp[x][y + dist]+= dp[x][y]
