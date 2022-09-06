# 위상 정렬 알고리즘(선수 과목)

from collections import deque

# 노드의 개수와 간선의 개수
v, e = map(int, input().split())
# 모든 노드에 대한 진입차수 0으로 초기화
indegree = [0] * (v + 1)
# 각 노드에 연결된 간선 정보를 담기 위한 연결 리스트 초기화
graph = [[] for i in range(v + 1)]

# 방향 그래프의 모든 간선 정보 입력
for _ in range(e):
    a, b = map(int, input().split())
    graph[a].append(b)  # a -> b
    # 진입차수 + 1
    indegree[b] += 1

# 위상 정렬 함수
def topology_sort():
    result = []     # 결과 리스트
    q = deque()

    # 처음 시작할 때는 진입차수가 0인 노드 큐에 삽입
    for i in range(1, v + 1):
        if indegree[i] == 0:
            q.append(i)
    
    while q:
        now = q.popleft()
        result.append(now)
        # 해당 원소와 연결된 노드들의 진입차수에서 -1
        for i in graph[now]:
            indegree[i] -= 1
            # 새롭게 진입차수가 0이 되는 노드 큐에 삽입
            if indegree[i] == 0:
                q.append(i)

    # 결과 출력
    for i in result:
        print(i, end=' ')

topology_sort()



"""
순서가 정해져 있는 일련의 작업을 차례대로 수행해야 할 때 사용할 수 있는 알고리즘
방향 그래프의 모든 노드를 '방향성에 거스르지 않도록 순서대로 나열하는 것'
그래프상에서 선후 관계가 있다면, 위상 정렬을 수행하여 모든 선후 관계를 지키는 전체 순서를 계산할 수 있다
진입차수: 특정한 노드로 '들어오는' 간선의 개수
작동 원리:
1. 진입차수가 0인 노드를 큐에 넣는다
2. 큐가 빌 때까지 다음의 과정 반복
 1). 큐에서 원소를 꺼내 해당 노드에서 출발하는 간선을 그래프에서 제거
 2). 새롭게 진입차수가 0이 된 노드를 큐에 넣는다
모든 원소를 방문하기 전에 큐가 빈다면 사이클이 존재
"""
