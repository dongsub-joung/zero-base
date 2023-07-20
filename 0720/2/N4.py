def solution(s):
    decimal= int(s, 16)
    ans= bin(decimal)
    return ans[2:]
