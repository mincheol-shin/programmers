def solution(numbers):
    answer = sorted(list(set([numbers[x] + y for x in range(0, len(numbers)) for y in numbers[x+1:]])))
    return answer


solution([2, 1, 3, 4, 1, 30, 500, 30])
