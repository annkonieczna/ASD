def drivers( P, B ):
    n = len(P)
    ojacieniemoge = P[:]
    for i in range(n):
        ojacieniemoge[i] = (P[i][0], P[i][1], i)
    points = sorted(ojacieniemoge, key=lambda x:x[0])

    J = 0
    M = 1
    naps = 3

    dp = [[[float("inf") for _  in range(2)] for _ in range(naps)] for _ in range(n + 1)]

    dp[0][0][J] = 0

    last_index = n

    for p in range(n):
        s = p + 1

        if points[p][0] > B:
            last_index = s
            break

        if not points[p][1]:
            for i in range(naps):
                dp[s][i][J] = dp[s - 1][i][J]
                dp[s][i][M] = dp[s - 1][i][M] + 1
            continue

        for i in range(naps - 1, 0, -1):
            dp[s][i][J] = dp[s - 1][i - 1][J]
            dp[s][i][M] = dp[s - 1][i - 1][M]

        dp[s][0][J] = min(dp[s - 1], key=lambda x:x[M])[M]
        dp[s][0][M] = min(dp[s - 1], key=lambda x:x[J])[J]

    res = []

    min_cost = float("inf")
    driver = J
    fatique = 0
    for i in range(naps):
        for d in range(2):
            if dp[last_index][i][d] <= min_cost:
                min_cost = dp[last_index][i][d]
                driver = d
                fatique = i

    for i in range(last_index, 0, -1):
        p = i - 1
        current = dp[i][fatique][driver]


        if points[p][1]:
            if fatique > 0 and dp[i - 1][fatique - 1][driver] <= current:
                fatique -= 1
                continue
        else:
            if dp[i - 1][fatique][driver] <= current:
                continue

        res.append(points[p][2])
        driver = 1 - driver # Swap the drivers
        for f in range(naps):
            if dp[i - 1][f][driver] == current:
                fatique = f
                continue

    return res
