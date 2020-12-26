def solution(numbers):
    # 일부 테스트 케이스 오류
    numbers.sort(key=lambda x: x * (100 / (10 ** len(str(x)))), reverse=True)
    return str(int("".join(map(str, numbers))))


