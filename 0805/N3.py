def solution(A: list):
    min_num=0
    min_arr=[]
    # fail solution, misread
    for arr in A:
        min_num= min(arr) 
        min_arr.append(min_num)
    return sum(min_arr)
