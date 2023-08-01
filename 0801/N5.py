def solution(n: int, price: int) -> int:
    free= n // 10
    return int(n-free) * price
