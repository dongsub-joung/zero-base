import sys

input= sys.stdin.readline

coins= []
answer= 0

N, K= map(int, input().split())

for _ in range(N):
    coins.append(int(input()))

coins.sort(reverse=True)

for coin in coins:
    if K >= coin:
        answer+= K
        K%= coin
        
        if K<= 0:
            break

print(answer)
