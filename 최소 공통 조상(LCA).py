# 최소 공통 조상(LCA) 찾기 -> 다이나믹 프로그래밍 이용

import sys
sys.setrecursionlimit(int(1e5))
input = sys.stdin.readline
LOG = 21    # 2^20 = 1,000,000

n = int(input())
parent = [[0] * LOG for _ in range(n + 1)]  # 부모 노드 정보
d = [0] * (n + 1)   # 각 노드까지의 깊이
c = [False] * (n + 1)   # 각 노드의 깊이가 계산되었는지 여부
graph = [[] for _ in range(n + 1)]  # 트리 정보

for _ in range(n - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# 루트 노드부터 시작하여 깊이(depth)를 구하는 함수
def dfs(x, depth):
    c[x] = True
    d[x] = depth    # 매번 노드에 대해서 깊이 기록
    for i in graph[x]:  # 인접 노드 확인
        if c[i]:    # 이미 깊이를 구했다면
            continue
        parent[i][0] = x    # 한 칸 위에 있는 부모에 대한 정보만 먼저 구함
        dfs(i, depth + 1)

# 전체 부모 관계를 설정하는 함수
# 다이나믹 프로그래밍 이용해 각 노드에 대하여 2^i번째 부모에 대한 정보 기록
def set_parent():
    dfs(1, 0)   # 루트 노드는 1번 노드
    for i in range(1, LOG):
        for j in range(1, n + 1):
            parent[j][i] = parent[parent[j][i - 1]][i - 1]

# A와 B의 최소 공통 조상을 찾는 함수
def lca(a, b):
    # b가 더 깊도록 설정
    if d[a] > d[b]:
        a, b = b, a
    # 먼저 깊이(depth)가 동일하도록
    # 큰 크기부터 작은 크기까지 차례대로 확인 하면서 거슬러 올라가기 ex) 15: 8 -> 4 -> 2 -> 1
    for i in range(LOG - 1, -1, -1):
        if d[b] - d[a] >= (1 << i):
            b = parent[b][i]    # 더 깊은 쪽의 깊이가 줄어들도록
    # 부모가 같아 지도록
    if a == b:
        return a
    for i in range(LOG - 1, -1, -1):
        # 조상을 향해 올라가기
        if parent[a][i] != parent[b][i]:
            a = parent[a][i]
            b = parent[b][i]
    # 이후에 부모가 찾고자 하는 조상
    parent[a][0]

set_parent()

m = int(input())    # LCA를 구할 쌍의 수

for i in range(m):
    a, b = map(int, input().split())
    print(lca(a, b))

"""
최소 공통 조상
1. 모든 노드에 대한 깊이 계산
2. 최소 공통 조상을 찾을 두 노드 확인
    1. 먼저 두 노드의 깊이가 동일하도록 거슬러 올라간다
    2. 이후에 부모가 같아질 때까지 반복적으로 두 노드의 부모 방향으로 거슬러 올라간다
3. 모든 LCA(a, b)연산에 대하여 2번의 과정 반복


개선된 최소 공통 조상 알고리즘(다이나믹 프로그래밍 이용)
- 메모리를 조금 더 사용하여 각노드에 대하여 2^i 번째 부모에 대한 정보 기록
- 2의 제곱 형태로 거슬러 올라가도록
1. 먼저 두 노드의 깊이를 맞춘다
2. 이후에 거슬러 올라간다(2^i 형태로 빠르게 올라가도록함)
"""
