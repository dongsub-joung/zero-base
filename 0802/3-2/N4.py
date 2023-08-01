def solution(matrix: list, b: bool)->bool:
    for arr in matrix:
        for e in arr:
            if e != b:
                return False
    return True
