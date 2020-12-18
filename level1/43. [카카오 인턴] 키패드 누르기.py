def solution(numbers, hand):
    left = ['1', '4', '7', '*']
    right = ['3', '6', '9', '*']
    common = ['2', '5', '8', '0']

    left_hand = [3, 0]
    right_hand = [3, 2]
    answer = ""
    for i in numbers:
        num = str(i)

        if num in left:
            answer += 'L'
            left_hand = [left.index(num), 0]
        elif num in right:
            answer += 'R'
            right_hand = [right.index(num), 2]
        else:
            location = [common.index(num), 1]

            left_distance = sum([abs(left_hand[0] - location[0]), abs(left_hand[1] - location[1])])
            right_distance = sum([abs(right_hand[0] - location[0]), abs(right_hand[1] - location[1])])
            if left_distance > right_distance:
                answer += 'R'
                right_hand = location
            elif left_distance < right_distance:
                answer += 'L'
                left_hand = location
            else:
                if hand == "left":
                    answer += 'L'
                    left_hand = location
                else:
                    answer += 'R'
                    right_hand = location
    print(answer)

solution([1, 2, 3, 4, 5, 6, 7, 8, 9, 0], 'right')
