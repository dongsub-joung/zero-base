import sys

def solution(numbers, direction):
    if direction == "right":
        numbers.insert(0, numbers.pop())
    elif direction == "left":
        numbers.append(numbers.pop(0))
    return numbers

# 3,1,2
print(solution([1,2,3], "right"))