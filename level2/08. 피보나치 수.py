def solution(n):
    answer = [0, 1]
    for i in range(0, n):
        answer.append(answer[i]+answer[-1])

    return answer[n] % 1234567

