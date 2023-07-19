def solution(s):
    strs= []
    ans= []
    full_char_list= list(s)

    for i in range(len(s)):
        for j in range(1, len(s)):
            if full_char_list[i] in '!'or full_char_list[i] in '?' or full_char_list[i] in '.' or full_char_list[i] in  ',' or full_char_list[i] in  ' ':
                if full_char_list[i] == '!' or full_char_list[i] == '?' or full_char_list[i] == '.' or full_char_list[i] == '.' or full_char_list[i] == ' ':
                    s.replace(full_char_list[i], " ")

    strs= s.split()
    strs= s.split('!')
    strs= s.split('?')
    strs= s.split('.')
    strs= s.split(',')

    for string in strs:
        char_list= list(string)
        char_list.reverse()
        joined_string= ''.join(char_list)
        ans.append(joined_string)

    print(ans)
    
solution("Hello, World!?")
    