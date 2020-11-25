def solution(s, n):
    answer = ""
    for i in s:
        if i != ' ':
            value = ord(i) + n
            if i.isupper():
                if value > 90:
                    num = value - 90
                    answer += chr(64 + num)
                else:
                    answer += chr(value)
            else:
                if value > 122:
                    num = value - 122
                    answer += chr(96 + num)

                else:
                    answer += chr(value)
        else:
            answer += ' '

    return answer
