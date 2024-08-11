from lib.outPutPrint import outPutPrint


def optimalFreelancing_first_solution(jobs):
    current_day = [0] * 7
    for job in jobs:
        index = min(job["deadline"], 7)
        for i in reversed(range(index)):
            if current_day[i] == 0:
                current_day[i] = job["payment"]
                break
            elif current_day[i] < job["payment"]:
                if i > 0:
                    current_day[i - 1] = max(current_day[i], current_day[i - 1])
                current_day[i] = job["payment"]
                break
    return sum(current_day)


def optimalFreelancing(jobs):
    current_day = [0] * 7
    jobs.sort(key=lambda x: x["payment"], reverse=True)
    total_profit = 0
    for job in jobs:
        index = min(job["deadline"], 7)
        for i in reversed(range(index)):
            if current_day[i] == 0:
                current_day[i] = job["payment"]
                total_profit += job["payment"]
                break
    return total_profit


data = [
    {
        "deadline": 1,
        "payment": 1
    },
    {
        "deadline": 1,
        "payment": 2
    }
]
output = optimalFreelancing(data)
outPutPrint(data, output)
