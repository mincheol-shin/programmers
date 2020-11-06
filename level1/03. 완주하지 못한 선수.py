import collections


def solution(participant, completion):
    return list(collections.Counter(participant) - collections.Counter(completion))[0]


