def solution(s):
    answer = list(map(int, s.split(" ")))
    return "{0} {1}".format(min(answer), max(answer))

