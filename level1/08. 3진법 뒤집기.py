def solution(n):
    result = []
    while n > 0:
        n, mod = divmod(n, 3)
        result.append(str(mod))
    return int("".join(result), base=3)


solution(45)
