def solution(arr):
    result = [] 
    for num in arr:
        if not result or num != result[-1]: 
            result.append(num) 
    return result