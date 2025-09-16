def dynamicArray(n, queries):
    arr = [[] for _ in range(n)]
    lastAnswer = 0
    answers = []
    for q_type, x, y in queries:
        idx = (x ^ lastAnswer) % n
        if q_type == 1:
            arr[idx].append(y)
        elif q_type == 2:
            lastAnswer = arr[idx][y % len(arr[idx])]
            answers.append(lastAnswer)
    return answers
if __name__ == '__main__':
    n, q = map(int, input().split())
    queries = []
    for _ in range(q):
        queries.append(list(map(int, input().split())))
    result = dynamicArray(n, queries)
    for val in result:
        print(val)
