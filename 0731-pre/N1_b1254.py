import sys

input= sys.stdin.readline

S= input()

for i in range(len(S)):
  if S[i:] == S[i:][::-1]:
    print(len(S)+i)
    break

# Anyway, let's cross the str whether thats a palindrome
#str_size= len(S)
#print(S[:str_size]) 
#print(S[str_size+1:])

