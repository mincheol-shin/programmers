def solution(seoul):
    answer = [i for i in range(0, len(seoul)) if seoul[i] == "Kim"][0]
    return "김서방은 {0}에 있다".format(answer)
