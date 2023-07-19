# 주식 매수 문제
# stack

# 1st
def solution(A):
    max_income= 0
    income=0
    
    for stock in A:
        for i in range(len(stock)):
            income= stock - A[i]

            if income > 0:
                if max_income < income:
                    max_income= income
            
    return max_income


def solution2(A):
    max_income= 0

    for i in range(len(A)):
        for j in range(i, len(A)):
            income= A[i] - A[j]

            if income >= 0:
                if max_income <= income:
                    max_income= income
            else:
                max_income= 0
    return max_income