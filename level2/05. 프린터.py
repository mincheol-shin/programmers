from queue import Queue


def solution(priorities, location):
    documents = Queue()
    answer = 0

    for i, v in enumerate(priorities):
        documents.put((i, v))

    while len(documents.queue) > 0:
        document = documents.get()
        if document[1] < (len(documents.queue) > 0 and max(documents.queue, key=lambda x: x[1])[1]):
            documents.put(document)
        else:
            answer += 1
            if document[0] == location:
                break
    return answer

