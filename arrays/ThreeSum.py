#Given a list of numbers and a target,
#Find the sum of three numbers from the list that's closest to the target.

def threeSumClosest(self, nums: List[int], target: int) -> int:
    k = 1
    log = {}
    sums = {}
    for i in nums:
        log[k] = i
        k += 1
    print(log)

    for a, b in log.items():
        for m, n in log.items():
            if a == m:
                continue
            for c, d in log.items():
                if a == c or m == c:
                    continue
                l = abs(target - (b + n + d))
                sums[b + n + d] = l

    t = 1000000
    for key, value in sums.items():
        if value < t:
            t = value
            h = key

    return h
