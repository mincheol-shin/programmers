def solution(arr):
    if len(arr) > 1:
        min_num = arr[0]
        for i in arr[1:]:
            if i < min_num:
                min_num = i

        arr.remove(min_num)
        return arr
    else:
        return [-1]



