def solution(s):

    if s.isnumeric():
        return int(s)
    else:
        if s[0] == '+':
            return int(s)
        else:
            return int(s[1:len(s)]) * -1


print(solution("-1234"))