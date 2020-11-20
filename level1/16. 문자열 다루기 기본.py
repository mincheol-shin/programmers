def solution(s):
    s_length = len(s)

    if s_length == 4 or s_length == 6:
        return s.isdigit()
    else:
        return False
