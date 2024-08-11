from lib.outPutPrint import outPutPrint


def taskAssignment(k, tasks):
    tasks_sor = sorted(tasks)
    result = []
    ref = dict()
    for i, task in enumerate(tasks):
        if task in ref:
            ref[task].append(i)
        else:
            ref[task] = [i]
    i = 0
    j = len(tasks_sor) - 1
    while i < k:
        i_index = ref[tasks_sor[i]].pop()
        j_index = ref[tasks_sor[j]].pop()
        result.append([i_index, j_index])
        i += 1
        j -= 1

    return result


data = dict(
    k=3,
    tasks=[1, 3, 5, 3, 1, 4]
)
output = taskAssignment(data["k"], data["tasks"])

outPutPrint(data, output)

data = dict(
    k=4,
    tasks=[1, 2, 3, 4, 5, 6, 7, 8]
)
output = taskAssignment(data["k"], data["tasks"])

outPutPrint(data, output)
