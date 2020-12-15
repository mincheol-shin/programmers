def solution(n, arr1, arr2):
    sum_map = ["{0:0{1}d}".format(int("{0:016b}".format(arr1[i])) + int("{0:016b}".format(arr2[i])), n) for i in
               range(0, len(arr1))]
    answer = []
    for i in sum_map:
        value = i.replace('1', '#')
        value = value.replace('0', ' ')
        value = value.replace('2', '#')
        answer.append(value)
    return answer
