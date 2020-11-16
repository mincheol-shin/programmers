def solution(a, b):
    answer = 0
    value = sorted([a, b])
    for i in range(value[0], value[1] + 1):
        answer += i
    return answer


solution(3, 5)
