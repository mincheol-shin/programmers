import math


def solution(progresses, speeds):
    working_period = [math.ceil((100 - progresses[i]) / speeds[i]) for i in range(0, len(progresses))]
    answer = []
    distribution = 0
    for i in working_period:
        if i > distribution:
            distribution = i
            answer.append(1)
        else:
            answer[len(answer) - 1] += 1
    return answer
