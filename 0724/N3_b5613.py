import sys

input= sys.stdin.readline

# try 1
ans= 0
buff= []
global inputed
while True:
    inputed= input()
    buff.append(inputed)
    if inputed == '=':
        break

for e in buff:
    if e == '+':
        ans+= e
    elif e == '-':
        ans-= e
    elif e == '*':
        ans*= e
    elif e == '/':
        ans//= e
    elif e == '=':
        break
    else:
        ans+= int(e)

print(ans)


# https://star7sss.tistory.com/699

frist= int(input())
while 1:
    inputed= input()
    if inputed == '=':
        break
    n= int(input())
    if inputed  == '+':
        frist+= n
    elif inputed == '-':
        frist-= n
    elif inputed == '*':
        frist*= n
    elif inputed == '/':
        frist//= n
print(frist)