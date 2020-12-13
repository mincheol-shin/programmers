import itertools


def solution(d, budget):
    count = 0
    for i in range(1, len(d) + 1):
        case = list(itertools.permutations(d, i))
        for j in case:
            if sum(j) <= budget:
                count += 1
                break
    return count
