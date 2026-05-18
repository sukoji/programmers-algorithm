def solution(n):
    return sum(num for num in range(2, n+1) if num % 2 == 0)
