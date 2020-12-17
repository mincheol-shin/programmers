def solution(dartResult):
    num = []
    point = 0
    i = 0

    while i < len(dartResult):
        result = dartResult[i]
        if result.isnumeric():
            num.append(point)
            if result == '1':
                if dartResult[i + 1] == '0':
                    point = 10
                    i += 1
                else:
                    point = 1
            else:
                point = int(result)
        else:
            if result == 'S':
                point = point ** 1
            elif result == 'D':
                point = point ** 2
            elif result == 'T':
                point = point ** 3
            elif result == '*':
                if len(num) > 1:
                    num[len(num) - 1] = num[len(num) - 1] * 2
                point = point * 2
            elif result == '#':
                point = point * -1
        i += 1

    num.append(point)

    return sum(num)


# 일부 테스트 케이스 실패 후 해당 테스트 케이스로 원인 분석
# solution("0T2T0T")
