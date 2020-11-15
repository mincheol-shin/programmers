def solution(arr, divisor):
    result = [i for i in arr if i % divisor == 0]

    return sorted(result) if len(result) > 0 else [-1]


solution([2, 36, 1, 3], 1)
