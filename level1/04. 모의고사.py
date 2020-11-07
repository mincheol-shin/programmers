def solution(answers):
    answer = []
    max_score = 0
    student = [
        {'pattern': [1, 2, 3, 4, 5], 'right_answer': 0},
        {'pattern': [2, 1, 2, 3, 2, 4, 2, 5], 'right_answer': 0},
        {'pattern': [3, 3, 1, 1, 2, 2, 4, 4, 5, 5], 'right_answer': 0},
    ]

    for i in range(0, len(answers)):
        for j in range(0, 3):
            if student[j]['pattern'][i % len(student[j]['pattern'])] == answers[i]:
                student[j]['right_answer'] += 1

    for i in range(0, 3):
        if student[i]['right_answer'] > max_score:
            answer = []
            max_score = student[i]['right_answer']
            answer.append(i + 1)
        elif student[i]['right_answer'] == max_score:
            answer.append(i + 1)
    return answer


