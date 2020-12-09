def solution(x):
    num = 0
    for i in list(str(x)):
        num += int(i)

    return True if x % num == 0 else False

