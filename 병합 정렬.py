# 2751

# 병합 정렬

def merge_sort(array):
    if len(array) <= 1:
        return array

    # 재귀함수를 이용
    mid = len(array) // 2
    left = merge_sort(array[:mid])
    right = merge_sort(array[mid:])

    i, j, k = 0, 0, 0       # k: 정렬할 배열의 index

    # 양쪽 그룹의 index가 가리키는 값을 비교한 후 더 작은 수를 선택해 배열에 저장하고
    # 선택된 배열과 정렬하는 배열의 index를 + 1, 반복문이 끝나고 남아 있는 데이터 처리
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            array[k] = left[i]
            i += 1
            k += 1
        else:
            array[k] = right[j]
            j += 1
            k += 1

    # 한쪽 그룹이 모두 정렬된 후 다른 그룹의 남아있는 데이터 처리
    if i == len(left):      # 왼쪽 데이터를 먼저 다 배열한 경우
        while j < len(right):       # 남아있는 오른쪽 데이터 처리
            array[k] = right[j]
            j += 1
            k += 1

    elif j == len(right):   # 오른쪽 데이터를 먼저 다 배열한 경우
        while i < len(left):        # 남아있는 왼쪽 데이터 처리
            array[k] = left[i]
            i += 1
            k += 1
    return array


n = int(input())

array = []
for _ in range(n):
    array.append(int(input()))

result = merge_sort(array)

for i in result:
    print(i)



# 병합 정렬 개념 설명
# https://www.youtube.com/watch?v=ctkuGoJPmAE
