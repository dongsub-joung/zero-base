# https://campkim.tistory.com/13
# DFS

import sys

input= sys.stdin.readline
sys.setrecursionlimit(1000000)

N= int(input())
visited= [False] * (N+1)
anser= [
