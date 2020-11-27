def solution(n):
    answer = []

    for i in range(1, int((n + 2) / 2)):
        if n % i == 0:
            answer.insert(0, n // i)
    answer.insert(0, 1)
    return sum(answer) if n != 0 else 0

