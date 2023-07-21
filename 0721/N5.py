def solution(s):
    answer = ''
    for char in s:
        if char >= chr(97):
            answer+= char.upper()
        else:
            answer+= char.lower()
    return answer

print(solution("Naver"))