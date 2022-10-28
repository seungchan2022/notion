# 이진 탐색(재귀 함수)
def binary_search(array, target, start, end):
    if start > end:
        return None
    mid = (start + end) // 2
    # 찾은 경우 중간점 인덱스 반환
    if array[mid] == target:
        return mid
    # 중간점의 값보다 찾고자 하는 값이 작은 경우 왼쪽 확인(중간점 > target)
    elif array[mid] > target:
        return binary_search(array, target, start, mid - 1)
    # 중간점의 값보다 찾고자 하는 값이 더 큰 경우 오른쪽 확인(중간점 < target)
    else:
        return binary_search(array, target, mid + 1, end)

n, target = map(int, input().split())
array = list(map(int, input().split()))

# 이진 탐색 수행 결과(index 출력)
result = binary_search(array, target, 0, n - 1)
if result == None:
    print('None')
else:
    print(result)

------------------------------------------------------------------------------------------------------

# 이진 탐색(반복문)
def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        # 찾은 경우 중간점 인덱스 반환
        if array[mid] == target:
            return mid
        # 중간점의 값보다 찾고자 하는 값이 작은 경우 왼쪽 확인(중간점 > target)
        elif array[mid] > target:
            end = mid - 1
        # 중간점의 값보다 찾고자 하는 값이 더 큰 경우 오른쪽 확인(중간점 < target)
        else:
            start = mid + 1
    return None

n, target = map(int, input().split())
array = list(map(int, input().split()))

# 이진 탐색 수행 결과(index 출력)
result = binary_search(array, target, 0, n - 1)
if result == None:
    print('None')
else:
    print(result + 1)
