import sys

input= sys.stdin.readline

i,j= map(int, input().split())

array= []
s_array= []
for _ in range(i):
    s_array= list(map(int, input().split()))
    array.append(s_array)

k= int(input())

sum_array=[]
for _ in range(k):
    a,b,c,d= map(int, input().split())
    suming= 0
    for frist in range(a, c):
        for sec in range(b, d):
            print(f"a:{a} b: {b}")
            suming+= array[frist][sec]
    
    sum_array.append(suming)

for e in sum_array:
    print(e)
