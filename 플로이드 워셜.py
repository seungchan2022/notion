# 플로이드 워셜 알고리즘
INF = int(1e9)

# 노드, 간선
n, m = map(int, input().split())
# 2차원 리스트를 만들고, 모든 값을 무한으로 초기화
graph = [[INF] * (n + 1) for _ in range(n + 1)]

# 자기 자신에서 자기 자신으로 가는 비용은 0으로 초기화
for a in range(1, n + 1):
    for b in range(1, n + 1):
        if a == b:
            graph[a][b] = 0

# 각 간선에 대한 정보
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a][b] = c     # a -> b로 가는 비용: c

# 점화식에 따라 플로이드 워셜 알고리즘 수행
for k in range(1, n + 1):           # k: 거쳐가는 노드
    for a in range(1, n + 1):       # a: 출발 노드
        for b in range(1, n + 1):   # b: 도착 노드
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

# 결과
for a in range(1, n + 1):
    for b in range(1, n + 1):
        if graph[a][b] == INF:
            print('INF', end=' ')
        else:
            print(graph[a][b], end=' ')
    print()

    
"""
플로이드 워셜 알고리즘
- 모든 지점에서 다른 모든 지점까지의 최단 경롤르 모두 구해야 하는 경우 사용
- 단계마다 '거쳐 가는 노드'를 기준으로 알고리즘을 수행하지만, 매번 방문하지 않은 노드중에서 최단 거리를 갖는 노드를 찾을 필요가 없다
- 2차원 리스트에 '최단 거리'정보 저장, 모든 노드에 대하여 다른 모든 노드로 가는 최단 거리 정보를 담아야 하기 때문
- 다이나믹 프로그래밍 Dab = min(Dab, Dak + Dkb)
- k: 거쳐가는 노드, a: 출발 노드, b: 도착 노드
"""
