# 다익스트라 알고리즘(우선순위 큐)
import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

# 노드, 간선
n, m = map(int, input().split())
start = int(input())    # 시작 노드 번호
# 각 노드에 연결되어 있는 노드에 대한 정보를 담는 리스트
graph = [[] for _ in range(n + 1)]
# 최단 거리 테이블 모두 무한으로 초기화
distance = [INF] * (n + 1)

# 모든 간선 정보 입력
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))     # a -> b로 가는 비용: c

def dijkstra(start):
    q = []
    # 시작 노드로 가기위한 최단 경로 0으로 설정하고, 큐에 삽입
    distance[start] = 0
    heapq.heappush(q, (0, start))      # (거리, 노드)

    while q:
        # 가장 최단 거리가 짧은 노드에 대한 정보 꺼내기
        dist, now = heapq.heappop(q)
        # 현재 노드가 이미 처리 된적이 있는 노드라면 무시
        if distance[now] < dist:
            continue
        # 현재 노드와 연결된 다른 인접 노드들 확인
        for i in graph[now]:
            cost = dist + i[1]      # graph의 i[1] = 거리
            # 현재 노드를 거쳐서, 다른 노드로 이동하는 거리가 더 짧은 경우
            if cost < distance[i[0]]:   # i[0]: 노드 번호
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

dijkstra(start)

# 결과 
for i in range(1, n + 1):
    if distance[i] == INF:
        print('INF')
    else:
        print(distance[i])

"""
다익스트라 알고리즘
- 한 지점에서 다른 특정 지점까지의 최단 경로를 구해야 하는 경우 사용
- 단계마다 최단 거리를 가지는 노드를 하나씩 반복적으로 선택하고, 해당 노드를 거쳐 가며 경로를 확인하며, 최단 거리 테이블 갱신
- 출발 노드가 1개 이므로 다른 모든 노드까지의 최단 거리를 저장하기 위해서 1차원 리스트 이용
- 그리디 알고리즘
"""
