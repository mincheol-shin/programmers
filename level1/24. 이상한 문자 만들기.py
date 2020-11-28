def solution(s):
    words = s.split(' ')

    for i in range(0, len(words)):
        word = words[i]
        temp = ""
        for j in range(0, len(word)):
            if j % 2 == 0:
                temp += word[j].upper()
            else:
                temp += word[j].lower()
        words[i] = temp

    return " ".join(words)



