# https://www.acmicpc.net/problem/2830
# 행성 X3 

#https://singun11.tistory.com/29
import sys
n= int(sys.stdin.readline())
L= [int(sys.stdin.readline()) for i in range(n)]

D= [0]*30

for i in L:
    cnt=0
    while k > 0:
        D[cnt] += k % 2
        k//=2
        cnt+=1

ans= 0
c= 1
for i in D:
    ans+= c*(i*(n-i))
    c*=2

print(ans)

# https://gukin.tistory.com/14
# https://velog.io/@wellsbabo/%ED%96%89%EC%84%B1-X3%EB%B0%B1%EC%A4%802830%EB%B2%88