# ?? 1st try
# def solution(arr):
#     i, j, k= 0,1,2
#     max= 0
#     for e in len(arr-2):
#         sumed= arr[i] + arr[j] + arr[k]
#         if sumed > max:
#             max= sumed
#         i+=1
#         j+=1 
#         k+=1


def solution(arr):
    arr.sort()
    return sum(arr[-3:])
print(solution([6,2,12,8,5,9]))