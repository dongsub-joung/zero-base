def solution(arr: list, prefix: str, separator: str, postfix: str)->str:
    answer = ''+prefix
   
    arr= list(map(str, arr))
    answer+= separator.join(arr)

    return answer+postfix

print(solution([1,3,0,7,9], "<", ",", ">"))
