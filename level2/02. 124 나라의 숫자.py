def solution(n):
    num = ['4', '1', '2']
    answer = ""

    while n >= 1:
        answer += num[int(n % 3)]
        n = (n - 1) / 3

    return answer[-1::-1]
