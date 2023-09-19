# Количество вершин
nV = 8
INF = 999
# Алгоритм
def floyd(G):
    dist = list(map(lambda p: list(map(lambda q: q, p)), G))
    # Добавление вершин по отдельности
    for r in range(nV):
        for p in range(nV):
            for q in range(nV):
                dist[p][q] = min(dist[p][q], dist[p][r] + dist[r][q])
    sol(dist)
# Выходные данные
def sol(dist):
    for p in range(nV):
        for q in range(nV):
            if(dist[p][q] == INF):
                print("INF", end=" ")
            else:
                print(dist[p][q], end="  ")
        print(" ")
# Наша матрица
G = [[0, 2,INF, 3, 1, INF, INF, 10],
     [2, 0, 4, INF, INF, INF, INF, INF],
     [INF, 4, 0,INF,INF,INF,INF, 3],
     [3,INF,INF, 0, INF,INF,INF, 8],
     [1,INF,INF,INF, 0, 2,INF,INF],
     [INF,INF,INF,INF, 2, 0, 3,INF],
     [INF,INF,INF,INF,INF, 3, 0, 1],
     [10, INF, 3, 8,INF,INF, 1, 0],
]
floyd(G)
