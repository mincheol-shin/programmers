def solution(n):
    num = list(str(n))
    answer = [int(i) for i in num[-1:: -1]]
    return answer

