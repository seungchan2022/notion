# 서로소 집합 알고리즘(경로 압축)

# 특정 원소가 속한 집합 찾기
def find_parent(parent, x):     # (부모테이블, 노드 번호)
    # 루트 노드가 아니라면, 루트 노드를 찾을 때까지 재귀적으로 호출
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

# 두 원소가 속한 집합 합치기
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

# 노드의 개수와 간선(union 연산)의 개수
v, e = map(int, input().split())
parent = [0] * (v + 1)  # 부모 테이블 초기화

# 부모 테이블상에서, 부모를 자기 자신으로 초기화
for i in range(1, v + 1):
    parent[i] = i

# union 연산 각각 수행
for i in range(e):
    a, b = map(int, input().split())
    union_parent(parent, a, b)

# 각 원소가 속한 집합 출력(각 원소의 루트 노드)
for i in range(1, v + 1):
    # 루트 노드가 같으면 같은 집합
    print(find_parent(parent, i), end=' ')

# 부모 테이블 내용 출력
for i in range(1, v + 1):
    print(parent[i], end=' ')

    
"""
union 연산: 2개의 원소가 포함된 집합을 하나의 집합으로 합치는 연산
find 연산: 특정한 원소가 속한 집합이 어떤 집합인지 알려주는 연산
3 ~ 8를 경로 압축기법 이라고 하는데 경로 압축은 find함수를 재귀적으로 호출한 뒤에 부모 테이블값을 갱신하는 기법
이렇게 하면 각 노드에 대하여 find 함수를 호출한 이후에, 해당 노드의 루트노드가 바로 부모 노드가 된다.
"""
