def solution(s: str) -> str:
    #1 clear
    #append e

    buff= []

    for c in s:
        buff.append(c)
        if c == 1:
            buff.clear()
        if buff.count(0) >= 4:
            return "NO"
    return "YES"
