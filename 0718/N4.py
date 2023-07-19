def solution(s):
    arr= []
    numbers= ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    
    for number in numbers:
        arr.append(s.count(number))

    return arr.index(max(arr))

print(solution("174771177"))
