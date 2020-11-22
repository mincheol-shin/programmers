import collections


def solution(n):
    answer = [True for i in range(2, n + 3)]
    for i in range(2, len(answer)):
        if answer[i]:
            for j in range(i * 2, n + 1, i):
                answer[j] = False

    return dict(collections.Counter(answer))[True] - 2
