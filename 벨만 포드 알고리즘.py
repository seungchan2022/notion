# 벨만 포드 알고리즘

import sys
input = sys.stdin.readline
INF = int(1e9)

n, m = map(int, input().split())    # 노드, 간선
edges = []      # 모든 간선에 대한 정보를 담는 리스트
dist = [INF] * (n + 1)  # 최단 거리 테이블 모두 무한으로 초기화

for _ in range(m):
    a, b, c = map(int, input().split())
    edges.append((a, b, c))     # edges[a].append((b, c)) => X

def bf(start):
    dist[start] = 0     # 시작 노드 초기화
    for i in range(n):      # 전체 n번의 라운드(round) 반복
        # 매 반복마다 "모든 간선"을 확인 하며
        for j in range(m):
            cur = edges[j][0]
            next_node = edges[j][1]
            cost = edges[j][2]
            # 현재 간선을 거쳐서 다른 노드로 이동하는 거리가 더 짧은 경우
            if dist[cur] != INF and dist[next_node] > dist[cur] + cost:
                dist[next_node] = dist[cur] + cost
                # n번째 라운드에서도 값이 갱신된다면 음수 순환이 존재
                if i == n - 1:
                    return True
    return False

# 벨만 포드 알고리즘 수행
negative_cycle = bf(1)      # 1번노드가 시작 노드

if negative_cycle:
    print('-1')
else:
    # 1번 노드를 제외한 다른 모든 노드로 가기위한 최단거리 출력
    for i in range(2, n + 1):
        # 도달할 수 없는 경우 -1
        if dist[i] == INF:
            print('-1')
        else:
            print(dist[i])


"""
벨만 포드 최단 경로 알고리즘은 음의 간선이 포함된 상황에서 사용할 수 있다.

작동 원리
1. 출발 노드 설정
2. 최단 거리 테이블 초기화
3. 다음의 과정 N - 1번 반복
    1) 전체 간선 E개를 하나씩 확인
    2) 각 가선을 거쳐 다른 노드로 가는 비용을 계산하여 최단 거리 테이블 갱신

만약 음수 간선 순환이 발생하는지 체크하고 싶다면 3번의 과정을 한 번 더 수행
이때, 최단 거리 테이블이 갱신된다면 음수 간선 순화이 존재하는 것
양수 사이클이 존재 할수도 있다.
"""
