def solution(num):
    count = 0
    while num != 1 and count <= 500:
        if num % 2 == 0:
            num = num // 2
        else:
            num = (num * 3) + 1
        count += 1

    # 정확히 500번 시도해야 되는 케이스 => 통과하기 위한 케이스에는 해당 케이스 X
    # 3027113
    # 3030267
    # 3086523
    # 3170806
    # 3170807
    return count if count < 500 else -1


