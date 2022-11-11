# 바이너리 인덱스 트리

# 변경 되는 데이터 에서 구간 합 구하는 문제

import sys
input = sys.stdin.readline

# 데이터의 개수(n), 변경 횟수(m), 구간합 계산 횟수(k)
n, m, k = map(int, input().split())

arr = [0] * (n + 1)
tree = [0] * (n + 1)

# i번째 수 까지의 누적합을 계산하는 함수
def prefix_sum(i):
    result = 0
    while i > 0:
        result += tree[i]
        # 0이 아닌 마지막 비트만큼 빼가면서 이동
        i -= (i & -i)
    return result

# i번째 수를 dif(특정값)만큼 더하는 함수
def update(i, dif):
    while i <= n:
        tree[i] += dif
        i += (i & -i)

# start부터 end까지의 구간합을 계산하는 함수
def interval_sum(start, end):
    return prefix_sum(end) - prefix_sum(start - 1)

for i in range(1, n + 1):
    x = int(input())
    arr[i] = x
    update(i, x)

for i in range(m + k):
    a, b, c = map(int, input().split())
    # 업데이트(update)연산인 경우
    if a == 1:
        update(b, c - arr[b])   # 바뀐 크기(dif)만큼 적용
        arr[b] = c
    # 구간합(interval_sum)연산인 경우
    else:
        print(interval_sum(b, c))
        


# https://www.acmicpc.net/problem/2042
