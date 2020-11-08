def solution(n, lost, reserve):
    lost_student = []

    for value in lost:
        if value in reserve:
            reserve.remove(value)
        else:
            lost_student.append(value)

    for value in lost_student:
        if value - 1 in reserve:
            reserve.remove(value - 1)
        elif value + 1 in reserve:
            reserve.remove(value + 1)
        else:
            n -= 1
    return n
