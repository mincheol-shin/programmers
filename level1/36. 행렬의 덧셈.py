def solution(arr1, arr2):
    answer = []
    for i in range(0, len(arr1)):
        sum_matrix = []
        for j in range(0, len(arr1[i])):
            sum_matrix.append(arr1[i][j] + arr2[i][j])

        answer.append(sum_matrix)

    return answer

