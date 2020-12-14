def solution(N, stages):
    failure_late = {}
    for stage in range(1, N + 1):
        people = 0
        failed_people = 0
        for challenge_stage in stages:
            if stage == challenge_stage:
                failed_people += 1
                people += 1
            elif stage < challenge_stage:
                people += 1

        failure_late[stage] = failed_people / people if people != 0 else 0
    answer = sorted(failure_late.items(), reverse=True, key=lambda x: x[1])
    return [i[0] for i in answer]
