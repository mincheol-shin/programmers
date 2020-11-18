import collections


def solution(s):
    result = collections.Counter(s.lower())
    return True if result['y'] == result['p'] else False
