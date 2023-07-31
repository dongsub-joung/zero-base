# java version solution blog
# https://wooooozin.tistory.com/entry/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-%ED%95%9C-%EB%B2%88%EB%A7%8C-%EB%93%B1%EC%9E%A5%ED%95%9C-%EB%AC%B8%EC%9E%90

import sys

input= sys.stdin.readline

s= input()
buff= []
for char in s:
    cnt= s.count(char)
    if cnt == 1:
        buff.append(char)

duplicated= list(set(buff))
duplicated.sort()

ans= ""
for e in duplicated:
    ans+=e

print(ans)