def solution(prices):
    answer = []

    for i in range(0, len(prices)):
        price = prices[i]
        count = 0
        is_down = False
        for j in range(i + 1, len(prices)):
            count += 1
            if price > prices[j]:
                answer.append(count)
                is_down = True
                break

        if not is_down:
            answer.append(len(prices) - (i + 1))
    return answer


solution([1, 2, 3, 2, 3])
