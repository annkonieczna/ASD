def EulerCycle(G, start_v):
    def is_connected():
        visited = [False] * n
        stack = [start_v]
        visited[start_v] = True
        count = 1
        while stack:
            u = stack.pop()
            for v in G[u]:
                if not visited[v]:
                    visited[v] = True
                    stack.append(v)
                    count += 1
        return count == n

    def DFS_visit(u):
        nonlocal cycle
        for v in G[u]:
            if M[u][v] > 0:
                M[u][v] -= 1
                M[v][u] -= 1
                DFS_visit(v)
        cycle.append(u)

    n = len(G)
    if n == 0:
        return None

    # 1. Sprawdzenie spójności
    if not is_connected():
        return None

    # 2. Sprawdzenie parzystości stopni
    for i in range(n):
        if len(G[i]) % 2 != 0:
            return None

    # 3. Inicjalizacja macierzy sąsiedztwa
    M = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in G[i]:
            M[i][j] += 1

    # 4. Znajdowanie cyklu DFS
    cycle = []
    DFS_visit(start_v)
    return cycle[::-1]