def solution(s):
    s_length = int(len(s) / 2)

    return s[s_length - 1: s_length + 1] if len(s) % 2 == 0 else s[s_length:s_length + 1]
