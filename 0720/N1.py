
def solution(s):
    for i in range(len(s)):
        for j in range(1, len(s)):
            if s[i] == s[j]:
                s= s.replace(s[i], "")
    return s 

# 단순하게 생각
# def solution(s):
#     listing= list(s)
#     return list(set(listing))

print(solution("aacddefg"))