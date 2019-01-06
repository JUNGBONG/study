def crossBridge(steps):
    cnt = 0
    current = 0
    n = len(steps)
    while (n>=current):
        current += steps[current]
        cnt += 1
    return cnt

crossBridge([1, 1, 2, 3, 5])


