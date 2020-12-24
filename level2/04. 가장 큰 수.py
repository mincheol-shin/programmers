from itertools import permutations


def solution(numbers):
    max_num = 0
    # max 함수를 제거
    # 시간 초과 (시간 복잡도가 똑같을 것)
    for i in permutations(numbers):
        num = int("".join(list(map(str, list(i)))))
        if max_num < num:
            max_num = num
    return str(max_num)

