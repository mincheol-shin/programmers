from itertools import permutations


def solution(numbers):
    answer = []

    # 시간 초과
    # idea : 앞자리 숫자를 비교?
    for i in permutations(numbers):
        answer.append("".join(list(map(str, list(i)))))

    return str(max(answer))
