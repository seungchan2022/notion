# 투 포인터 알고리즘(리스트에 순차적으로 접근해야 할 때 2가의 점의 위치를 기록하면서 처리하는 알고리즘)


# 특정한 합을 가지는 부분 연속 수열 찾기

n = 5       # 데이터의 개수
m = 5       # 찾고자 하는 부분합
data = [1, 2, 3, 2, 5]  # 전체 수열

count = 0       # 부분합의 개수
interval_sum = 0    # 부분합
end = 0     # 끝점

# start를 차례대로 증가시키며 반복
for start in range(n):
    # end를 가능한 만큼 이동시키기
    while interval_sum < m and end < n:
        interval_sum += data[end]
        end += 1
    # 부분합이 m일 때 카운트 증가
    if interval_sum == m:
        count += 1
    # 부분합이 m보다 크거나 같으면 start를 1 증가시키기 때문에 이전 start값을 빼주어야 한다.
    interval_sum -= data[start]

print(count)

"""
특정한 합을 가지는 부분 연속 수열 찾기
(이코테 p.475 그림)

1) 시작점(start)과 끝점(end)이 첫 번째 원소의 인데스(0)을 가리키도록 한다.
2) 현재 부분합이 M과 같다면 카운트 한다.
3) 현재 부분합이 M보다 작으면 end를 1 증가시킨다.
4) 현재 부분합이 M보다 크거나 같으면 start를 1 증가 시킨다.
5) 모든 경우를 확인할 때 까지 2)번부터 4)번까지의 과정을 반복한다.
"""